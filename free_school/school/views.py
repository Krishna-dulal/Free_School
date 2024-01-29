from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.



def home(request):
    user = request.user
        #print(user)
    if (userIsInGroup(user, 'Student')):
        return studentIndex(request)
    elif (userIsInGroup(user, 'Teacher')):
        return advisorIndex(request)
    else:
        return render(request, 'home.html')


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
