from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser

# Doctor: Create new blog post
@login_required
def create_blog_post(request):
    if request.user.user_type != 'doctor':
        return redirect('patient_dashboard')  # or some access-denied page

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.doctor = request.user
            blog.save()
            return redirect('blog:my_blogs')
    else:
        form = BlogPostForm()

    return render(request, 'blog/create_blog.html', {'form': form})

# Doctor: View own blog posts
@login_required
def my_blogs(request):
    if request.user.user_type != 'doctor':
        return redirect('patient_dashboard')
    
    blogs = BlogPost.objects.filter(doctor=request.user).order_by('-created_at')
    return render(request, 'blog/my_blogs.html', {'blogs': blogs})

# Patient: View published posts category-wise
@login_required
def all_blogs(request):
    if request.user.user_type != 'patient':
        return redirect('doctor_dashboard')

    categories = {}
    for post in BlogPost.objects.filter(is_draft=False).order_by('-created_at'):
        if post.category not in categories:
            categories[post.category] = []
        categories[post.category].append(post)

    return render(request, 'blog/all_blogs.html', {'categories': categories})
