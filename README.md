# 🛒 E-Commerce Website (Django)

A simple E-Commerce web application built using Django.

This project includes user authentication, product listing, cart system, checkout functionality, and order management.

---

## 🚀 Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- Git & GitHub

---

## 📌 Features

### 🔐 Authentication
- User Registration
- Login / Logout
- Restricted access (Login required to view products)

### 🛍 Product Management
- Product Name
- Price
- Image Upload
- Grid Layout (4 products per row)

### 🛒 Cart System
- Add to Cart
- Increase Quantity
- Decrease Quantity
- Remove Item
- Subtotal Calculation

### 📦 Orders
- Checkout Page
- Order Creation
- Order Success Page

### 🛠 Admin Panel
- Add / Edit / Delete Products
- Manage Orders
- Manage Users

---

## 📂 Project Structure

```bash
e-commerce-website/
│
├── ecommerce/                  # Project configuration folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── amazon/                     # Main e-commerce app
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── templates/
│   │   └── store/
│   │       ├── base.html
│   │       ├── product_list.html
│   │       ├── cart.html
│   │       ├── login.html
│   │       ├── register.html
│   │       └── order_success.html
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── images/
│
├── media/
│   └── products/               # Uploaded product images
│
├── db.sqlite3
├── manage.py
└── README.md
```

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/AnanyaMesta02/e-commerce-website.git
cd e-commerce-website
