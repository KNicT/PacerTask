from django.contrib import admin
from api.models import Scores


# Register your models here.
class AdminScores(admin.ModelAdmin):
    list_display = ['id', 'userId', 'score']
    list_editable = ['userId', 'score']
    search_fields = ['userId']
    list_filter = ['score']

admin.site.register(Scores, AdminScores)