from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Task
from .forms import TaskAddForm


# Create your views here.
def index(request):
    # change is yet to make
    pk = request.user.id
    user = User.objects.get(pk=pk)
    task_list = Task.objects.filter(user=user).order_by('task_deadline', 'task_text')
    context = {'task_list': task_list}
    return render(request, 'todoapp/index.html', context)


def add_task(request):
    if not request.user.is_authenticated:
        HttpResponseRedirect(reverse('accounts:login'))
    if request.method == 'POST':
        form = TaskAddForm(request.POST)

        if form.is_valid():
            task = Task()
            task.task_text = form.cleaned_data.get('task_text')
            task.add_time = form.cleaned_data.get('add_time')
            task.task_deadline = form.cleaned_data.get('task_deadline')
            task.user = request.user
            task.save()
            return HttpResponseRedirect(reverse('todoapp:index'))
        return render(request, 'todoapp/addtask.html', {'form': form})
    else:
        form = TaskAddForm()
        context = {'form': form}
        return render(request, 'todoapp/addtask.html', context)


def remove_task(request, task_id):
    Task.objects.get(pk=task_id).delete()
    return HttpResponseRedirect(reverse('todoapp:index'))
