# Lesson 40 - 12.03.23 Adding Registered User to student model & POSTING user ID to students & GETTING data per user AND Live Render

# this project includes:
    - CRUDS using class (django rest framework APIView)
    - Register & loggin
    - connecting registered user id to students model (adjustments in Serializer.py, models.py, views.py: GET (getting only data the user posted) and POST)
    - 3 html pages:
        1. loggin
        2. register
        * Access token is saved to localStorage
        ** if log in is successful then Access token will be saved to localStorage and then we can go to display students
        3. display students - if Access Token from local storage is okay, students will display


# live back-end server: https://lesson40-addingregistereduser.onrender.com/
# netlify front-end:    https://lesson40-django-class-authentication.netlify.app