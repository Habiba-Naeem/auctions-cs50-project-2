from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.category}"


class Listing(models.Model):
    title =  models.CharField(max_length = 100)
    picture = models.ImageField(upload_to = 'pic/%Y/%m/%d')
    detail = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    category = models.OneToOneField(Category, on_delete=models.DO_NOTHING)
    startingbid = models.FloatField(default=0)
    status = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.title},{self.created_at} {self.detail}, {self.owner}, {self.category}, {self.startingbid}, {self.picture}, {self.status}"

class Bid(models.Model):
    bid = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.bid}"

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment}, {self.user}, {self.listing}"


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}, {self.listing}"
    
class Winner(models.Model):
    winner = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.winner}, {self.listing}"
    