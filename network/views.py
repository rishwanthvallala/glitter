from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect , JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator



from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.contrib.auth import get_user_model
from django.http import HttpResponse


from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import Http404



from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.contrib.auth import get_user_model
from django.http import HttpResponse


from .models import User, Post, follow_status
import json




def index(request):
    posts = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    message = ""
    fuser = None
    if request.user.is_authenticated:
        fuser = follow_status.objects.get(user=request.user)

    return render(request, "network/index.html", {
        "posts": posts,
        "page_obj": page_obj,
        "message": message,
        "fuser": fuser
    })

def activate(request, uidb64, token):  
    User = get_user_model()  
    print("user is")
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
        fuser = follow_status.objects.get(user_id=user.id)
        fuser.is_verified = True
        fuser.save()
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        print("user is", fuser.is_verified)
        return HttpResponse('Thank you for your email confirmation. Your account has been verified. Please refresh the home page to see the changes.')  
    else:  
        return HttpResponse('Activation link is invalid!') 

def verify(request, username):
    user = User.objects.get(username=username)
    user.verified = True
    email = user.email
    user.save()
    
    # for post
    fuser = follow_status.objects.get(user_id=user.id)
    if fuser.is_verified:
        return HttpResponseRedirect(reverse("index"))
    posts = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print("fuser is", fuser.is_verified)
    try:
        current_site = get_current_site(request)
        mail_subject = 'Activate your blog account.'
        message = render_to_string('network/acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
            'token':account_activation_token.make_token(user),  
        })
        to_email = email
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()
    
    except Exception as e:
        print(e)
        return HttpResponse("Error sending email")
    message= "Email sent has been sent to your email address. Please check your email and click on the link to verify your account."
    return render(request, "network/index.html", {
        "message": message,
        "posts": posts,
        "page_obj": page_obj,
        "fuser": fuser  
    })




def profile(request, username):

    user = User.objects.get(username=username)
    posts = Post.objects.filter(user=user).order_by("-timestamp")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #Display the number of followers the user has, as well as the number of people that the user follows.
    profile = follow_status.objects.get(user=user)
    followers = profile.followers.count()
    following = profile.following.count()
    curuser = request.user
    followingstatus = False
    if curuser.is_authenticated:    
        followingstatus = follow_status.objects.filter(user=curuser, following=user).exists()
    print("followingstatus is", followingstatus)
    return render(request, "network/profile.html", {
        "posts": posts,
        "page_obj": page_obj,
        "curuser": user,
        "followers": followers,
        "following": following,
        "followingstatus": followingstatus
    })


def edit(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        content = json.loads(request.body)["content"]
        post.content = content
        post.save()
        response_data = {
            "content": content
        }
        return JsonResponse(response_data, status=200) 




def following(request):
    print("following")
    user = request.user
    following = follow_status.objects.get(user=user).following.all()

    posts = Post.objects.filter(user__in=following).order_by("-timestamp")
    print("posts are", posts)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/following.html", {
        "posts": posts,
        "page_obj": page_obj
    })

def like(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        user = request.user
        if user in post.likers.all():
            post.likers.remove(user)
            post.likes -= 1
            post.save()
            response_data = {
                "likes": post.likes,
                "liked": False
            }
            return JsonResponse(response_data, status=200)
        else:
            post.likers.add(user)
            post.likes += 1
            post.save()
            response_data = {
                "likes": post.likes,
                "liked": True
            }
            return JsonResponse(response_data, status=200)

def newpost(request):
    if request.method == "POST":
        print("newpost")    
        content = request.POST["content"]
        if content == "":
            return HttpResponseRedirect(reverse("index"))
        user = request.user
        post = Post(user=user, content=content)
        post.save()
        return HttpResponseRedirect(reverse("index"))
   


def follow(request, username):
    user = User.objects.get(username=username)
    currentuser = request.user
    try:
        currentuser= follow_status.objects.get(user=currentuser)
    except:
        follow = follow_status(user=currentuser)
        follow.save()
        currentuser= follow_status.objects.get(user=currentuser)
    currentuser.following.add(user)
    currentuser.save()
    user = follow_status.objects.get(user=user)
    currentuser = request.user
    user.followers.add(currentuser)
    user.save()
    return HttpResponseRedirect(reverse("profile", args=(username,)))

def unfollow(request, username):
    user = User.objects.get(username=username)
    currentuser = request.user
    currentuser= follow_status.objects.get(user=currentuser)
    currentuser.following.remove(user)
    currentuser.save()
    user = follow_status.objects.get(user=user)
    currentuser = request.user
    user.followers.remove(currentuser)
    user.save()
    return HttpResponseRedirect(reverse("profile", args=(username,)))


def login_view(request):
    if request.method == "POST":

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
            user1 = follow_status(user=user, is_verified=False)
            user1.save()


        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
