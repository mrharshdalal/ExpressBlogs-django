from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from .createBlog import BlogPostForm
from .models import BlogPost, Hashtag, Like
from django.db.models import Q, Count



# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("base")
    trending_blogs = BlogPost.objects.order_by('-likes')[:3]

    context = {
        'trending_blogs': trending_blogs,
    }
    return render(request, 'base.html', context)

def home(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("")
    else:
        trending_blogs = BlogPost.objects.order_by('-likes')[:3]

        # Prepare the context with trending_blogs
        context = {
            'trending_blogs': trending_blogs,
        }
        return render(request, 'home.html', context)

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
    trending_blogs = BlogPost.objects.order_by('-likes')[:3]

    context = {
        'blog_posts': blog_posts,
        'trending_blogs': trending_blogs,
    }
    
    return render(request, 'blog_list.html', context)

def search_results(request):
    query = request.GET.get('query', '')
    print(query)
   
    # Search for blog posts that match the query in title or hashtags
    blog_posts = BlogPost.objects.filter(
        Q(title__icontains=query) | Q(hashtags__name__icontains=query)
    )
    
    context = {
        'query': query,
        'blog_posts': blog_posts,
    }
    
    return render(request, 'search_results.html', context)

def like_blog_post(request, blog_post_id):
    if request.user.is_authenticated:
        blog_post = get_object_or_404(BlogPost, pk=blog_post_id)

        # Check if the user has already liked the post
        existing_like, created = Like.objects.get_or_create(
            user=request.user,
            blog_post=blog_post
        )

        # If the like is created (i.e., user hasn't liked the post before), increment the likes count
        if created:
            blog_post.likes += 1
            blog_post.save()

    return redirect('blog_list')  

def blog_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', {'blog_post': blog_post})

def trending_blogs(request):
    # Retrieve trending blogs by ordering by likes in descending order
    trending_blogs = BlogPost.objects.order_by('-likes')[:3]

    context = {
        'trending_blogs': trending_blogs,
    }

    return render(request, 'base.html', context)

