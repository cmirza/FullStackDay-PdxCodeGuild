from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .models import BlogPost, Comment
import datetime


# function to get index page
def index(request):
    return render(request, 'blog/index.html')


# function to get login page
def login_page(request):
    return render(request, 'blog/login.html')


# function to login user, gets username and password from the page, makes an authentication request, if user is none
# returns login page with error message, otherwise returns profile page
def login_user(request):

    user_name = request.POST['user_name']
    user_pass = request.POST['user_pass']

    user = authenticate(request, username=user_name, password=user_pass)

    if user is None:
        return render(request, 'blog/login.html', {'message': 'Invalid username or password.'})
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('blog:profile'))


# function to return registration page
def register(request):
    return render(request, 'blog/register.html')


# function to register user, gets username, email and password, if username exists, returns registration page with an
# error, otherwise creates a new user object, adds user to commenter group, saves, returns profile page with
# welcome message
def reg_user(request):

    user_name = request.POST['user_name']
    user_email = request.POST['user_email']
    user_pass = request.POST['user_pass']

    if User.objects.filter(username=user_name).exists():
        return render(request, 'blog/register.html', {'message': 'Username Already Exists.'})
    else:
        user = User.objects.create_user(username=user_name, email=user_email, password=user_pass)
        group = Group.objects.get(name='commenter')
        user.groups.add(group)
        user.save()

        login(request, user)

        context = {'user_message': 'Welcome to Blog.'}

    return render(request, 'blog/profile.html', context)


# function to return profile page, gets date and time of user's last login and renders as a message
@login_required
def profile(request):

    last_login = request.user.last_login
    context = {'user_message': 'Your last login was ', 'last_login': last_login}

    return render(request, 'blog/profile.html', context)


# function to logout user, returns login page with message that user has been logged out
@login_required
def logout_user(request):
    logout(request)
    return render(request, 'blog/login.html', {'message': 'You have been logged out.'})


# function to get list of available blog posts. requests all blog posts from model and passes them to be
# rendered in template
@login_required
def post_list(request):

    posts = BlogPost.objects.all()
    context = {'posts': posts}

    return render(request, 'blog/post_list.html', context)


# function to view blog post, gets id of post from url, requests post from model, requests comments from model,
# passes both to template to be rendered
@login_required
def post_detail(request, url_key):

    post = BlogPost.objects.get(id=url_key)

    comments = Comment.objects.filter(post=url_key)

    context = {'post': post, 'comments': comments}

    return render(request, 'blog/post_detail.html', context)


# function to post comment on blog post, gets comment from page, creates comment object and saves,
# redirects to same post
@login_required
def comment(request, url_key):

    page_comment = request.POST['comment']

    url_item = Comment(body=page_comment, post=BlogPost.objects.get(id=url_key), user=request.user, timestamp=datetime.datetime.now())
    url_item.save()

    return HttpResponseRedirect(reverse('blog:post_detail', args=url_key))


# function for blog composition, checks if user has permissions, if they do, render composition page, if not
# forward to profile page with error message
def post_compose(request):

    if request.user.has_perm('blog.poster'):
        return render(request, 'blog/post_compose.html')
    else:
        context = {'user_message': 'You don\'t have permission to post.'}

        return render(request, 'blog/profile.html', context)


# function to post new blog article, gets title and body of post from page, creates new blogpost object and saves,
# then redirects to post list
@permission_required('blog.poster')
def post_blog(request):

    post_title = request.POST['post_title']
    post_body = request.POST['post_body']

    blog_article = BlogPost(user=request.user, title=post_title, body=post_body, timestamp=datetime.datetime.now())
    blog_article.save()

    return HttpResponseRedirect(reverse('blog:post_list'))
