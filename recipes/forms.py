from django.forms import ModelForm

from .models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        exclude = ('date_created', 'date_updated', 'owner')
