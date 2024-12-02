# from django.contrib import admin
# from .models import Project, Task

# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('name', 'start_date', 'end_date', 'budget')
#     list_filter = ('start_date', 'end_date')
#     search_fields = ('name', 'description')
#     date_hierarchy = 'start_date'

# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('name', 'project', 'start_date', 'end_date', 'status')
#     list_filter = ('project', 'status', 'start_date', 'end_date')
#     search_fields = ('name', 'description', 'project__name')
#     date_hierarchy = 'start_date'
