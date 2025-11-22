from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task
from .forms import ProjectForm, TaskForm

# PROJECT CRUD

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects':projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = project.tasks.all()
    return render(request, 'projects/project_detail.html', {'project':project, 'tasks': tasks})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form':form})

def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('project_detail', pk=pk)
    return render(request, 'projects/project_form.html', {'form': form})

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/project_delete.html', {'project': project})

# TASK CRUD

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'projects/task_detail.html', {'task':task})

def task_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', pk=project_pk)
    else:
        form = TaskForm()
    return render(request, 'projects/task_form.html', {'form': form, 'project': project})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_detail', pk=pk)
    return render(request, 'projects/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('project_detail', pk=task.project.pk)
    return render(request, 'projects/task_delete.html', {'task': task})