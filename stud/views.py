from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from stud.forms import CategoryCreateForm,StudentCreateForm,StudentChangeForm
from stud.models import Category,Student
from django.views.generic import View,CreateView,ListView,UpdateView,DetailView
from django.urls import reverse_lazy

class CategoryCreateView(CreateView,ListView):
    template_name="category_add.html"
    form_class= CategoryCreateForm
    model=Category
    context_object_name="categories"
    success_url=reverse_lazy("category_add")

class CategoryDetailView(DetailView):
    template_name="category_detail.html"
    context_object_name="categories"
    model=Category
   

    


class StudentCreateView(View):
   def get(self,request,*args,**kwargs):
        form=StudentCreateForm()
        return render(request,"student_add.html",{"form":form})
    
   def post(self,request,*args, **kwargs):
        form=StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student-add")
        else:
             return render(request,"student_add.html",{"form":form})
        

class StudentListView(ListView):
   
    template_name="stud_list.html"
    model=Student
    context_object_name="stud"



class StudentUpdateView(UpdateView):
   
    template_name="stud_update.html"
    success_url=reverse_lazy("student-list")
    form_class=StudentChangeForm
    model=Student

class StudentDetailView(DetailView):
    template_name="studentdetail.html"
    model=Student
    context_object_name="s"
    

def remove_student(request,*args,**kwargs):
    id=kwargs.get("pk")
    Student.objects.get(id=id).delete()
    return redirect("student-list")




   

    
  
        


    
    








 

    



   