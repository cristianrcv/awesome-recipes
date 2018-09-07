# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .models import Recipe
from .forms import RecipeForm, RecipeDeleteForm


@login_required
def recipes_list(request):
    recipes = Recipe.public.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/recipes_list.html', context)


@login_required
def recipes_user_list(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        recipes = user.recipes.all()
    else:
        recipes = Recipe.public.filter(owner__username=username)
    context = {'recipes': recipes, 'owner': user}
    return render(request, 'recipes/recipes_user_list.html', context)


@login_required
def recipes_filter(request):
    recipes = Recipe.public.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/recipes_filter.html', context)


@login_required
def recipe_create(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(data=request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.owner = request.user
            recipe.save()
            recipe_form.save_m2m()
            return redirect('recipes_user_list', username=request.user.username)
    else:
        recipe_form = RecipeForm()
    context = {'message': "Check your form", 'recipe_form': recipe_form, 'create': True}
    return render(request, 'recipes/create_edit_form.html', context)


@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        recipe_form = RecipeForm(instance=recipe, data=request.POST)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect('recipes_user_list', username=request.user.username)
    else:
        recipe_form = RecipeForm(instance=recipe)
    context = {'recipe_form': recipe_form, 'create': False}
    return render(request, 'recipes/create_edit_form.html', context)


@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied

    if request.method == 'POST':
        form = RecipeDeleteForm(request.POST, instance=recipe)

        if form.is_valid():
            recipe.delete()
            return redirect('recipes_user_list', username=request.user.username)

    else:
        form = RecipeDeleteForm(instance=recipe)

    template_vars = {'form': form}
    return render(request, 'recipes/delete_form.html', template_vars)
