from django.db import models


class Category(models.Model):
    category_name=models.CharField(max_length=200)

    def __str__(self):
        return self.category_name
    

class Student(models.Model):
    student_name=models.CharField(max_length=200,unique=True)
    place=models.CharField(max_length=200)
    Mobile_number=models.CharField(max_length=200)
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE)
