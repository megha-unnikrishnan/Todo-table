from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from .models import TodoTask
from .forms import TodoTaskForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView

class Listview(ListView):
    model = TodoTask
    template_name = 'index.html'
    context_object_name = 'task'

class Detailview(DetailView):
    model = TodoTask
    template_name = 'detail.html'
    context_object_name = 'task'

class Updateview(UpdateView):
    model = TodoTask
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ['name','task','priority','date']

    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})

class Deleteview(DeleteView):
    model = TodoTask
    template_name = 'delete.html'
    success_url = reverse_lazy('listview')

class Createview(CreateView):
    model = TodoTask
    template_name = 'add_task.html'
    fields = ('name','task','priority','date')
    success_url = reverse_lazy('listview')

def home(request):
    task = TodoTask.objects.all()
    return render(request,'index.html',{'task':task})
def add(request):
    task1 = TodoTask.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        task = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = TodoTask(name=name, task=task,priority=priority, date=date)
        task.save()
        return redirect('/')
    return render(request,'add_task.html',{'task':task1})
def delete(request,taskid):
    task=TodoTask.objects.get(id=taskid)
    if 'yes' in request.POST:
        task.delete()
        return redirect('/')
    elif 'no' in request.POST:
        return redirect('/')
    else:
        pass
    return render(request,'delete.html',{'task2':task})
def update(request,updateid):
    task=TodoTask.objects.get(id=updateid)
    form=TodoTaskForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':form})
# Create your views here.
