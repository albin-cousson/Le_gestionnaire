from django import forms
from .models import main_idea_model, second_idea_model, third_idea_model

class main_idea_form(forms.ModelForm):
    class Meta:
        model = main_idea_model
        fields = ('idea',)

class second_idea_form(forms.ModelForm):
    class Meta:
        model = second_idea_model
        fields = ('idea','categorie',)

class third_idea_form(forms.ModelForm):
    class Meta:
        model = third_idea_model
        fields = ('idea','categorie',)
