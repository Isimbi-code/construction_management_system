from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'

    def handle_no_permission(self):
        messages.warning(self.request, "You need to be logged in to view this page.")
        return redirect('login')


    def get_queryset(self):
        # Filter projects based on the logged-in user
        return Employee.objects.filter(user=self.request.user)

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'
    context_object_name = 'employee'

class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    template_name = 'employees/employee_form.html'
    fields = ['name', 'position', 'hire_date', 'phone_number', 'emergency_contact', 'emailAddress']
    success_url = reverse_lazy('employee_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the logged-in user to the inventory
        return super().form_valid(form)

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employees/employee_form.html'
    fields = ['name', 'position', 'hire_date', 'phone_number', 'emergency_contact', 'emailAddress']
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')


