from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Booking
from django.http import JsonResponse, HttpResponseForbidden
from .models import Ambulance

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Ambulance

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    form = AuthenticationForm()  # Initialize the form outside the conditional blocks
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['user_id'] = user.id  # Set user ID in the session
                return redirect('index')
        # If form is invalid, it will continue to the rendering part below
    
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout


#@login_required(login_url='login')
def index(request):
  #return HttpResponse('hi guys')
  return render(request, 'index.html')
  
  

from django.shortcuts import render



def maps(request):
    return render(request, 'maps.html')


@login_required(login_url='login')
def ambulance_registration(request):


    if request.method == 'POST':
        ambulance_number = request.POST.get('ambulance_number')
        telephone_number = request.POST.get('telephone_number')
        driver_name = request.POST.get('driver_name')
        ambulance_location = request.POST.get('ambulance_location')
        
       

        try:
            Ambulance.objects.create(ambulance_number=ambulance_number,telephone_number=telephone_number,ambulance_location=ambulance_location,driver_name=driver_name)
            messages.success(request, 'Ambulance registered successfully!')
        except Exception as e:
            messages.error(request, f'Error: {e}')

    return render(request, 'ambulance_registration.html')

@login_required(login_url='login')
def booking_page(request):

    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        tel_number = request.POST.get('tel_number')
        pickup_location = request.POST.get('pickup_location')
        


        try:
            # Retrieve an available ambulance
            available_ambulance = Ambulance.objects.filter(availability=True).first()

            # Create a booking and assign the available ambulance if found
            new_booking = Booking(patient_name=patient_name, pickup_location=pickup_location)
            if available_ambulance:
                new_booking.ambulance = available_ambulance
                available_ambulance.availability = False  # Assuming the ambulance is no longer available after assignment
                available_ambulance.save()
            new_booking.save()

            return JsonResponse({'success': True})
        except Exception as e:
            # Log the error for debugging purposes
            print(f"Error saving booking: {e}")
            return JsonResponse({'success': False, 'error': str(e)})

    # Handle GET request or rendering the form initially
    # Your GET request logic here
    return render(request, 'booking_page.html')



@login_required(login_url='login')
def booking_history(request):
    # Your logic for retrieving data (booking history)
    # Ensure you fetch the required data to display in the booking_history.html template
    bookings = Booking.objects.all()  # Example: Fetching booking data from a model
    print(bookings)
    return render(request, 'booking_history.html', {'bookings': bookings})
        





@login_required(login_url='login')
def confirmation_page(request):

    # Fetch multiple bookings (for demonstration, you might adjust the logic)
    bookings = Booking.objects.all()  # Retrieve all bookings or apply filtering as needed
    booking_details_list = []

    for booking in bookings:
        booking_details = {
            'Booking ID': booking.id,
            'Patient Name': booking.patient_name,
            'Pickup Location': booking.pickup_location,
            # Add other details as needed
        }
        booking_details_list.append(booking_details)

    return render(request, 'confirmation_page.html', {'booking_details_list': booking_details_list})

