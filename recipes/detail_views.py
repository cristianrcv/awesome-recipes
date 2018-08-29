# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.views.generic.detail import DetailView

from .models import Recipe


class RecipeDetailView(DetailView):
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
