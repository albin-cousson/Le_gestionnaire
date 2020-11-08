from django.contrib import admin
from .models import main_idea_model, second_idea_model, third_idea_model, programme_model

class main_idea_admin(admin.ModelAdmin):
    list_display = ('idea',)
    date_hierarchy = 'date'
    search_fields = ('idea',)

admin.site.register(main_idea_model, main_idea_admin)
admin.site.register(second_idea_model)
admin.site.register(third_idea_model)
admin.site.register(programme_model)
