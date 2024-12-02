from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

    def handle_no_permission(self):
        messages.warning(self.request, "You need to be logged in to view this page.")
        return redirect('login') 


    def get_queryset(self):
        # Filter projects based on the logged-in user
        return Project.objects.filter(user=self.request.user)

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'projects/project_form.html'
    fields = ['name', 'description', 'start_date', 'end_date', 'budget']
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project_form.html'
    fields = ['name', 'description', 'start_date', 'end_date', 'budget']
    success_url = reverse_lazy('project_list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')



