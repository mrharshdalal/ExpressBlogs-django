from django import forms
from django.shortcuts import render, redirect
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image']

def create_blog_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new blog post instance and save it to the database
            new_blog_post = form.save()  # This saves the form data to the database
            return redirect('blog_list')  # Redirect to the blog list view
    else:
        form = BlogPostForm()
    
    return BlogPostForm(request, 'createBlogPost.html', {'form': form})
