from django.shortcuts import render, redirect
from .models import NullHydFollower, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .MyHTMLSanitizer import MyHTMLSanitizer


@login_required
def index(request):
    context = {}

    return render(request, 'index.html', context)


@login_required
def add_follower(request):

    if "POST" == request.method:
        name = request.POST.get('name', '')
        NullHydFollower.objects.create(follower_name=name)

    followers = NullHydFollower.objects.all()
    context = {"followers": followers}

    return render(request, 'app/add-follower.html', context)


@login_required
def article(request):
    if "POST" == request.method:
        content = request.POST.get('content', '')
        # Sanitize the input data
        content = MyHTMLSanitizer.sanitize(content)

        Comment.objects.create(content=content)

    comments = Comment.objects.all().order_by("-id")
    context = {"comments": comments}

    return render(request, 'app/article.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('/')


