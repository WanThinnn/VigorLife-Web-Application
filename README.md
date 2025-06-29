# VigorWeb - Health & Weight Management Platform

A comprehensive Django web application that combines health monitoring and weight management features. This project was developed as an academic assignment to create a user-friendly platform for health-conscious individuals.

## Project Overview

VigorWeb is a health and weight management web application built with Django. The platform provides users with tools to track calories, calculate health metrics, access exercise routines, and explore healthy recipes. The application features modern web technologies and integrates with cloud services for enhanced functionality.
![đemo-1](https://github.com/user-attachments/assets/91ca8294-b48f-488b-b6ae-394f1cfa8ff9)
![demo-2](https://github.com/user-attachments/assets/d47608d1-cc2c-4792-84f5-9c1b58cb27f8)

## Technology Stack

**Backend:**
- **Django** - Python web framework for rapid development and clean design
- **Python** - Primary programming language
- **MySQL** - Relational database for data storage and management

**Frontend:**
- **HTML5** - Markup language for structuring web content
- **CSS3** - Styling and responsive design
- **JavaScript** - Client-side interactivity and dynamic features

**Cloud Services:**
- **AWS RDS MySQL** - Cloud database hosting
- **AWS S3** - Media file storage
- **AWS EC2** - Web application deployment
- **Google Cloud Vision API** - Food image recognition
- **Google Cloud Translate API** - Translation services

## Key Features

### Core Features
- **User Authentication System**
  - User registration and login
  - Password reset functionality
  - OTP (One-Time Password) verification
  
- **Health Calculators**
  - TDEE (Total Daily Energy Expenditure) calculator
  - BMR (Basal Metabolic Rate) calculator  
  - BMI (Body Mass Index) calculator
  - Calorie tracking and calculation tools

- **Content Management**
  - News and articles section
  - Blog posting and commenting system
  - Search functionality with auto-suggestions

### Advanced Features
- **AI-Powered Food Recognition**
  - Image-based food identification using Google Cloud Vision API
  - Automatic calorie estimation from food images
  
- **Comprehensive Database**
  - Extensive food calorie database
  - Exercise calorie burn calculator
  - Recipe collection with nutritional information

- **Cloud Integration**
  - Scalable database hosting on AWS RDS
  - Secure media storage on AWS S3
  - Production deployment on AWS EC2

## Application Structure

### Main Pages

**Home Page**
- Featured content and latest news
- Quick access to main features

**About Section**
- Project information
- Team details and contact information

**News & Articles**
- Health and fitness articles
- Regional and international health news

**Calorie Management**
- Calorie calculation tools
- Food database with nutritional information
- Activity-based calorie burn calculator
- AI-powered food image recognition

**Weight Loss Section**  
- Weight loss guidance and tips
- Exercise routines and workout plans
- Progress tracking tools

**Recipe Collection**
- Healthy meal recipes
- Vegetarian and dietary-specific options
- Nutritional information for each recipe

**User Account Management**
- Profile management
- Login/logout functionality
- Password recovery system

**Support Center**
- Contact information
- Online messaging system
- FAQ and help documentation

## Installation and Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/WanThinnn/VigorLife-Web-Application.git
   cd VigorLife-Web-Application
   ```

2. **Navigate to the main Django project**
   ```bash
   cd main/VigorWeb
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database setup**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Project Structure

```
main/VigorWeb/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── site1/                 # Main application
│   ├── models.py         # Database models
│   ├── views.py          # Application logic
│   ├── urls.py           # URL routing
│   ├── forms.py          # Django forms
│   ├── templates/        # HTML templates
│   └── static/           # CSS, JS, images
└── VigorWeb/             # Project settings
    ├── settings.py       # Django configuration
    ├── urls.py           # Main URL configuration
    └── wsgi.py           # WSGI configuration
```

## Contributing

This project was developed as an academic assignment. We welcome feedback and suggestions for improvement. Please feel free to submit issues or pull requests.

## Team Members

1. Lại Quan Thiên
2. Lê Minh Quân  
3. Mai Nguyễn Nam Phương
4. Nguyễn Quang Thịnh

## License

This project is developed for educational purposes as part of an academic course assignment.

