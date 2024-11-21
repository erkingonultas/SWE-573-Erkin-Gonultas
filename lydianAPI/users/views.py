from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from firebase_admin import storage
import uuid
from .models import Post

def index(request):
    posts = Post.objects.order_by('-id')  # Order by newest posts
    return render(request, 'forum/index.html', {'posts': posts, 'user': request.user})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'forum/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'forum/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        color = request.POST['color']
        shape = request.POST['shape']
        material = request.POST['material']
        weight = request.POST['weight']
        location = request.POST['location']
        hardness = request.POST['hardness']
        time_period = request.POST['time_period']
        smell = request.POST['smell']
        taste = request.POST['taste']
        texture = request.POST['texture']
        value = request.POST['value']
        image = request.FILES.get('image')
        image_url = None

        # Upload image to Firebase Storage if it exists
        if image:
            # Generate a unique filename for the image
            image_name = f"{uuid.uuid4()}.jpg"
            bucket = storage.bucket()
            blob = bucket.blob(image_name)
            blob.upload_from_file(image.file, content_type=image.content_type)
            # Make the image publicly accessible and get the URL
            blob.make_public()
            image_url = blob.public_url

        # Create the post with the Firebase image URL
        Post.objects.create(
            title=title,
            description=description,
            image_url=image_url,
            color=color,
            shape=shape,
            material=material,
            weight=weight,
            location=location,
            hardness=hardness,
            time_period=time_period,
            smell=smell,
            taste=taste,
            texture=texture,
            value=value, author=request.user,
        )
        return redirect('index')
    
    return render(request, 'forum/create_post.html')

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Check if the user is the post's author or an admin
    if request.user == post.author or request.user.is_staff:
        if request.method == 'POST':
            post.delete()
            return redirect('index')
    else:
        return HttpResponseForbidden("You do not have permission to delete this post.")

    return render(request, 'components/delete_post.html', {'post': post})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'components/post_detail.html', {'post': post})
