from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def planner(request):
    todolist = Todo.objects.all()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('planner')
    else:
        form = TodoForm()
    return render(request, 'planner.html', {'form': form, 'todolist': todolist})

def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todolist = Todo.objects.exclude(id=todo.id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('planner')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todo_edit.html', {'form': form, 'todolist': todolist})

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('planner')

