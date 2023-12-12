# views.py
from django.shortcuts import render, redirect
from .models import Todo,DeletedTask
from .forms import TaskForm,DeleteForm
from django.http import HttpResponse

def home(request):
    task = Todo.objects.all().values()
    deletedtask = DeletedTask.objects.all().values()
    deletedtaskcount = DeletedTask.objects.all().values()
    form = TaskForm(request.POST)
    if request.method == 'POST' and form.is_valid():
       form.save()
    alltask = len(task)
    deltask = len(deletedtaskcount)
    if deletedtask is None:
        print("empty")
    return render(request, 'base.html', {'tasks':task,'form': form,'alltask':alltask,'deltask':deltask,'deletedtask':deletedtask})
def delete(request,pk):
    deletedtask = Todo.objects.get(id=pk)
    deltask = DeletedTask(task=deletedtask.task, description=deletedtask.description)
    deltask.save()
    deletedtask.delete()
    return redirect('/todo/')

def update(request,pk):
    taskId = Todo.objects.get(id=pk)
    form = TaskForm(instance=taskId)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=taskId)
        if form.is_valid():
            form.save()
            return redirect('/todo/')
    context = {
        'form':form
    }
    
    return render(request,'edit.html',context)

def clear(request):
    clearTable = DeletedTask.objects.all()
    clearTable.delete()
    return redirect('/todo/')

def finaldelete(request,pk):
    deltask = DeletedTask.objects.get(id=pk)
    deltask.delete()
    return redirect('/todo/')
