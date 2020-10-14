from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    try:
        listing = Listing.objects.all()
        print(listing)
    except Listing.DoesNotExists:#error
        return render(request, "auctions/index.html")
    
    context = {
        "listing" :listing
    }
    return render(request, "auctions/index.html", context)


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required(login_url='login')
def listing(request):
    if request.method == "POST":
        listingform = ListingForm(request.POST, request.FILES)
        
        if listingform.is_valid():
            listing = listingform.save(commit=False)
            
            listing.owner = request.user
            listing.save()

    listingform = ListingForm()
    context = {"listingform": listingform}
    return render(request, "auctions/listing.html", context)

def view_list(request, id):
    listing = Listing.objects.get(id=id)
    bidform = BidForm()
    print(listing)

    if request.user.is_authenticated:
        try:
            watchlist = Watchlist.objects.get(user = request.user, listing = listing)
        except ObjectDoesNotExist:
            watchlist = None
    watchlist = None
    try:
        bids = Bid.objects.filter(listing=listing).count()
    except:
        bids = 0
    context = {
        "list": listing,
        "bidform": bidform,
        "watchlist": watchlist,
        "bids": bids
    }
    return render(request, "auctions/list.html", context)

@login_required(login_url='login')
def addwatchlist(request, id):
    listing = Listing.objects.get(id=id)
    Watchlist.objects.create(user=request.user, listing=listing)
    return HttpResponseRedirect(reverse('list', args=(id,)))

@login_required(login_url='login')
def remove(request, id):
    listing = Listing.objects.get(id=id)
    watch = Watchlist.objects.get(user=request.user, listing=listing)
    watch.delete()
    return HttpResponseRedirect(reverse('list', args=(id,)))

@login_required(login_url='login')
def bid(request, id):
    if request.method == "POST":
        bidform = BidForm(request.POST)
        listing = Listing.objects.get(id=id)
        print(listing)
        bids = Bid.objects.filter(user=request.user, listing=listing)

        if bidform.is_valid():
            bid = bidform.save(commit=False)
            largest = 0
            try:
                for i in bids:
                    if largest < i.bid:
                        largest = i.bid
            except:
                pass
            if bid.bid > largest and bid.bid > listing.startingbid:
                bid.user = request.user
                bid.listing = listing
                bid.save()
                return HttpResponseRedirect(reverse('list', args=(id,))) 
            else:
                messages.warning(request, "Please place larger bid") 

    return HttpResponseRedirect(reverse('list', args=(id,)))    
