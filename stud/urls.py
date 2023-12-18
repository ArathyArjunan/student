from django.urls import path
from stud import views

urlpatterns = [
    path("category/",views.CategoryCreateView.as_view(),name='category_add'),
    path("category/<int:pk>/",views.CategoryDetailView.as_view(),name='category-detail'),
    path("student/add",views.StudentCreateView.as_view(),name='student-add'),
    path("student/all",views.StudentListView.as_view(),name='student-list'),
    path("student/<int:pk>/change",views.StudentUpdateView.as_view(),name='student-update'),
     path("student/<int:pk>/remove",views.remove_student,name='remove-student'),
    path("student/<int:pk>/change/list",views.StudentDetailView.as_view(),name='student-detail'),
]


