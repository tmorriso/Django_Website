from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html',{'content':['To see how SMB can help your company, Email us at:','tmorriso1990@gmail.com']})
