# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Course, Keyword, RawMaterial, Recipe, Ingredient, Image


#
# Model Admins
#

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'elaboration_time', 'elaboration_time_units', 'elaboration', 'is_public')
    list_editable = ('course', 'elaboration_time', 'elaboration_time_units', 'elaboration', 'is_public')
    list_filter = ('course', 'is_public', 'owner__username')
    search_fields = ['title', 'course']
    readonly_fields = ('date_created', 'date_updated')


#
# Registration
#

admin.site.register(Course)
admin.site.register(Keyword)
admin.site.register(RawMaterial)
admin.site.register(Ingredient)
admin.site.register(Image)
admin.site.register(Recipe, RecipeAdmin)
