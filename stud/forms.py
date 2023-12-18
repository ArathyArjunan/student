from django import forms
from stud.models import Category,Student


class CategoryCreateForm(forms.ModelForm):

    class Meta:
        model=Category
        fields="__all__"


class StudentCreateForm(forms.ModelForm):

    class Meta:
        model=Student
        fields="__all__"

        widgets={

            "student_name":forms.TextInput(attrs={"class":"form-control"}),
             "place":forms.TextInput(attrs={"class":"form-control"}), 
             "Mobile_number":forms.TextInput(attrs={"class":"form-control"})
        }



class StudentChangeForm(forms.ModelForm):

    class Meta:
        model=Student
        fields="__all__"

        widgets={

            "student_name":forms.TextInput(attrs={"class":"form-control"}),
             "place":forms.TextInput(attrs={"class":"form-control"}), 
             "Mobile_number":forms.TextInput(attrs={"class":"form-control"})
        }




# class CategorySearchForm(forms.Form):
#     category_name=forms.CharField()