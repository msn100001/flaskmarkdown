# Website Header with Fly-Out Sidebar Menu

## Overview

This software is a simple Flask-based web application with a **responsive design** that includes the following features:

1. **Responsive Header and Footer**: The header and footer remain consistent in size and style across the application, with the footer always sticking to the bottom of the page.
2. **Fly-Out Sidebar Menu**: A fly-out sidebar menu that is initially hidden and can be toggled by clicking the hamburger icon on the top-right corner of the header.
3. **Content Pages**: Static content pages including the **Home**, **About**, **Contact**, **Login**, and **Dashboard** pages.
4. **Admin Functionality**: The admin can view submitted contact forms, delete submissions, and block specific IP addresses.

## Features

### Header

- The header spans the top of the page and includes:
    - A site title ("Website Header") centered vertically and horizontally.
    - A **red hamburger menu button** located in the top-right corner.
    - The **hamburger menu** initially appears as three stacked red horizontal lines.
- **Color**: Dark gray (`#333`) with white text.
- **Height**: Fixed padding of 12px for a clean layout.

### Hamburger Menu

- Positioned in the top-right corner of the header.
- Initially displayed as three red horizontal lines to resemble a "hamburger."
- **Interaction**:
    - Clicking the hamburger menu:
        - **Smooth animation**: The three lines transition into an "X."
        - **Fly-out menu**: A sidebar menu slides in from the right.
    - The **hamburger button** toggles the visibility of the sidebar menu.

### Fly-Out Navigation Menu

- **Hidden by default** and slides in from the right when activated.
- Contains vertically-stacked navigation links for:
    - **Home**
    - **About**
    - **Contact**
    - **Login**
    - **Dashboard**
- **Background color**: Dark gray (`#444`).
- Links appear in **white text**, and they change background color slightly when hovered.
- The sidebar uses **CSS transitions** to smoothly slide in and out.

### Main Content Area

- **Content**:
    - Each page (Home, About, etc.) has static placeholder content.
    - The main content area is **centered both vertically and horizontally** on the page using **Flexbox** layout.
    - The content includes a header for the page (e.g., "Welcome to the Home Page") and sample filler text for illustration.
  
### Footer

- Matches the **header** in color (`#333`) and style.
- The footer text ("Website Footer") is centered horizontally and vertically.
- The **footer is sticky** and always stays at the bottom of the page, even if the content is short.

### Responsive Design

- **Flexbox Layout**: Ensures that the main content fills the available space on the page.
- **CSS Media Queries**: Adjusts the layout and visibility of elements based on the screen size.
    - On smaller screens (e.g., mobile), the **hamburger menu** appears, and the sidebar menu becomes a fly-out.
    - For larger screens, the sidebar is hidden by default and can be triggered using the hamburger icon.

### Interactive Hamburger Menu

- The **hamburger icon** toggles between its traditional state (three lines) and a closing "X" when clicked.
- The **fly-out sidebar menu** smoothly slides in and out from the right when activated.
  
### Sticky Footer

- The footer remains at the bottom of the viewport, regardless of the content length.

### Static Content Pages

The software includes four pages, each of which is accessible through the navigation menu:

1. **Home Page**:
   - Displays a welcome message and static content.
   
2. **About Page**:
   - Includes information about the site or organization (static content).
   
3. **Login Page**:
   - A placeholder for future login functionality.
   
4. **Dashboard Page**:
   - Displays a placeholder for the admin dashboard.

### Simple Setup and Styling

- The application uses **Bootstrap** for core responsive elements (via CDN).
- Custom **CSS** for additional styling and interactivity.

## Installation Instructions

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:
    ```bash
    cd <project_directory>
    ```

3. Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the Flask app:
    ```bash
    python app.py
    ```

6. Open your browser and go to `http://localhost:5000` to view the application.

## Conclusion

This web application provides a clean and interactive UI with a responsive design and a fly-out sidebar menu, along with basic functionality like handling contact form submissions, blocking IP addresses, and user authentication.

---

Let me know if you need any further adjustments to the documentation or if you'd like to add additional features!
