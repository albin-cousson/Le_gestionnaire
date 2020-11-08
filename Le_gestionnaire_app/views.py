from django.shortcuts import render, redirect
from django.urls import reverse
from . import urls
from django.http import HttpResponseRedirect
from .models import main_idea_model, second_idea_model, third_idea_model, programme_model
from .forms import main_idea_form, second_idea_form, third_idea_form

def main_idea_view(request):
    main_ideas = main_idea_model.objects.all()
    programmes = programme_model.objects.all()
    main_form = main_idea_form(request.POST)
    if main_form.is_valid():
        main_form.save()
    return render (request, 'Le_gestionnaire_app/Le_gestionnaire_main.html', {'main_ideas':main_ideas, 'main_form':main_form, 'programmes':programmes})

def main_ideaEdit_view(request, id):
    main_ideas = main_idea_model.objects.all()
    main_idea = main_idea_model.objects.get(id=id)
    second_ideas = second_idea_model.objects.filter(categorie__idea=main_idea.idea)
    second_form = second_idea_form(request.POST) 
    if second_form.is_valid():
        second_form.save()
    return render (request, 'Le_gestionnaire_app/Le_gestionnaire_second.html', {'main_ideas':main_ideas, 'main_idea':main_idea, 'second_ideas':second_ideas, 'second_form':second_form})
def main_ideaDelete_view(request, id):
    main_ideas = main_idea_model.objects.all()
    programmes = programme_model.objects.all()
    main_form = main_idea_form(request.POST)
    if main_form.is_valid():
        main_form.save()
    main_ideaDelete = main_idea_model.objects.get(id=id)
    main_ideaDelete.delete()
    return render (request, 'Le_gestionnaire_app/Le_gestionnaire_main.html', {'main_ideas':main_ideas, 'main_form':main_form, 'programmes':programmes})

def second_ideaEdit_view(request, id):
    main_ideas = main_idea_model.objects.all()
    second_ideas = second_idea_model.objects.all()
    second_idea = second_idea_model.objects.get(id=id)
    second = second_idea_model.objects.filter(id=id) 
    third_ideas = third_idea_model.objects.filter(categorie__idea=second_idea.idea)
    third_form = third_idea_form(request.POST)
    if third_form.is_valid():
        third_form.save()       
    return render (request, 'Le_gestionnaire_app/Le_gestionnaire_third.html', {'main_ideas':main_ideas, 'second_ideas':second_ideas, 'second':second, 'third_ideas':third_ideas, 'third_form':third_form})
def second_ideaDelete_view(request, id):
    main_ideas = main_idea_model.objects.all()
    second_ideas = second_idea_model.objects.all()
    second_ideaDelete = second_idea_model.objects.get(id=id)
    second_ideaDelete.delete()
    second = second_idea_model.objects.filter(categorie=second_ideaDelete.categorie)
    main_idea = main_idea_model.objects.get(idea=second_ideaDelete.categorie)
    second_form = second_idea_form(request.POST)    
    if second_form.is_valid():
        second_form.save()
    try:
        programme = programme_model.objects.get(id=id)
        programme.delete()
    finally:
        return render(request, 'Le_gestionnaire_app/Le_gestionnaire_second.html', {'main_ideas':main_ideas, 'main_idea':main_idea, 'second_ideas':second_ideas, 'second':second, 'second_form':second_form})

def third_ideaDelete_view(request, id):
    third_ideaDelete = third_idea_model.objects.get(id=id)
    third_ideaDelete.delete()
    try:
        programme = programme_model.objects.get(id=id)
        programme.delete()
    finally:
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def second_programme_view(request, id):
    main_ideas = main_idea_model.objects.all()    
    second_form = second_idea_form(request.POST)
    if second_form.is_valid():
        second_form.save()
    second_idea = second_idea_model.objects.get(id=id)
    programme = programme_model(idea=second_idea.idea, main_categorie=second_idea.categorie, id=second_idea.id)
    programme.save()
    second_ideas = second_idea_model.objects.filter(categorie=second_idea.categorie)
    main_idea = main_idea_model.objects.get(idea=second_idea.categorie)
    return render(request, 'Le_gestionnaire_app/Le_gestionnaire_second.html', {'main_ideas':main_ideas, 'main_idea':main_idea, 'second_ideas':second_ideas, 'second_form':second_form})
def second_programmeDelete_view(request, id):
    second_ideas = second_idea_model.objects.get(id=id)
    second_ideas.delete()
    programme = programme_model.objects.get(id=id)
    programme.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER")) 

def programme_view(request, id):
    third_ideas = third_idea_model.objects.get(id=id)
    programme = programme_model(idea=third_ideas.idea, categorie=third_ideas.categorie, id=third_ideas.id)
    programme.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
def programmeDelete_view(request, id):
    try: 
        third_idea = third_idea_model.objects.get(id=id)
        third_idea.delete()
    finally:
        programme = programme_model.objects.get(id=id)
        programme.delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

