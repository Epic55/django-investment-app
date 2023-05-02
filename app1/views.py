from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
import json, urllib.request
from .forms import FormClass, ModelFormClass, EmployeeForm, GeeksForm, SignupForm
from .models import ModelClass, Employee, GeeksModel
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm

#AUTHENTICATION
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form': form
    })


#FUNCTION BASED VIEW
def delete_view(request, id):
    context = {}
    obj = get_object_or_404(GeeksModel, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("../r")
    return render(request, "fbv_delete_view.html", context)

def update_view(request, id):
    context = {}
    obj = get_object_or_404(GeeksModel, id=id)
    form = GeeksForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("../r")
    context["form"] = form
    return render(request, "fbv_update_view.html", context)

def detail_view(request, id):
    context = {}
    context["data"] = GeeksModel.objects.get(id=id)
    return render(request, "fbv_detail_view.html", context)

def list_view(request):
    context = {}
    context["dataset"] = GeeksModel.objects.all()
    return render(request, "fbv_list_view.html", context)

def create_view(request):
    context = {}
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "fbv_create_view.html", context)



#CLASS BASED VIEW
class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('EmployeeRetrieve')

class EmployeeUpdate(UpdateView):
    model = Employee
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = reverse_lazy('EmployeeRetrieve')

class EmployeeDetail(DetailView):
    model = Employee
    success_url = reverse_lazy('EmployeeRetrieve')

class EmployeeRetrieve(ListView):
    model = Employee
    success_url = reverse_lazy('EmployeeRetrieve')

class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('EmployeeRetrieve')



#MODEL FORM CLASS
def model_form_class(request):
    stu = ModelFormClass(request.POST or None)
    if stu.is_valid():
        stu.save()
        stu = ModelFormClass()
    return render(request,"model_form_class.html",{'form':stu})

#FORM CLASS
def form_class(request):
    my_form = FormClass()
    if request.method == "POST":
        my_form = FormClass(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
      #      Class1.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, 'form_class.html', context)

def index(request):
    if request.method == 'POST':
        symbol1 = request.POST['symbol']
        res = urllib.request.urlopen('https://cloud.iexapis.com/stable/tops?token=&symbols='+symbol1).read()
        json_data = json.loads(res)
        data = {
            "symbol": json_data[0]['symbol'],
            "lastSalePrice": json_data[0]['lastSalePrice'],
         }
    else:
        symbol1 = ''
        data = {}
    return render(request, 'base.html', {'symbol1': symbol1, 'data': data})