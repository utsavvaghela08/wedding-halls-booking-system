from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Model representing a Hall available for booking
class Hall(models.Model):
    title = models.CharField(max_length=200)  # Title of the hall
    description = models.TextField()  # Description of the hall
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the hall for booking
    image = models.ImageField(upload_to='halls/')  # Image of the hall
    services = models.CharField(max_length=200)  # Services available at the hall
    date = models.DateTimeField(default=timezone.now)  # Date when the hall was added

    def __str__(self):
        return self.title  # Return the title of the hall when the object is printed


# Model for User Registration (custom user model)
class user_register(models.Model):
    RESPONSE_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    # Fields for user details
    name = models.CharField(max_length=50, unique=True)  # User's name
    email = models.EmailField(unique=True)  # User's email
    number = models.IntegerField()  # User's phone number
    password = models.CharField(max_length=50)  # User's password (this should be hashed in production)
    gender = models.CharField(max_length=10, choices=RESPONSE_CHOICES)  # Gender of the user
    address = models.TextField(null=True)  # User's address (can be left empty)
    date = models.DateTimeField(default=timezone.now)  # Date when the user registered

    def __str__(self):
        return self.name  # Return the user's name when the object is printed


# Model representing a booking made by a user for a hall
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to the User who made the booking
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)  # Reference to the Hall being booked
    guest_count = models.IntegerField()  # Number of guests for the booking
    address = models.TextField()  # Address for the booking (where the event is taking place)
    booking_date = models.DateTimeField(auto_now_add=False)  # The date when the booking is made

    def __str__(self):
        return f"Booking by {self.user.username} for {self.hall.title}"  # Display a message with user and hall info


# Model for storing messages from users (contact form or inquiries)
class Msg(models.Model):
    name = models.CharField(max_length=100)  # Name of the person sending the message
    PhoNo = models.CharField(max_length=10, null=True)  # Phone number (can be left empty)
    email = models.EmailField()  # Email address of the person
    msge = models.TextField(null=True)  # The message content (can be left empty)

    def __str__(self):
        return self.name  # Display the sender's name when the object is printed
