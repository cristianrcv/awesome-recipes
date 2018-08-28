# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .models import Recipe
from .forms import RecipeForm


def recipes_list(request):
    recipes = Recipe.public.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/recipes_list.html', context)


def recipes_user_list(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        recipes = user.recipes.all()
    else:
        recipes = Recipe.public.filter(owner__username=username)
    context = {'recipes': recipes, 'owner': user}
    return render(request, 'recipes/recipes_user_list.html', context)


@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(data=request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.owner = request.user
            recipe.save()
            form.save_m2m()
            return redirect('recipes_user_list', username=request.user.username)
    else:
        form = RecipeForm()
    context = {'form': form, 'create': True}
    return render(request, 'recipes/form.html', context)


@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = RecipeForm(instance=recipe, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes_user_list', username=request.user.username)
    else:
        form = RecipeForm(instance=recipe)
    context = {'form': form, 'create': False}
    return render(request, 'recipes/form.html', context)
