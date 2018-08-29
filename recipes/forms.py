from django.forms import ModelForm

from .models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        exclude = ('date_created', 'date_updated', 'owner')


class RecipeDeleteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecipeDeleteForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['title'].widget.attrs['readonly'] = True

    def clean_title(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            return instance.title
        else:
            return self.cleaned_data['title']

    class Meta:
        model = Recipe
        fields = ['title']
