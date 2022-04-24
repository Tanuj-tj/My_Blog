from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from home.models import Contact
# Inorder to use the alert messages for from validation
from django.contrib import messages
from django.contrib.auth import authenticate , login,logout
from django.contrib.auth.models import User
from blog.models import Post
from blog.forms import PostEditForm
from django.views.generic import CreateView

def home(request):
    posts = Post.objects.order_by("views")[::-1]
    posts = posts[:2]
    context = {
        "posts" : posts
    }
    return render(request,'home/home.html',context)

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
            messages.success(request, "Your message has been successfully send")

    return render(request,'home/contact.html')



def search(request):
    query = request.GET['query']

    if len(query)>100:
        allPosts = Post.objects.none()
    else:
        allPostsCategory = Post.objects.filter(category__icontains=query)
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)

        # Merge two query sets with help of union
        #allPosts = allPostsTitle.union(allPostsContent)
        allPosts = allPostsTitle | allPostsContent | allPostsCategory

    if allPosts.count() == 0:
        messages.warning(request, 'No search result found please refine your query')

    context = {
        'allPosts' : allPosts,
        'query' : query,
    }
    return render(request,"home/search.html",context)



def handleSignup(request):
    if request.method == 'POST':
        
        # Get all the parameters of sigup models from base.html
        
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # If some error from user while creating account
        
        # Username should be under 10 characters
        if len(username) > 10:
            messages.error(request,"Username must be under 10 characters")
            #return redirect('home')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

        # Username should bbe alphanumeric
        if not username.isalnum():
            messages.error(request,"Username should only contain letters and numbers")
            #return redirect('home')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        
        # Password and conform password should match
        if pass1 != pass2:
            messages.error(request,"Passwords do not match")
            #return redirect('home')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


        # Create the user

        myuser = User.objects.create_user(username,email,pass1)

        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account has been successfully created")

    else:
        return HttpResponse('404 - Not Found')

    #return redirect('home')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def handleLogin(request):
    if request.method == 'POST':
        
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername,password = loginpass)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged in as "+str(loginusername))
            #return redirect('home')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


        else:
            messages.error(request,"Invalid Credentials, Please Try again")
            #return redirect('home')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

    return HttpResponse('404 - Not Found')


def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    #return redirect('home')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


class AddNewPost(CreateView):
    model = Post
    template_name = "newBlog.html"
    fields = '__all__'

# def newBlog(request):
#     post = Post
#     form = PostEditForm(instance=post)

#     # if request.method == 'POST':
#     #     form = PostEditForm(request.POST, request.FILES, instance=post)
#     #     form.save()
#     #     return redirect(f"/blog/")

#     context = {
#         'form': form
#         }
#     return render(request, 'blog/newBlog.html', context)
