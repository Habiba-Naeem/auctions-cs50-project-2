from django.forms import ModelForm
from .models import *
from django import forms

class ListingForm(ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Listing 
        exclude = ['owner', 'created_at', 'status']
        
class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['bid']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
