from django.shortcuts import render, redirect
from .models import TodoItem
from django.contrib.auth.decorators import login_required
from .forms import TodoItemForm


@login_required(login_url="accounts:login")
def todo_list_view(request):
    """todo list view"""
    user = request.user
    query = TodoItem.objects.filter(owner=user)
    if request.method == "POST":
        checked_list = request.POST.getlist('checked')
        checked_list = list(map(int, checked_list))
        for todo_item in query:
            checked = todo_item.id in checked_list
            TodoItem.objects.filter(id=todo_item.id).update(checked=checked)
        return redirect("todoapp:todo_list")

    arg = {
        "todo_list": query,
        "todo_length": len(query),
    }
    return render(request, "todoapp/todo_list.html", arg)


@login_required(login_url="accounts:login")
def create_todo(request):
    """todo item create"""
    user = request.user
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = user
            if not instance.date:
                instance.date = "امروز"
            instance.save()
            return redirect("todoapp:todo_list")
    else:
        form = TodoItemForm()
    arg = {
        "form": form,
    }
    return render(request, "todoapp/create_todo.html", arg)


def delete_todo(request, id_):
    """delete todo item"""
    try:
        item = TodoItem.objects.get(id=id_)
    except (TodoItem.DoesNotExist, ValueError, OverflowError) as err:
        print(err)
        return redirect("todoapp:todo_list")
    if item.owner == request.user:
        item.delete()
        return redirect("todoapp:todo_list")
    return redirect("todoapp:todo_list")


def edit_todo(request, id_):
    """edit todo item"""
    try:
        item = TodoItem.objects.get(id=id_)
    except (TodoItem.DoesNotExist, ValueError, OverflowError) as err:
        print(err)
        return redirect("todoapp:todo_list")
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            work = instance.work
            date = instance.date
            if not date:
                date = "امروز"
            item.work = work
            item.date = date
            item.save()
            return redirect("todoapp:todo_list")
    else:
        if item.owner == request.user:
            arg = {
                "work": item.work,
                "date": item.date,
            }
            return render(request, "todoapp/edit_todo.html", arg)
    return redirect("todoapp:todo_list")
