# 📚 **Django Library Management**  

Django Library Management is a **web application** built with **Django, Razorpay, and Tailwind CSS** that provides an online platform for managing libraries.  

[![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)](https://github.com/rajaprerak/MusicPlayer/commits/master)  
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)  

This project is built using:  

![HTML5](https://www.w3.org/html/logo/downloads/HTML5_Logo_64.png)  
![CSS3](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CSS3_logo_and_wordmark.svg/48px-CSS3_logo_and_wordmark.svg.png)  
![Vanilla JS](https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/64px-Unofficial_JavaScript_logo_2.svg.png)  
![Python](https://www.quintagroup.com/++theme++quintagroup-theme/images/logo_python_section.png)  
![Django](https://www.quintagroup.com/++theme++quintagroup-theme/images/logo_django_section.png)  

---

## 🚀 **Installation Guide**  

### 📌 **1. Clone this repository:**
```bash
git clone https://github.com/your-username/django-library-management.git
cd django-library-management
```

### 📌 **2. Create and activate a virtual environment:**
```bash
python3 -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

### 📌 **3. Install dependencies:**
```bash
pip install -r requirements.txt
```

### 📌 **4. Apply database migrations:**
```bash
python manage.py migrate
```

### 📌 **5. Seed the database with dummy data (users & books):**
```bash
python manage.py seed_users
python manage.py seed_books
```

### 📌 **6. Create a superuser for admin access:**
```bash
python manage.py createsuperuser
```

### 📌 **7. Run the server:**
```bash
python manage.py runserver
```

### 📌 **8. Open the app in your browser:**
Go to: **[http://localhost:8000/](http://localhost:8000/)**  

---

## 🔥 **Features**

### 🏠 **Public Users**
✅ View all books on the homepage  
✅ Search books by **author, title, or category**  
✅ Sort books alphabetically by **title or author**  

### 🎓 **Students**
✅ Register / Login  
✅ Borrow books  
✅ View their borrowed books with **due return date**  
✅ Check & filter books by:  
   - Requested  
   - Issued  
   - All  

✅ View any outstanding fines  
✅ Online fine payment via **Razorpay**  

### 🛠 **Admin**
✅ Login to the **Admin Dashboard**  
✅ Manage book requests:  
   - View, Approve, or Reject requests  
   - Filter by **issued** or **returned** status  
✅ Add, delete, search, and filter books  
✅ Manage authors: Add, delete, search  
✅ Manage fines:  
   - Calculate fines  
   - Mark fines as **paid** (if paid in cash)  
   - Search fines by **student ID**  
✅ Manage students:  
   - Search, modify, add, delete  
   - Filter by department  
   - View **all books & fines** for a student  
✅ View user activity: **Last login, join date, assigned student**  
✅ Reset passwords for any user  

### 🔍 **Additional Features**
✅ Live validation during sign-up (checks if **Student ID** already exists)  
✅ Books display real-time status:  
   - **"Issued"** (if borrowed)  
   - **"Request Issue"** (if available)  

---

## 📊 **Seeding the Database**  

To generate dummy users and books, run the following commands:

### 📌 **1. Seed Users**
```bash
python manage.py seed_users
```
This will create **10 fake users** (students) with random names, emails, and login credentials.  

### 📌 **2. Seed Books**
```bash
python manage.py seed_books
```
This will generate **10 random books** with **titles, authors, and categories**.  

---

## 🛠 **Usage**  

### 🔹 **1. Run the server**  
```bash
python manage.py runserver
```

### 🔹 **2. Open in your browser**  
> Go to: **[http://localhost:8000/](http://localhost:8000/)**  

### 🔹 **3. Sign up or Log in**  

### 🔹 **4. Browse books & borrow**  

### 🔹 **5. Manage users & fines (Admin Only)**  

---

## 🎯 **Contributing**  

🚀 Want to improve this project? Feel free to fork this repository and submit a **pull request**!  

### 🔹 **Step 1:**
- 🍴 Fork this repo!  
- 👯 Clone this repo to your local machine.  

### 🔹 **Step 2:**
- **Build your code** 🔨🔨🔨  

### 🔹 **Step 3:**
- 🔃 Create a **new pull request**.  

---

## 🔖 **Credits**  

**Django Library Management** was created by **Mohammad Burhan**. 🎉  

---

## 📜 **License**  

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)  

📜 **Licensed under the MIT License** – [Read More](http://opensource.org/licenses/mit-license.php)  

---

🎯 **Enjoy using Django Library Management!** 🚀