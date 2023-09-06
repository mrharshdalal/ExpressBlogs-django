from django import forms
from django.shortcuts import render, redirect
from .models import BlogPost, Hashtag

class BlogPostForm(forms.ModelForm):
    hashtags = forms.CharField(
        max_length=100,  # Adjust the max length as needed
        required=False,  # Make the field optional
        help_text="Enter hashtags separated by commas (e.g., #travel, #food)",
    )
    
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image', 'hashtags']

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Extract and process hashtags
        hashtag_names = [word.strip() for word in self.cleaned_data.get('hashtags', '').split(',') if word.strip()]
        instance.save()

        # Associate hashtags with the blog post
        for hashtag_name in hashtag_names:
            hashtag, created = Hashtag.objects.get_or_create(name=hashtag_name)
            instance.hashtags.add(hashtag)

        if commit:
            instance.save()

        return instance

def create_blog_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new blog post instance and save it to the database
            new_blog_post = form.save()

            # Extract and associate hashtags with the blog post
            hashtag_names = [word.strip() for word in form.cleaned_data.get('hashtags', '').split(',') if word.strip()]
            for hashtag_name in hashtag_names:
                hashtag, created = Hashtag.objects.get_or_create(name=hashtag_name)
                new_blog_post.hashtags.add(hashtag)

            return redirect('blog_list')  # Redirect to the blog list view
    else:
        form = BlogPostForm()
    
    return render(request, 'createBlogPost.html', {'form': form})
