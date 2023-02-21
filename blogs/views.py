from django.shortcuts import render

# Create your views here.
def blogs(request):
    return render(request, 'blogs.html')

def blog_details(request, slug):
    return render(request, 'blog_details.html')