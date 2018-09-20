# -*- coding: utf-8 -*-

from django_filters import FilterSet
from django_filters import CharFilter
from django_filters import ModelMultipleChoiceFilter

from django import forms

from .models import Recipe
from .models import Course
from .models import Keyword
from .models import Ingredient


class RecipesFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')
    owner = CharFilter(lookup_expr='icontains')
    course = ModelMultipleChoiceFilter(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple)
    keywords = ModelMultipleChoiceFilter(queryset=Keyword.objects.all(), widget=forms.CheckboxSelectMultiple)
    ingredients = ModelMultipleChoiceFilter(queryset=Ingredient.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Recipe
        fields = ['title', 'owner', 'course', 'keywords', 'ingredients']
