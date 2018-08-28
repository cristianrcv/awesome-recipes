# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Course, Keyword, RawMaterial, Recipe, Ingredient


#
# Model Admins
#

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'owner', 'is_public', 'date_updated')
    list_editable = ('course', 'is_public',)
    list_filter = ('course', 'is_public', 'owner__username')
    search_fields = ['title']
    readonly_fields = ('date_created', 'date_updated')


#
# Registration
#

admin.site.register(Course)
admin.site.register(Keyword)
admin.site.register(RawMaterial)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
