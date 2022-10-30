from django.contrib import admin
from .models import Candidate
# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'gender', 'careen']
    search_fields = ['name', 'phone', 'email']
    list_filter = ['gender', 'careen']
    list_per_page = 10
admin.site.register(Candidate, CandidateAdmin)
