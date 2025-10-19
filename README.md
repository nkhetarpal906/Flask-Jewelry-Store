# Flask Jewelry Store - A Customizable E-commerce Platform

A full-stack, customizable e-commerce platform for jewelry stores built with Python and Flask. Features product management, user authentication, and an admin dashboard.

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
- [Project Structure](#project-structure)
- [Usage](#usage)

## Project Overview

This project is a complete and scalable e-commerce web application designed to serve as a versatile template for any online jewelry store. While originally a demo for a brand named "Pearl Box," its modular design allows for easy customization of the branding, products, and style.

The platform replaces a manual ordering system with a dynamic, web-based solution that automates the sales process. It is built on a foundation of modern web technologies and integrates advanced programming concepts like modular design, object-relational mapping (ORM), and secure authentication protocols to deliver a robust user experience.

## Key Features

**Customer-Facing Features:**

* **User Authentication:** Secure user registration and login functionality.
* **Product Catalog:** A responsive shop page to display all products, with options for filtering by category.
* **Sorting Capabilities:** Users can sort products by price (low to high, high to low) or by new arrivals.
* **Product Details Page:** Individual pages for each product with detailed descriptions, images, and pricing.
* **Simple Ordering Process:** A streamlined process for authenticated users to purchase products.
* **User Dashboard:** A personal dashboard for users to view their order history and track the status of their purchases.

**Administrative Features:**

* **Admin Dashboard:** A comprehensive admin panel for site administrators to manage the store.
* **Full CRUD for Products:** Admins can easily Create, Read, Update, and Delete products in the catalog.
* **Order Management:** View all customer orders and update their status (e.g., mark as "Delivered").
* **Secure Access:** The admin panel is protected and only accessible to users with the 'admin' role.

**Technical Features:**

* **Email Notifications:** Automated email confirmations are sent to users upon placing an order, and a notification is sent to the admin for each new sale.
* **Responsive Design:** The front-end is designed to be fully responsive, providing an optimal viewing experience on desktops, tablets, and mobile devices.
* **Modular & Scalable:** The codebase is organized into logical modules (e.g., models, routes, forms), making it easy to maintain and extend.

## Tech Stack

* **Backend:** Python, Flask
* **Database:** SQLite (with SQLAlchemy ORM)
* **Frontend:** HTML, CSS, JavaScript, Jinja2 Templating
* **Flask Extensions:**
    * Flask-SQLAlchemy for database interaction.
    * Flask-Login for managing user sessions.
    * Flask-WTF for secure form handling and validation.
    * Flask-Mail for sending emails.

## Getting Started

Follow these instructions to get a local copy of the project up and running on your machine for development and testing purposes.

### Prerequisites

* Python 3.6+
* pip package manager
* Git for version control

### Installation & Setup

1.  Clone the repository:
    ```bash
    git clone [https://github.com/nkhetarpal906/Flask-Jewelry-Store.git](https://github.com/nkhetarpal906/Flask-Jewelry-Store.git)
    cd Flask-Jewelry-Store
    ```

2.  Create and activate a virtual environment:
    * **Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * **macOS / Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4.  Run the application:
    ```bash
    python app.py
    ```
    The application will be running at `http://127.0.0.1:5000`. The first time you run it, it will automatically create a `pearlbox.db` file in an `instance` folder.

## Project Structure

The project is organized in a modular way to separate concerns and improve maintainability.
