from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import MyTodo


# Create your views here.
def index(request):
    todos = MyTodo.objects.all().order_by('-created_at')
    form = TodoForm
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'todos': todos,
        'form': form,
    }
    return render(request, 'todos/index.html', context=context)

def UpdateTodo(request, pk):
    task = MyTodo.objects.get(id=pk)

    form = TodoForm(instance=task)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request, "todos/update.html", {"task_edit_form": form})


def delete(request, id):
    item = MyTodo.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'todos/delete.html', {'item': item})
