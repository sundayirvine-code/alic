from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from capstone.settings import EMAIL_HOST_USER
from django.http import JsonResponse
import json
from urllib.parse import urlparse, parse_qs
from django.views.decorators.csrf import csrf_exempt
from googleapiclient.discovery import build


# Create your views here.
def posts(request):
    obj= Afrobeat.objects.all()
    return render(request, "alic/posts.html", {
        'obj':obj
    })

def hangout(request):
    obj= Hangout.objects.all()
    return render(request, "alic/posts.html", {
        'obj':obj
    })

def dancehall(request):
    obj= Dancehall.objects.all()
    return render(request, "alic/posts.html", {
        'obj':obj
    })

def hiphop(request):
    obj= Hiphop.objects.all()
    return render(request, "alic/posts.html", {
        'obj':obj
    })

def amapiano(request):
    obj= Amapiano.objects.all()
    return render(request, "alic/posts.html", {
        'obj':obj
    })

def reels(request):
    obj= Reels.objects.all()
    return render(request, "alic/posts.html", {
        'obj':obj
    })

def nuggets(request):
    obj= Nuggets.objects.all()
    return render(request, "alic/posts.html", {
        'obj':obj
    })

def image(request):
    images= Image.objects.all()
    return render(request, "alic/posts.html", {
        'images':images
    })



@csrf_exempt
def link(request):
    apikey='AIzaSyDuIe-bAwV6tmureptFckh7wEof65SR_Ck'
    youtube=build('youtube', 'v3', developerKey=apikey)
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # GET THE URL PARAMETER
    data = json.loads(request.body)
    url = data.get("body")
    query = urlparse(url)
    if query.hostname in {'www.youtube.com', 'youtube.com'}:
        if query.path == '/watch':
            #print(parse_qs(query.query)['v'][0])
            request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=parse_qs(query.query)['v'][0]
            )
            response=request.execute()
            print(response["items"][0]['statistics']['viewCount'])
            return JsonResponse({"message": "Post Edited successfully.",
            "ID":ID,
            "body":p

            }, status=201)
        if query.path[:7] == '/watch/':
            #print(query.path.split('/')[1])
            request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=query.path.split('/')[1]
            )
            response=request.execute()
            stats=response["items"][0]['statistics']
            return JsonResponse({
            'stats':stats

            }, status=201)
        if query.path[:7] == '/embed/':
            #print(query.path.split('/')[2])
            request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=query.path.split('/')[2]
            )
            response=request.execute()
            #print(response["items"][0]['statistics'])
            stats=response["items"][0]['statistics']
            return JsonResponse({
            'stats':stats

            }, status=201)
        if query.path[:3] == '/v/':
            print(query.path.split('/')[2])
            request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=query.path.split('/')[2]
            )
            response=request.execute()
            stats=response["items"][0]['statistics']
            return JsonResponse({
            'stats':stats

            }, status=201)
        # below is optional for playlists
        if query.path[:9] == '/playlist':
            print(parse_qs(query.query)['list'][0])
            request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=parse_qs(query.query)['list'][0]
            )
            response=request.execute()
            stats=response["items"][0]['statistics']
            return JsonResponse({
            'stats':stats

            }, status=201)


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["pasw"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "alic/login.html", {
                "message": "Invalid username and/or password."
            })

    return render(request, "alic/login.html")

#@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"].capitalize()
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "alic/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "alic/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "alic/register.html")

def about(request):
    return render(request, "alic/about-us-details.html")


def index(request):
    return render(request,"alic/index.html")

# Send email to admin
def message(request):
    if request.method == "POST":
        send_to = 'sunvineirday@gmail.com'
        subject = request.POST['subject']
        message = request.POST['message']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        from_email = request.POST['from_email']
        message=message+ f" \n\n Email from: {from_email} \n First Name: {firstname} \n Last Name: {lastname}"
        send_mail(subject, message, EMAIL_HOST_USER, [send_to ], fail_silently = False)

        return HttpResponseRedirect(reverse("index"))

    else:
        return render("You cant do this")
