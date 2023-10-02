from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        description = request.POST['description']
        date = request.POST['date']
        todo = Todo(title=title, category=category, description=description, date=date)
        todo.save()
        return redirect('todo_list')
    return render(request, 'create_todo.html')

def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.category = request.POST['category']
        todo.description = request.POST['description']
        todo.date = request.POST['date']
        todo.save()
        return redirect('todo_list')
    return render(request, 'update_todo.html', {'todo': todo})

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')