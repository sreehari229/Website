from django.shortcuts import render
from django.http import HttpResponse
from .models import Education

def index(request):
    education_details = Education.objects.all().values()
    data = {
        "name" : "Sreehari S",

        "about" : "Hello! I am Sreehari S. Currently pursuing Masters in Computer Science. Strongly motivated individual with Bachelor's degree in Computer Applications. Interested in exploring fields like ML/AI. Offering effective coding skills and working experience with multiple projects.",

        "about_section" : {
            'age' : '22',
            'email' : "sreehari229@gmail.com",
            'phone' : "+91 - 8971 422 625",
            'address' : "Bangalore, India",
        },

        "professional_skills_left" : {
            "Python" : 90,
            "C#" : 85,
            "Java" : 85,
            "Microsoft Sql Server" : 70,
        },

        "professional_skills_right" : {
            "Flask / Django" : 70,
            "ASP.net MVB" : 85,
            "MySQL" : 80,
            "Git\Github" : 90,
        },

        "education" : education_details,
              
    }

    return render(request, 'CurVitae/education.html', data)