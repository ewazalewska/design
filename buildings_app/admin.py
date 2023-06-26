from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['symbol', 'type', 'date_of_the_order', 'investor_last_name']
    list_filter = ('type', 'walls', 'ceiling', 'roof', 'elevation')
    search_fields = ['symbol', 'investor_last_name']
