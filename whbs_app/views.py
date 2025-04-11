from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Home page view
@login_required(login_url='login')  # User must be logged in to view this page
def home(request):
    halls = Hall.objects.all()  # Fetch all halls from the database
    return render(request, 'whbs/index.html', {'halls': halls})  # Render the 'index.html' template with the halls data

# View for displaying all halls
@login_required(login_url='login')  
def halls(request):
    halls = Hall.objects.all()  # Fetch all halls
    return render(request, 'whbs/halls.html', {'halls': halls})  # Render the 'halls.html' template with the halls data

# Profile view for logged-in users
@login_required(login_url='login')  # User must be logged in to view this page
def proFile(request):
    uname = request.user  # Get the logged-in user's username
    print(uname)
    users = user_register.objects.get(name=uname)  # Fetch user details from user_register model
    return render(request, 'whbs/profile.html', {'users': users})  # Render profile page with user data

# View for displaying user's bookings
@login_required(login_url='login')  
def mybookings_view(request):
    return render(request, 'whbs/my_bookings.html')  # Render the 'my_bookings.html' template

# About page view
@login_required(login_url='login')  
def about(request):
    return render(request, 'whbs/about.html')  # Render the 'about.html' template

# Contact form view (POST request for submitting a message)
@login_required(login_url='login')  
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')  # Get name from POST data
        PhoNo = request.POST.get('PhoNo')  # Get phone number
        email = request.POST.get('email')  # Get email
        msg = request.POST.get('massage')  # Get message
        
        # Create a new message object and save it to the database
        newuser = Msg.objects.create(
            name=name,
            PhoNo=PhoNo,
            email=email,
            msge=msg,
        )
        newuser.save()  # Save the new message

    return render(request, 'whbs/contact.html')  # Render the contact page

# Login view for users
def loginn(request):
    if request.method == "POST":
        name = request.POST.get('name')  # Get username from POST data
        password = request.POST.get('password')  # Get password
        
        # Authenticate the user using the provided username and password
        userr = authenticate(request, username=name, password=password)
        if userr is not None:  # If authentication is successful
            login(request, userr)  # Log the user in
            return redirect('/')  # Redirect to home page
        else:
            messages.info(request, 'Invalid Username and password !.')
            return redirect('login')  # Redirect back to login page if authentication fails

    return render(request, 'whbs/login.html')  # Render the login page

# User registration view
def register(request):
    if request.method == "POST":
        # Get form data for registration
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        address = request.POST.get('address')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        gender = request.POST.get('gender')

        # Check if both passwords match
        if password == password2:
            # Create a new user_register entry and save it to the database
            newUser = user_register.objects.create(
                name=name,
                email=email,
                number=number,
                address=address,
                password=password,
                gender=gender,
            )
            newUser.save()  # Save the new user
        

            # Create a new User object in Django's User model
            newUser = User.objects.create_user(username=name, email=email, password=password)
            newUser.save()  # Save the new Django User

            return redirect('login')  # Redirect to the login page after successful registration
        else:
            messages.info(request, 'Password Not Matched !.')
    return render(request, 'whbs/register.html')  # Render the registration page

# Logout view to log the user out
def signout(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to the login page

# Booking a hall view (only accessible to logged-in users)
@login_required(login_url='login')  
def book_hall(request, hall_id):
    hall = get_object_or_404(Hall, id=hall_id)  # Fetch hall based on hall_id, or return 404 if not found
    if request.method == 'POST':
        guest_count = request.POST.get('guest_count')  # Get the number of guests
        address = request.POST.get('address')  # Get the address for the booking
        date = request.POST.get('date')  # Get the booking date

        # Create a new booking for the logged-in user and save it to the database
        Booking.objects.create(user=request.user, hall=hall, guest_count=guest_count, address=address, booking_date=date)
        return redirect('my_bookings')  # Redirect to the 'my_bookings' page

    return render(request, 'whbs/book_hall.html', {'hall': hall})  # Render the booking page for the selected hall

# View for displaying user's bookings
@login_required(login_url='login')  
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)  # Get all bookings made by the logged-in user
    return render(request, 'whbs/my_bookings.html', {'bookings': bookings})  # Render the 'my_bookings.html' page with bookings data

# Delete a booking view (only accessible to logged-in users)
@login_required(login_url='login')  
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)  # Fetch the booking if it belongs to the logged-in user
    booking.delete()  # Delete the booking
    return redirect('my_bookings')  # Redirect to the 'my_bookings' page

# Edit booking view (only accessible to logged-in users)
@login_required(login_url='login')  
def edit_booking(request, id):
    if request.method == 'POST':
        guest_count = request.POST.get('guest_count')  # Get updated guest count
        address = request.POST.get('address')  # Get updated address
        date = request.POST.get('date')  # Get updated date

        # Fetch the booking and update its fields
        obj = Booking.objects.get(id=id)
        obj.guest_count = guest_count
        obj.address = address
        obj.date = date
        obj.save()  # Save the changes to the booking
        return redirect('my_bookings')  # Redirect to the 'my_bookings' page

    obj = Booking.objects.get(id=id)  # Fetch the booking details to display in the form
    return render(request, 'whbs/edit_booking.html', {'obj': obj})  # Render the 'edit_booking.html' template with booking details
