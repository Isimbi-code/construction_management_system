# from django.http import JsonResponse
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from .models import Item, Employee, Project
# import json

# @login_required
# def dashboard_view(request):
#     # Get the counts
#     item_count = Item.objects.filter(user=request.user).count()
#     employee_count = Employee.objects.filter(user=request.user).count()
#     project_count = Project.objects.filter(user=request.user).count()

#     # Prepare data for the chart
#     chart_data = {
#         'labels': ['Items', 'Employees', 'Projects'],
#         'data': [item_count, employee_count, project_count],
#     }

#     return render(request, 'dashboard/dashboard.html', {
#         'item_count': item_count,
#         'employee_count': employee_count,
#         'project_count': project_count,
#         'chart_data': json.dumps(chart_data),  # Pass serialized data
#     })

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from invetory.models import Item
from employees.models import Employee
from projects.models import Project
import json

@login_required
def dashboard_view(request):
    # Fetch data related to the current user
    items = Item.objects.filter(user=request.user)
    employees = Employee.objects.filter(user=request.user)
    projects = Project.objects.filter(user=request.user)

    # Get the counts
    item_count = items.count()
    employee_count = employees.count()
    project_count = projects.count()

    # Prepare data for the chart
    chart_data = {
        'labels': ['Inventory Items', 'Employees', 'Projects'],
        'data': [item_count, employee_count, project_count],
    }

    # Prepare context data
    context = {
        'item_count': item_count,
        'employee_count': employee_count,
        'project_count': project_count,
        'chart_data': json.dumps(chart_data),
        'recent_items': items[:5],
        'recent_employees': employees.order_by('-hire_date')[:5],
        'recent_projects': projects.order_by('-start_date')[:5],
    }

    return render(request, 'dashboard/dashboard.html', context)



