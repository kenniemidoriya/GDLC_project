from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Home/home.html')

def student_list(request):
    return render(request, 'Students/student-list.html')

def dashboard(request):
    return render(request, 'Students/student-dashboard.html')

def settings(request):
    return render(request, 'Student/settings.html')
def student_profile(request):
    return render(request, 'Student/student_profile.html')
