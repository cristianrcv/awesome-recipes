# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now


#
# MANAGERS
#

# Manager for public recipes
class PublicRecipesManager(models.Manager):

    def get_queryset(self):
        qs = super(PublicRecipesManager, self).get_queryset()
        return qs.filter(is_public=True)


#
# MODELS
#

# Course: starter, main, dessert, etc.
@python_2_unicode_compatible
class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        ordering = ['name']


# Keyword: soup, meat, fish, etc.
@python_2_unicode_compatible
class Keyword(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'keyword'
        verbose_name_plural = 'keywords'
        ordering = ['name']


# RawMaterial
@python_2_unicode_compatible
class RawMaterial(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'raw material'
        verbose_name_plural = 'raw materials'
        ordering = ['name']


# Recipe
@python_2_unicode_compatible
class Recipe(models.Model):
    HOUR = 'h'
    MINUTE = 'min'

    UNITS = (
        (HOUR, 'hour'),
        (MINUTE, 'minute')
    )

    title = models.CharField('title', max_length=100, unique=True)
    course = models.ForeignKey(Course, verbose_name='course', related_name='recipes')
    keywords = models.ManyToManyField(Keyword, blank=True)

    elaboration_time = models.PositiveSmallIntegerField()
    elaboration_time_units = models.CharField(max_length=10, choices=UNITS, default='1')
    elaboration = models.TextField('elaboration', blank=True)
    # ingredients = models.ManyToManyField(Ingredient, blank=True)

    owner = models.ForeignKey(User, verbose_name='owner', related_name='recipes')
    is_public = models.BooleanField('public', default=True)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')

    objects = models.Manager()
    public = PublicRecipesManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Recipe, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'
        ordering = ['title']


# Ingredient
@python_2_unicode_compatible
class Ingredient(models.Model):
    UNIT = 'u'
    GRAM = 'g'
    KILOGRAM = 'kg'
    LITER = 'l'
    DECILITER = 'dl'
    MILLILITER = 'ml'
    CUBIC_CM = 'cm3'
    CUBIC_DM = 'dm3'
    TABLESPOON = 'tbsp'
    TEASPOON = 'tsp'

    UNITS = (
        (UNIT, 'unit'),
        (GRAM, 'gram'),
        (KILOGRAM, 'kilogram'),
        (LITER, 'liter'),
        (DECILITER, 'dl'),
        (MILLILITER, 'ml'),
        (CUBIC_CM, 'cm3'),
        (CUBIC_DM, 'dm3'),
        (TABLESPOON, 'tablespoon'),
        (TEASPOON, 'teaspoon'),
    )

    name = models.ForeignKey(RawMaterial, verbose_name='material', related_name='used_in')
    quantity = models.PositiveSmallIntegerField()
    units = models.CharField(max_length=15, choices=UNITS, default='1')
    recipe = models.ForeignKey(Recipe, verbose_name='used_in', related_name='ingredients', null=True)

    def __str__(self):
        # Returns the name of the raw material
        return self.name.name

    class Meta:
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'
        ordering = ['name']


def user_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.recipe.owner.id, filename)


# Image
@python_2_unicode_compatible
class Image(models.Model):
    document = models.ImageField(upload_to=user_directory_path)

    uploaded_at = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipe, verbose_name='used_in', related_name='images', null=True)

    def __str__(self):
        return self.recipe.title + "_image"

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
