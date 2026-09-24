from django.shortcuts import render 

def home(request): 
    """ 
    Renders the home page of the application. 
    """ 
    return render(request, "home.html")

def index(request): 
    """ 
    Renders the index page of the application. 
    """ 
    return render(request, "index.html")

def about(request): 
    """ 
    Renders the about page of the application. 
    """ 
    return render(request, "about.html")

def contact(request): 
    """ 
    Renders the contact page of the application. 
    """ 
    return render(request, "contact.html")

def main(request):
    """
    Renders the main page of the application.
    """
    return render(request, "main.html")

def fruit_student_view(request): 
    """ 
    Renders a page showing an unordered list of fruits 
    and an ordered list of students selected for an event. 
    """ 

    context = { 
    "fruits": ["Apple", "Banana", "Mango", "Pineapple", "Grapes"], 
    "selected_students": [ 
    "Aarav Mehta", 
    "Diya Kapoor", 
    "Kabir Singh", 
    "Meera Nair", 
    "Rohan Iyer", 
    ], 
    "event_name": "Annual Sports Day 2026", 
    } 

    return render(request, "fruits_students.html", context) 