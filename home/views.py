from django.shortcuts import render, HttpResponse
from .models import Contact
# Inorder to use the alert messages for from validation
from django.contrib import messages

def home(request):
    return render(request,'home/home.html')

def about(request):
    messages.success(request, 'This is about page')
    return render(request,'home/about.html')

def contact(request):
    if request.method == 'POST':
        # Fetch the details from contact form (using name=" ")
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        if len(name)<2 or len(email)<3 or len(message)<4:
            messages.error(request, 'Please Fill the form correctly')
        else:
            contact = Contact(name=name,email=email,message=message)
            contact.save()
            messages.success(request, ": Your message has been successfully send")

    return render(request,'home/contact.html')
    
