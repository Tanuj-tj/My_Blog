from django.shortcuts import render, HttpResponse
from .models import Contact
# Inorder to use the alert messages for from validation
from django.contrib import messages
from blog.models import Post

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



def search(request):
    query = request.GET['query']

    if len(query)>100:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)

        # Merge two query sets with help of union
        allPosts = allPostsTitle.union(allPostsContent)

    if allPosts.count() == 0:
        messages.warning(request, 'No search result found please refine your query')

    context = {
        'allPosts' : allPosts,
        'query' : query,
    }
    return render(request,"home/search.html",context)
    
