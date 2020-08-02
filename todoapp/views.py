from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Task
from .forms import TaskAddForm


# Create your views here.
def index(request):
    task_list = Task.objects.all().order_by('task_deadline', 'task_text')
    context = {'task_list': task_list}
    return render(request, 'todoapp/index.html', context)


def add_task(request):
    if request.method == 'POST':
        form = TaskAddForm(request.POST)
        if form.is_valid():
            task = Task()
            task.task_text = form.cleaned_data.get('task_text')
            task.add_time = form.cleaned_data.get('add_time')
            task.task_deadline = form.cleaned_data.get('task_deadline')
            task.save()
            return HttpResponseRedirect(reverse('todoapp:index'))
    else:
        form = TaskAddForm()
        context = {'form': form}
        return render(request, 'todoapp/addtask.html', context)
