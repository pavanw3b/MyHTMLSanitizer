from django.shortcuts import render, redirect
from .models import NullHydFollower, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from mysecurityutils.myhtmlsanitizer import MyHTMLSanitizer


# View for homepage
@login_required  # Check if the user is logged in. Redirects to login_url per the settings.py if unauthenticated
def index(request):
    context = {}

    return render(request, 'index.html', context)


# View for Add Follow Page
# Also handles new follower submission
@login_required
def add_follower(request):

    if "POST" == request.method:  # If a new follower is submitted
        name = request.POST.get('name', '')
        NullHydFollower.objects.create(follower_name=name)  # db insert

    # Return list of followers for GET or after POST
    followers = NullHydFollower.objects.all()
    context = {"followers": followers}

    response = render(request, 'app/add-follower.html', context)
    response['X-XSS-Protection'] = 0  # # Disable browser XSS protection for the session.
    return response                   # # Don't disable XSS in an actual SDLC!


# View for Blog Article page.
# Also handles comment submitted on the article
@login_required
def article(request):
    submitted = False
    has_error = False
    content = ""

    if "POST" == request.method:
        submitted = True
        content = request.POST.get('content', '')
        # Sanitize the input data
        sanitizer = MyHTMLSanitizer()
        content = sanitizer.sanitize(content)

        # Check if the content all malicious & sanitize returned blank. Alert user if so.
        if 0 == len(content):
            content = request.POST.get('content', '')
            has_error = True
        # If the content has at least one acceptable char
        else:
            Comment.objects.create(content=content)  # Insert into db
            content = ""

    # Return the list of comments on GET request or after the POST
    comments = Comment.objects.all().order_by("-id")
    context = {
        "comments": comments,
        "submitted": submitted,
        "has_error": has_error,
        "content": content
    }

    response = render(request, 'app/article.html', context)
    response['X-XSS-Protection'] = 0  # Disable browser XSS protection for the session.
    return response                   # Don't disable XSS in a actual SDLC!


# Handles logout. Uses django's default logout
@login_required
def logout_user(request):
    logout(request)
    return redirect('/')


