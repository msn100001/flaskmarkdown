from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import markdown

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact_form.db'  # SQLite database URI
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# User model (for admin login)
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# Admin user (for simplicity, hardcoding with hashed password)
admin_user = User(id=1, username='admin', password=generate_password_hash('admin'))  # Store hashed password

users = {admin_user.username: admin_user}

@login_manager.user_loader
def load_user(user_id):
    return admin_user if user_id == '1' else None

# Page Content model to store markdown content for pages like Home and About
class PageContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_name = db.Column(db.String(100), nullable=False, unique=True)  # e.g. 'home', 'about'
    content = db.Column(db.Text, nullable=False)
    date_modified = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<PageContent {self.page_name}>'

# Contact form submission model
class ContactForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    comments = db.Column(db.Text, nullable=False)
    ip_address = db.Column(db.String(50), nullable=False, default='')  # IP address
    date_submitted = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<ContactForm {self.name}>'

# Route for Home Page
@app.route('/', methods=['GET', 'POST'])
def home():
    page_content = PageContent.query.filter_by(page_name='home').first()  # Get content from the database

    if request.method == 'POST':
        markdown_content = request.form['markdown']  # Get the markdown input from the form
        if page_content:
            page_content.content = markdown_content  # Update existing content
        else:
            new_content = PageContent(page_name='home', content=markdown_content)
            db.session.add(new_content)  # Add new content if none exists
        db.session.commit()

    content_html = markdown.markdown(page_content.content) if page_content else ""  # Convert markdown to HTML
    return render_template('home.html', content=content_html, markdown_content=page_content.content if page_content else "")

# Route for About Page
@app.route('/about', methods=['GET', 'POST'])
def about():
    page_content = PageContent.query.filter_by(page_name='about').first()  # Get content from the database

    if request.method == 'POST':
        markdown_content = request.form['markdown']  # Get the markdown input from the form
        if page_content:
            page_content.content = markdown_content  # Update existing content
        else:
            new_content = PageContent(page_name='about', content=markdown_content)
            db.session.add(new_content)  # Add new content if none exists
        db.session.commit()

    content_html = markdown.markdown(page_content.content) if page_content else ""  # Convert markdown to HTML
    return render_template('about.html', content=content_html, markdown_content=page_content.content if page_content else "")

# Route for Contact Form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        phone_number = request.form['phone_number']
        comments = request.form['comments']
        ip_address = request.remote_addr

        new_submission = ContactForm(name=name, email=email, address=address, phone_number=phone_number, comments=comments, ip_address=ip_address)
        db.session.add(new_submission)
        db.session.commit()

        flash('Your message has been sent!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

# Route for Dashboard (only accessible to admin)
@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.username != 'admin':  # Only allow admin to access
        return redirect(url_for('home'))

    submissions = ContactForm.query.all()  # Get all contact form submissions
    return render_template('dashboard.html', submissions=submissions)

# Route to delete contact form entries
@app.route('/delete_submission/<int:id>', methods=['POST'])
@login_required
def delete_submission(id):
    if current_user.username != 'admin':
        return redirect(url_for('home'))

    submission_to_delete = ContactForm.query.get_or_404(id)
    db.session.delete(submission_to_delete)
    db.session.commit()
    flash('Submission deleted successfully', 'danger')
    return redirect(url_for('dashboard'))

# Route to block an IP
@app.route('/block_ip/<string:ip>', methods=['POST'])
@login_required
def block_ip(ip):
    if current_user.username != 'admin':
        return redirect(url_for('home'))

    blocked_ip = BlockedIP(ip_address=ip)
    db.session.add(blocked_ip)
    db.session.commit()
    flash(f"IP {ip} has been blocked.", 'warning')
    return redirect(url_for('dashboard'))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Create the database tables inside an application context
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(debug=True)
