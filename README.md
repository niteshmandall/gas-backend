
# **Customer Support Management System : Bynry Inc Assignment**

This Django-based web application is designed to handle customer support requests efficiently. The application provides features for customers to submit and track their requests, while support representatives can manage and resolve these requests. 

## **Features**
### **Customer Features**
- Submit service requests with details and optional file attachments.
- Track the status of submitted requests.
- View details of individual requests.

### **Support Features**
- View and manage all customer service requests.
- Update the status of requests (e.g., Pending, In Progress, Resolved).
- Add comments to service requests for internal communication.
- Role-based access control to restrict access to support features.

### **Authentication and Authorization**
- User authentication using Django's built-in system.
- Role-based access:
  - **Customers** can only submit and track requests.
  - **Support team** can manage and resolve requests.

---

## **Installation**

### **Prerequisites**
- Python 3.8 or above
- Django 4.x
- A virtual environment manager (e.g., `venv` or `virtualenv`)
- Database (SQLite by default)

### **Steps**
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/customer-support-system.git
   cd customer-support-system
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create Superuser (Admin)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   Access the application at [http://localhost:8000/](http://localhost:8000/).

---

## **Usage**

### **1. Setup Groups**
1. Log in to the Django Admin at `/admin/`.
2. Create two groups: **Customer** and **Support** under **Groups**.
3. Assign users to these groups based on their roles.

### **2. Access Control**
- **Customers**:
  - Can submit service requests via the `/customer/` route.
  - Can track their requests.
- **Support Team**:
  - Can manage requests via the `/support/` route.
  - Can update statuses and add comments.

### **3. Redirect Logic**
- The homepage `/` redirects users based on their role:
  - Customers are redirected to `/customer/`.
  - Support team members are redirected to `/support/`.
  - Users without roles are redirected to the admin login.

---

## **File Structure**
```plaintext
customer-support-system/
├── customer/
│   ├── templates/
│   │   └── customer/
│   │       ├── submit_request.html
│   │       ├── request_list.html
│   │       └── request_detail.html
│   ├── views.py
│   ├── models.py
│   └── urls.py
├── support/
│   ├── templates/
│   │   └── support/
│   │       ├── manage_requests.html
│   │       ├── request_detail.html
│   │       └── update_status.html
│   ├── views.py
│   ├── models.py
│   └── urls.py
├── gas/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

---

## **Key Technologies**
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite (default), can be replaced with PostgreSQL/MySQL
- **Authentication**: Django's built-in user management system

---

## **Future Enhancements**
- Add email notifications for request status updates.
- Implement file upload validation.
- Add support for multi-language localization.
- Enhance UI with modern frameworks like React or Vue.js.

---

## Some Default User IDs and Pass for testing :

- Customer - Username : customer, Pass : user@123
- Support  - Username : support , Pass : admin@123

---

 
