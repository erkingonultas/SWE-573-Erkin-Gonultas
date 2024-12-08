from django import forms
from .models import Post

class PostSearchForm(forms.Form):
    title = forms.CharField(required=False, label="Title", widget=forms.TextInput(attrs={'placeholder': 'Search by title'}))
    description = forms.CharField(required=False, label="Description", widget=forms.TextInput(attrs={'placeholder': 'Search by description'}))
    
    # Size
    height = forms.IntegerField(required=False, min_value=0, label="Minimum Height")
    length = forms.IntegerField(required=False, min_value=0, label="Minimum Length")
    depth = forms.IntegerField(required=False, min_value=0, label="Minimum Depth")
    size_unit = forms.ChoiceField(required=False, choices=Post.SIZE_UNITS, label="Size Unit")
    
    # Dropdown fields
    color = forms.ChoiceField(required=False, choices=[('', 'Any')] + Post.COLOR_CHOICES, label="Color")
    shape = forms.ChoiceField(required=False, choices=[('', 'Any')] + Post.SHAPE_CHOICES, label="Shape")
    material = forms.ChoiceField(required=False, choices=[('', 'Any')] + Post.MATERIAL_CHOICES, label="Material")
    weight = forms.ChoiceField(required=False, choices=[('', 'Any')] + Post.WEIGHT_CHOICES, label="Weight")
    hardness = forms.ChoiceField(required=False, choices=[('', 'Any')] + Post.HARDNESS_CHOICES, label="Hardness")
    time_period = forms.ChoiceField(required=False, choices=[('', 'Any')] + Post.TIME_PERIOD_CHOICES, label="Time Period")
    smell = forms.ChoiceField(required=False, choices=[('', 'Any')] + Post.SMELL_CHOICES, label="Smell")
    taste = forms.ChoiceField(required=False, choices=[('', 'Any')] + Post.TASTE_CHOICES, label="Taste")
    texture = forms.ChoiceField(required=False, choices=[('', 'Any')] + Post.TEXTURE_CHOICES, label="Texture")
    value = forms.ChoiceField(required=False, choices=[('', 'Any')] + Post.VALUE_CHOICES, label="Value")
    location = forms.ChoiceField(required=False, choices=[('', 'Any')] + Post.LOCATION_CHOICES, label="Location")
