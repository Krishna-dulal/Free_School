from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.
from .models import UserProfile

def your_google_login_callback_view(request):
    user = request.user
    UserProfile.objects.get_or_create(user=user)
    # rest of your view logic




def home(request):
    user = request.user
    context = {}  # Initialize an empty context dictionary

    if userIsInGroup(user, 'Student'):
        context['role'] = 'Student'
        return studentIndex(request)
    elif userIsInGroup(user, 'Teacher'):
        context['role'] = 'Teacher'
        return advisorIndex(request)
    else:
        return render(request, 'home.html', context)


def logout_view(request):
    logout(request)
    return redirect("/")

def userIsInGroup(user, groupName):
    return user.groups.filter(name=groupName).exists()

def school(request, id):
    # Load the appropriate template based on user's group
    if userIsInGroup(request.user, 'Student'):
        template = loader.get_template('student.html')
    elif userIsInGroup(request.user, 'Teacher'):
        template = loader.get_template('teacher.html')
    else:
        # Redirect or show an error if the user is neither a student nor a teacher
        return redirect('/')
