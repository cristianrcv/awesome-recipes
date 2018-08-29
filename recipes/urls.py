# -*- coding: utf-8 -*-

from django.conf.urls import url

from django.contrib.auth.views import login
from recipes.detail_views import RecipeDetailView
from recipes.views import recipes_list, recipes_user_list, recipes_filter
from recipes.views import recipe_create, recipe_edit, recipe_delete

urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', recipes_user_list, name='recipes_user_list'),
    url(r'^recipes_list/$', recipes_list, name='recipes_list'),
    url(r'^recipes_filter/$', recipes_filter, name='recipes_filter'),

    url(r'^recipe_view/(?P<pk>\d+)$', RecipeDetailView.as_view(), name='recipe_detail'),
    url(r'^recipe_create/$', recipe_create, name='recipe_create'),
    url(r'^recipe_edit/(?P<pk>\d+)/$', recipe_edit, name='recipe_edit'),
    url(r'^recipe_delete/(?P<pk>\d+)/$', recipe_delete, name='recipe_delete'),

    url(r'^$', login, {'template_name': 'login.html'}, name='awesome_recipes_login'),
]
