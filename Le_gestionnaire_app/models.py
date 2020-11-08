from django.db import models
from django.utils import timezone

class main_idea_model(models.Model):
    idea = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.idea

class second_idea_model(models.Model):
    idea = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now) 
    categorie = models.ForeignKey('main_idea_model', null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.idea

class third_idea_model(models.Model):
    idea = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    categorie = models.ForeignKey('second_idea_model', null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.idea

class programme_model(models.Model):
    idea = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    categorie = models.ForeignKey('second_idea_model', null=True, on_delete=models.CASCADE)
    main_categorie =  models.ForeignKey('main_idea_model', null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.idea
    class Meta:
        ordering=['date']
