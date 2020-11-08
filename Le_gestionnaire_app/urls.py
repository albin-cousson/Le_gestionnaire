from django.urls import path
from . import views

urlpatterns = [
   path("", views.main_idea_view, name="getionnaire"),
   path("delete/<int:id>", views.main_ideaDelete_view, name="getionnaireDelete"),
   path("edit/<int:id>", views.main_ideaEdit_view, name="getionnaireEdit"),
   path("edit_sous_idee/<int:id>", views.second_ideaEdit_view, name="getionnaireEditSousIdee"),
   path("delete_sous_idee/<int:id>", views.second_ideaDelete_view, name="getionnaireDeleteSousIdee"),
   path("delete_sous_sous_idee/<int:id>", views.third_ideaDelete_view, name="getionnaireDeleteSousSousIdee"),
   path("programme/<int:id>", views.programme_view, name="programme_url"),
   path("programme_delete/<int:id>", views.programmeDelete_view, name="programmeDelete_url"),
   path("programme_second/<int:id>", views.second_programme_view, name="second_programme_url"),
   path("programme_second_delete/<int:id>", views.second_programmeDelete_view, name="second_programme_delete_url")
]

