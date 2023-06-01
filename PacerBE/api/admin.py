from django.contrib import admin
from api.models import Scores


# Register your models here.
class AdminScores(admin.ModelAdmin):
    list_display = ['id', 'userId', 'score'] #'is_adult'
    list_editable = ['userId', 'score']
    search_fields = ['userId']
    list_filter = ['score'] #'is_adult'

admin.site.register(Scores, AdminScores)
