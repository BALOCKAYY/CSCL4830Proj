from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.core.exceptions import ValidationError
import re
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.http import JsonResponse
from django.utils.timezone import now

def index(request):
    upcoming_todos = Todo.objects.filter(due__gte=now().date()).order_by("due")[:2]
    return render(request, 'index.html', {"upcoming_todos": upcoming_todos})

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

@csrf_exempt
def delete_todo(request, todo_id):
     if request.method == "POST":
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()
        return JsonResponse({"status": "success"})  # ✅ Return JSON response instead of redirecting
     return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)

def validate_due_date(date_str):
    """Validate and convert date from MM/DD/YYYY to a proper format."""
    pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/\d{4}$'
    
    if not re.match(pattern, date_str):
        raise ValidationError("Invalid date format. Use MM/DD/YYYY.")

    # Convert input to Python date object
    return datetime.strptime(date_str, "%m/%d/%Y").date()


def search_todo(request):
    due_date_str = request.GET.get("due", "").strip()
    
    if not due_date_str:
        return render(request, "todo_info.html", {"todos": [], "due_date": "", "search_error": None})

    # Validate the due date format (MM/DD/YYYY)
    try:
        # Convert input format MM/DD/YYYY → YYYY-MM-DD (which Django expects)
        due_date = datetime.strptime(due_date_str, "%m/%d/%Y").strftime("%Y-%m-%d")
    except ValueError:
        return render(request, "todo_info.html", {"search_error": "Invalid date format. Use MM/DD/YYYY."})

    # Retrieve all matching To-Dos
    todos = Todo.objects.filter(due=due_date)

    if not todos.exists():
        return render(request, "todo_info.html", {"search_error": f"No To-Do found for {due_date_str}."})
    return render(request, "todo_info.html", {"todos": todos, "due_date": due_date_str})

