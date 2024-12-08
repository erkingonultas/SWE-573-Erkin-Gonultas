from django.shortcuts import render, redirect, get_object_or_404
import requests
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from firebase_admin import storage
import uuid
from .models import Comment, Post, Tag
from django.db.models import Q
from .forms import PostSearchForm

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
        tags = request.POST.get('tags', '').split(',')
        color = request.POST['color']
        shape = request.POST['shape']
        material = request.POST['material']
        weight = request.POST['weight']
        # New size fields
        height = request.POST.get('height')
        length = request.POST.get('length')
        depth = request.POST.get('depth')
        size_unit = request.POST.get('size_unit', 'cm')
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
        post = Post.objects.create(
            title=title,
            description=description,
            image_url=image_url,
            color=color,
            shape=shape,
            material=material,
            weight=weight,
            height=int(height) if height else None,
            length=int(length) if length else None,
            depth=int(depth) if depth else None,
            size_unit=size_unit,
            location=location,
            hardness=hardness,
            time_period=time_period,
            smell=smell,
            taste=taste,
            texture=texture,
            value=value, author=request.user,
        )
        # Add tags
        for tag_name in tags:
            tag_name = tag_name.strip()
            if tag_name:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)
        return redirect('post_detail', post_id=post.id)
    
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

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post=post, author=request.user, content=content)
        return redirect('post_detail', post_id=post.id)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post = comment.post

    # Only post owner or admin can delete
    if request.user == post.author or request.user.is_staff:
        comment.delete()
    return redirect('post_detail', post_id=post.id)

@login_required
def mark_as_resolved(request, post_id, comment_id):
    post = get_object_or_404(Post, id=post_id)
    comment = get_object_or_404(Comment, id=comment_id, post=post)

    # Only the post owner can mark as resolved
    if request.user == post.author:
        post.is_resolved = True
        post.resolved_comment = comment
        post.save()
    return redirect('post_detail', post_id=post.id)

def search_wikidata(request):
    query = request.GET.get('query', '')
    if not query:
        return JsonResponse({'results': []})

    url = "https://www.wikidata.org/w/api.php"
    params = {
        'action': 'wbsearchentities',
        'format': 'json',
        'language': 'en',
        'search': query
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        results = [{'id': item['id'], 'label': item.get('label', ''), 'description': item.get('description', '')} for item in data.get('search', [])]
        return JsonResponse({'results': results})
    else:
        return JsonResponse({'results': []})
    
def search_posts(request):
    form = PostSearchForm(request.GET or None)
    results = None

    if form.is_valid():
        query = Q()

        # Filter by title and description
        if form.cleaned_data['title']:
            query &= Q(title__icontains=form.cleaned_data['title'])
        if form.cleaned_data['description']:
            query &= Q(description__icontains=form.cleaned_data['description'])

        # Filter by size
        if form.cleaned_data['height']:
            query &= Q(height__gte=form.cleaned_data['height'])
        if form.cleaned_data['length']:
            query &= Q(length__gte=form.cleaned_data['length'])
        if form.cleaned_data['depth']:
            query &= Q(depth__gte=form.cleaned_data['depth'])
        if form.cleaned_data['size_unit']:
            query &= Q(size_unit=form.cleaned_data['size_unit'])

        # Filter by dropdown fields
        for field in ['color', 'shape', 'material', 'weight', 'hardness', 'time_period', 
                      'smell', 'taste', 'texture', 'value', 'location']:
            if form.cleaned_data[field]:
                query &= Q(**{f"{field}": form.cleaned_data[field]})

        results = Post.objects.filter(query).distinct()

    return render(request, 'components/search_results.html', {'form': form, 'results': results})