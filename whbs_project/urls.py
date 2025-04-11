from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from whbs_app.views import *  # Import all views from whbs_app

# URL patterns list that maps URLs to views
urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),  # Admin page for managing the site

    # Home page URL
    path('', home, name='home'),  # Display available halls, home page view

    # Halls page URL
    path('halls/', halls, name='halls'),  # Display list of all halls

    # User profile page URL
    path('profile/', proFile, name='profile'),  # Display logged-in user's profile

    # My bookings page URL
    path('mybookings/', mybookings_view, name='mybookings_view'),  # Placeholder for user's booking details

    # About page URL
    path('about/', about, name='about'),  # Display about information page

    # Contact page URL
    path('contact/', contact, name='contact'),  # Contact form for submitting inquiries or messages

    # Login page URL
    path('login/', loginn, name='login'),  # Login page for users to authenticate

    # Registration page URL
    path('register/', register, name='register'),  # User registration page

    # Logout URL
    path('signout/', signout, name='logout'),  # Log out the current user

    # Book hall URL (requires hall ID as a parameter)
    path('book/<int:hall_id>/', book_hall, name='book_hall'),  # Allow user to book a hall by ID

    # My bookings page URL
    path('my_bookings/', my_bookings, name='my_bookings'),  # Display the list of user's bookings

    # Edit booking URL (requires booking ID as a parameter)
    path('edit_booking/<int:id>/', edit_booking, name='edit_booking'),  # Edit an existing booking by ID

    # Delete booking URL (requires booking ID as a parameter)
    path('delete_booking/<int:booking_id>/', delete_booking, name='delete_booking'),  # Delete a booking by ID
]

# Serve media files in development mode (for uploaded images or files)
# MEDIA_URL is used for the URL to access media files, MEDIA_ROOT is the file system location where media files are stored
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
