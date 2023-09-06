from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from .createBlog import BlogPostForm
from .models import BlogPost, Hashtag
from django.db.models import Q
from django.db import connection



# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("base")
    return render(request, 'base.html')

def home(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("")
    else:
        return render(request, 'home.html')

def loginUser(request):
    if request.method=="POST":

        # check for correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            print("authenticate success")
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            print("authenticate failed")
            return render(request, 'login.html')


    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("login")


def create_blog_post(request):
    print("hello i am here")

    if request.method == 'POST':
        # Handle form submission
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')  # Redirect to the list of blog posts after submission
    else:
        # Display the empty form
        form = BlogPostForm()

    return render(request, 'createBlogPost.html', {'form': form})

def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'blog_posts': blog_posts})

def search_results(request):
    query = request.GET.get('query', '')
    print(query)
    # connection.queries = []
    # print(connection.queries)

    # Search for blog posts that match the query in title or hashtags
    blog_posts = BlogPost.objects.filter(
        Q(title__icontains=query) | Q(hashtags__name__icontains=query)
    )
    
    context = {
        'query': query,
        'blog_posts': blog_posts,
    }
    
    return render(request, 'search_results.html', context)