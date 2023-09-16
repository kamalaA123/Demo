from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .forms import todoform
from django .views.generic import ListView
from django .views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
# Create your views here.

class listtask(ListView):
    model = task
    template_name = 'demo.html'
    context_object_name = 'data'

class detailtask(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'detail'

class updatetask(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'Task'
    fields = ('taskname','priority','date')

    def get_success_url(self):
        return reverse_lazy('detailtask',kwargs={'pk':self.object.id})

class deletetask(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('listtask')
def test(request):
    detail = task.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        details=task(taskname=name,priority=priority,date=date)
        details.save()
    return render(request,'demo.html',{'data':detail})

# def details(request):
#
#     return render(request,'details.html',)

def delete(request,taskid):
    Task=task.objects.get(id=taskid)
    if request.method=='POST':
        Task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    Task=task.objects.get(id=id)
    f=todoform(request.POST or None,instance=Task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':Task})