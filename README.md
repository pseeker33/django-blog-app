# Django Blog App

This project is a blog application built with Django. Users can create, view, and manage blog entries. The application includes authentication and session management features for registered users.

## Features

- Welcome page with registration and login options.  
- User registration and login functionality.  
- Pages to create, view, and list blog entries.  
- Authenticated users can create new blog entries.  
- Sidebar displaying authenticated user information on the home page.  
- Redirection after login, registration, and logout.  

## Technologies Used

- **Python 3.x**  
- **Django 4.x**  
- **Bootstrap 4** for responsive design.  
- **SQLite** as the default database for development.  

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your_user/django_blog_app.git
    ```

2. Navigate to the project folder:

    ```bash
    cd django_blog_app
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On **Windows**:
        ```bash
        venv\Scripts\activate
        ```

    - On **macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser to access the Django admin panel:

    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:

    ```bash
    python manage.py runserver
    ```

9. Open your browser and visit `http://127.0.0.1:8000/` to see the application in action.

## Project Structure



## Main Routes

- **Welcome Page**: `/users/welcome/`  
- **Blog Home Page**: `/blog/`  
- **Registration Page**: `/users/register/`  
- **Login Page**: `/users/login/`  
- **Create Blog Entry Page**: `/blog/create_entry/`  

## Contribution

If you want to contribute to this project, please follow these steps:

1. Fork the repository.  
2. Create a new branch (`git checkout -b feature/new-feature`).  
3. Make the necessary changes and commit your modifications (`git commit -am 'Add new feature'`).  
4. Push your changes to your forked repository (`git push origin feature/new-feature`).  
5. Create a pull request in this repository.  

## License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.