# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .models import Recipe
from .models import Ingredient
from .models import Image

from .forms import KeywordForm
from .forms import RawMaterialForm
from .forms import RecipeForm
from .forms import RecipeDeleteForm
from .forms import IngredientsFormSet
from .forms import ImagesFormSet


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
    if request.method == 'GET':
        recipe_form = RecipeForm(request.GET or None)
        ingredients_form = IngredientsFormSet(queryset=Ingredient.objects.none(), prefix='ingredients_form')
        images_form = ImagesFormSet(queryset=Image.objects.none(), prefix='images_form')
    elif request.method == 'POST':
        recipe_form = RecipeForm(request.POST or None)
        ingredients_form = IngredientsFormSet(request.POST or None, prefix='ingredients_form')
        images_form = ImagesFormSet(request.POST or None, request.FILES or None, prefix='images_form')
        # Formsets are validated per item to allow empty entries
        if recipe_form.is_valid():
            # Save recipe
            recipe = recipe_form.save(commit=False)
            recipe.owner = request.user
            recipe.save()
            recipe_form.save_m2m()
            # Save nested forms: Ingredients
            for ingredient_form in ingredients_form:
                if ingredient_form.is_valid():
                    ingr_name = ingredient_form.cleaned_data.get('name', None)
                    ingr_quantity = ingredient_form.cleaned_data.get('quantity', None)
                    ingr_units = ingredient_form.cleaned_data.get('units', None)
                    if ingr_name is not None and ingr_quantity is not None and ingr_units is not None:
                        ingredient = Ingredient(name=ingr_name,
                                                quantity=ingr_quantity,
                                                units=ingr_units,
                                                recipe=recipe)
                        ingredient.save()
            # Save nested forms: Images
            for image_form in images_form:
                if image_form.is_valid():
                    image_document = image_form.cleaned_data.get('document', None)
                    if image_document is not None:
                        img = Image(document=image_form.cleaned_data['document'], recipe=recipe)
                        img.save()
            # Redirect
            return redirect('recipes_user_list', username=request.user.username)
    else:
        recipe_form = RecipeForm()
        ingredients_form = IngredientsFormSet(queryset=Ingredient.objects.none(), prefix='ingredients_form')
        images_form = ImagesFormSet(queryset=Image.objects.none(), prefix='images_form')
    context = {'message': "Check your form",
               'recipe_form': recipe_form,
               'ingredients_form': ingredients_form,
               'images_form': images_form,
               'create': True}
    return render(request, 'recipes/recipe_create_edit_form.html', context)


@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied

    if request.method == 'GET':
        recipe_form = RecipeForm(instance=recipe)
        ingredients_form = IngredientsFormSet(queryset=recipe.ingredients.all(), prefix='ingredients_form')
        images_form = ImagesFormSet(queryset=recipe.images.all(), prefix='images_form')
    elif request.method == 'POST':
        recipe_form = RecipeForm(request.POST or None, instance=recipe)
        ingredients_form = IngredientsFormSet(request.POST or None,
                                              queryset=recipe.ingredients,
                                              prefix='ingredients_form')
        images_form = ImagesFormSet(request.POST or None,
                                    request.FILES or None,
                                    queryset=recipe.images,
                                    prefix='images_form')
        # Formsets are validated per item to allow empty entries
        if recipe_form.is_valid():
            # Save recipe
            recipe = recipe_form.save(commit=False)
            recipe.owner = request.user
            recipe.save()
            recipe_form.save_m2m()
            # Save nested forms: Ingredients
            for ingredient_form in ingredients_form:
                if ingredient_form.is_valid():
                    ingr_name = ingredient_form.cleaned_data.get('name', None)
                    ingr_quantity = ingredient_form.cleaned_data.get('quantity', None)
                    ingr_units = ingredient_form.cleaned_data.get('units', None)
                    if ingr_name is not None and ingr_quantity is not None and ingr_units is not None:
                        ingredient = Ingredient(name=ingr_name,
                                                quantity=ingr_quantity,
                                                units=ingr_units,
                                                recipe=recipe)
                        ingredient.save()
            # Save nested forms: Images
            for image_form in images_form:
                if image_form.is_valid():
                    image_document = image_form.cleaned_data.get('document', None)
                    if image_document is not None:
                        img = Image(document=image_form.cleaned_data['document'], recipe=recipe)
                        img.save()
            # Redirect
            return redirect('recipes_user_list', username=request.user.username)
    else:
        recipe_form = RecipeForm()
        ingredients_form = IngredientsFormSet(queryset=Ingredient.objects.none(), prefix='ingredients_form')
        images_form = ImagesFormSet(queryset=Image.objects.none(), prefix='images_form')
    context = {'message': "Check your form",
               'recipe_form': recipe_form,
               'ingredients_form': ingredients_form,
               'images_form': images_form,
               'create': False}
    return render(request, 'recipes/recipe_create_edit_form.html', context)


@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied

    if request.method == 'POST':
        form = RecipeDeleteForm(request.POST, instance=recipe)

        if form.is_valid():
            # Delete nested objects: Ingredients
            for ingredient in recipe.ingredients.all():
                ingredient.delete()
            # Delete nested objects: Images
            for image in recipe.images.all():
                image.delete()
            # Delete recipe object
            recipe.delete()
            return redirect('recipes_user_list', username=request.user.username)

    else:
        form = RecipeDeleteForm(instance=recipe)

    template_vars = {'form': form}
    return render(request, 'recipes/recipe_delete_form.html', template_vars)


@login_required
def keyword_create(request):
    if request.method == 'GET':
        keyword_form = KeywordForm(request.GET or None)
    elif request.method == 'POST':
        keyword_form = KeywordForm(request.POST or None)
        if keyword_form.is_valid():
            # Save keyword
            keyword = keyword_form.save(commit=False)
            keyword.save()

            # Redirect
            return redirect('recipes_user_list', username=request.user.username)
    else:
        keyword_form = KeywordForm()
    context = {'message': "Check your form",
               'keyword_form': keyword_form,
               'create': True}
    return render(request, 'recipes/keyword_create_form.html', context)


@login_required
def raw_material_create(request):
    if request.method == 'GET':
        raw_material_form = RawMaterialForm(request.GET or None)
    elif request.method == 'POST':
        raw_material_form = RawMaterialForm(request.POST or None)
        if raw_material_form.is_valid():
            # Save keyword
            raw_material = raw_material_form.save(commit=False)
            raw_material.save()

            # Redirect
            return redirect('recipes_user_list', username=request.user.username)
    else:
        raw_material_form = RawMaterialForm()
    context = {'message': "Check your form",
               'raw_material_form': raw_material_form,
               'create': True}
    return render(request, 'recipes/raw_material_create_form.html', context)
