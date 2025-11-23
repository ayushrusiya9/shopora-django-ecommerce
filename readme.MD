# SHOPORA-django-Ecommerce website

Shopora is a modern, responsive, and modular e-commerce web application built using Django, Bootstrap, and Razorpay for payments.  
It provides a clean UI, secure checkout flow, reusable components, and a scalable architecture suitable for real-world projects.

## ⭐ Features

### 🔹 Core Features
- Fully responsive home page with modern UI  
- Dynamic product listing & product detail pages  
- Add to cart, update cart, remove items  
- Razorpay payment gateway integration  
- Automatic order creation on successful payment  
- Django admin for managing products & orders  

### 🔹 UI/UX Features
- Reusable Navbar & Footer  
- Services page with hover animation cards  
- mobile-friendly layout  

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Backend | Django (Python) |
| Frontend | HTML, CSS, Bootstrap 5 |
| Database | SQLite3 |
| Payment Gateway | Razorpay |
| Version Control | Git & GitHub |

```

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/shopora.git
cd shopora
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
venv/scripts/activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py migrate
```

### 5. Start Development Server
```bash
python manage.py runserver
```

## 💳 Razorpay Integration Setup

1. Go to Razorpay Dashboard → API Keys  
2. Generate a Key ID and Key Secret  
3. Add the keys in settings.py:

```python
RAZORPAY_KEY_ID = "your_key_id"
RAZORPAY_KEY_SECRET = "your_key_secret"
```

4. Use Razorpay script on checkout page:

```html
<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
```

## 📦 Features Implemented Per Page

### 1️⃣ Home Page
- Product preview  
- Bootstrap-based responsive layout  

### 2️⃣ Services Page
- Three service cards  
- Icons + description + image  
- Hover effects

### 3️⃣ Checkout Page
- Razorpay script integrated  
- Card-based layout  
- Dynamic total amount  

## 📸 Screenshots (Add Later)

You can add your own images like:

```
/screenshots/
    home.png
    services.png
    product.png
    cart.png
    checkout.png
    admin.png
```


## 👤 Developer

**Ayush Rusiya**  
📍 Bhopal, India  
🔗 LinkedIn: https://www.linkedin.com/in/ayushrusiya/  
🔗 GitHub: https://github.com/ayushrusiya9  
