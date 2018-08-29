# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

from django_measurement.models import MeasurementField
from measurement.measures import Time, Volume


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


# Ingredient
@python_2_unicode_compatible
class Ingredient(models.Model):
    name = models.ForeignKey(RawMaterial, verbose_name='material', related_name='used_in')

    quantity = MeasurementField(
        name="quantity",
        measurement=Volume,
        unit_choices=(('cubic_centimeter', 'cm3'), ('cubic_decimeter', 'dm3'),
                      ('l', 'l'),
                      ('imperial_g', 'g'),
                      ('imperial_tbsp', 'tbspoon'), ('imperial_tsp', 'teaspoon')),
        default=0
    )

    def __str__(self):
        # Returns the name of the raw material
        return self.name.name

    class Meta:
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'
        ordering = ['name']


# Recipe
@python_2_unicode_compatible
class Recipe(models.Model):
    title = models.CharField('title', max_length=255)
    course = models.ForeignKey(Course, verbose_name='course', related_name='recipes')
    keywords = models.ManyToManyField(Keyword, blank=True)

    elaboration_time = MeasurementField(name='elaboration_time',
                                        measurement=Time,
                                        unit_choices=(('hr', 'h'), ('min', 'min')),
                                        default=0)
    elaboration = models.TextField('elaboration', blank=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True)

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
