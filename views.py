from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from network.forms import PostForm

from .models import Follower, User, Post, UserFollowing


def index(request):

    if request.method == "POST":
        if request.POST.get('content'):
            post_form = PostForm(request.POST)
            print(post_form)
            if post_form.is_valid():
                new_post = post_form.save(commit=False)
                new_post.author = request.user
                new_post.save()
                print(f'Saved {new_post, new_post.author}')

    return render(request, "network/index.html", {
        "posts": Post.objects.all().order_by('-date_created')
    })

def user_profile(request, username):
    current_user = request.user
    user = User.objects.get(username=username)
    print(user, current_user)
    try:
        UserFollowing.objects.get(user_id=current_user, following_user_id=user)
        following_is_true = True
    except:
        following_is_true = False
    user_following = len(user.following.all())
    user_followers = len(user.followers.all())
    print(user_followers)
    context = {
       "user": user,
       "following_is_true":following_is_true,
       'user_followers':user_followers,
       'user_following':user_following
    }

    return render(request, 'user_profile.html', context)

def followers_count(request):
    if request.method == "POST":
        print('POST')
        value = request.POST['value']
        user = request.POST['user']
        follower = request.POST['follower']
        print('user = ', user)
        main_user = User.objects.get(username=request.POST['user'])
        follower_user = User.objects.get(username=request.POST['follower'])
        if value == 'follow':
            UserFollowing.objects.create(user_id=main_user,
                             following_user_id=follower_user)
        else: 
            UserFollowing.objects.filter(user_id=main_user,
                             following_user_id=follower_user).delete()
            # follower_cnt = Follower.objects.create(follower=follower, user=user)
            # print(follower_cnt, follower, user)
            # follower_cnt.save()
        return redirect('/profile/'+follower)

def following_page(request):
    # print(UserFollowing.objects.filter(user_id=request.user))
    user_id_array = []
    all_posts = None
    following_users = UserFollowing.objects.filter(user_id=request.user).values('following_user_id')
    print(following_users)
    for user in following_users:
        user_id = user.get('following_user_id')
        user_id_array.append(user_id)
        users = User.objects.get(id=user_id)
        # print(user_id_array)
        all_posts = Post.objects.filter(author__in=user_id_array)
        print(all_posts)

    # print(UserFollowing.objects.values_list('following_user_id', user_id=request.user))
    # print(User.objects.get(id=2))

    all_following = request.user.following.all()
    user_followers = request.user.followers.all()
    # print(all_following, user_followers)
    # print(all_following)
    # for follower in all_following:
    #     print(follower)
    return render(request, "network/following_page.html", {
        "followers_posts":all_posts.order_by('-date_created')
    })

def login_view(request):
    if request.method == "POST":
        if request.POST.get('amount'):
            print('jaja')

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
