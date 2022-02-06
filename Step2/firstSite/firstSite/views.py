from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def list_course(request):
    course = ['Python', 'HTML', 'CSS', 'JavaScript', 'Java', 'Kotlin', 'Android']
    count_list = len(course)
    return render(request,'course.html', {'course': course, 'total': count_list})