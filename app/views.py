from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.models import Person


def regi(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fname = request.POST.get("fname")
            lname = request.POST.get("lname")
            address = request.POST.get("address")
            email = request.POST.get("email")
            # Check if email already exists
            if Person.objects.filter(email=email).exists():
                messages.warning(request, "E-Mail Already Exists!")
                return redirect("regi")  # Prevent form submission with duplicate email

            # If email is unique, proceed with registration
            new_person = Person(first_name=fname, last_name=lname, address=address, email=email)
            new_person.save()
            messages.success(request, "Registration successful!")
            return redirect("regi")  # Redirect to avoid form resubmission issues

        return render(request, "regi.html")  # Render form if GET request

    else:
        messages.warning(
            request, "You do not have access to the registration page without login."
        )
        return redirect("login")


def logout_view(request):
    logout(request)
    messages.success(request, "User Log-Out Successfully")
    return redirect("login")  # Ensure "login" is a valid URL name


def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        messages.warning(request, "User Not Access home page without login")
    return redirect("login")  # Redirect anonymous users instead of rendering login page


def person_list(request):
    if request.user.is_authenticated:
        persons = Person.objects.all()  # Fetch all persons
        return render(request, "show.html", {"persons": persons})
    else:
        messages.warning(request, "You Not Access View page without login")
        return redirect("login")
    # return render(request,"show.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        password = authenticate(password=password)
        if password:
            pass
        else:
            messages.warning(request, "You enter Invalid login information")

        if user:
            login(request, user)
            # next_url = request.GET.get("next", "home")  # Redirect to 'next' URL or 'home'
            return redirect("home")

    return render(request, "login.html")
