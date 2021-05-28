from django.shortcuts import render, HttpResponse

def blogHome(request):
    return HttpResponse("This is Blog home")


def blogPost(request,slug):
    return HttpResponse(f"This is Blog Post {slug}")

