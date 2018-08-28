# -*- coding: utf-8 -*-

from django.conf.urls import url

from recipes.views import recipes_list, recipes_user_list
from recipes.views import recipe_create, recipe_edit

urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', recipes_user_list, name='recipes_user_list'),
    url(r'^recipe_create/$', recipe_create, name='recipe_create'),
    url(r'^recipe_edit/(?P<pk>\d+)/$', recipe_edit, name='recipe_edit'),
    url(r'^$', recipes_list, name='recipes_list'),
]
