# Gas Utility Customer Service Application

A modern, full-featured web application for managing gas utility customer service requests. Built with Django and Bootstrap.

## 🌟 Features

### Customer Features
- User Registration and Authentication
- Service Request Submission
- Request Tracking
- Profile Management
- Real-time Status Updates

### Admin Features
- Modern Admin Interface (Jazzmin)
- Customer Management
- Request Processing
- Service Status Updates
- Analytics Dashboard

## 🚀 Technology Stack

### Backend
- Python 3.11
- Django 5.1.3
- Django REST Framework
- SQLite Database

### Frontend
- Bootstrap 5.3
- Font Awesome 6.0
- Custom CSS with Variables
- Google Fonts (Poppins)
- JavaScript/jQuery

### Admin Interface
- Django Jazzmin Theme
- Custom Admin Views
- Enhanced User Management

## 📋 Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd gas-utility
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Unix/MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Ensure all user profiles exist:
```bash
python manage.py ensure_user_profiles
```

7. Run development server:
```bash
python manage.py runserver
```

## 🎨 UI/UX Features

### Modern Design Elements
- Responsive Layout
- Custom Color Scheme
- Interactive Components
- Smooth Animations
- Enhanced Typography
- Consistent Visual Language

### Key Pages
1. Home Page
   - Hero Section
   - Service Features
   - Statistics Display
   - Call-to-Action Areas

2. Authentication Pages
   - Modern Login Interface
   - Registration Form
   - Profile Management
   - Password Reset

3. Service Request System
   - Intuitive Request Form
   - Request Tracking
   - Status Updates
   - History View

## 👥 User Roles

### Customer
- Register/Login
- Submit Service Requests
- Track Request Status
- Update Profile
- View Request History

### Administrator
- Manage Users
- Process Requests
- Update Service Status
- View Analytics
- System Configuration

## 🔒 Security Features

- CSRF Protection
- Password Hashing
- Form Validation
- Secure Session Management
- Protected Admin Interface

## 📱 Responsive Design

- Mobile-First Approach
- Tablet Optimization
- Desktop Enhancement
- Cross-Browser Support

## 🛣️ Roadmap

### Short Term
- [ ] Implement Social Login
- [ ] Enhanced Search Functionality
- [ ] Email Notifications
- [ ] Request Categories

### Long Term
- [ ] API Development
- [ ] Mobile Application
- [ ] Real-time Chat Support
- [ ] Analytics Dashboard

