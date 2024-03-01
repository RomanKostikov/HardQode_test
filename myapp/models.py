from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Creator(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name_student = models.CharField(max_length=100)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, blank=True)


class Product(models.Model):
    """1.1. Создать сущность продукта. У продукта должен быть создатель этого продукта(автор/преподаватель).
    Название продукта, дата и время старта, стоимость **(1 балл)**"""
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField(null=True)
    students = models.ManyToManyField(Student, through='StudentProduct')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    lessons_count = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)  # Добавляем поле is_available
    min_users_in_group = models.PositiveIntegerField(default=1)
    max_users_in_group = models.PositiveIntegerField(default=3)

    def __str__(self):
        return self.name


class StudentProduct(models.Model):
    """1.2. Определить, каким образом мы будем понимать, что у пользователя(клиент/студент) есть доступ к продукту."""
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name_student = models.CharField(max_length=100, blank=True)


class Lesson(models.Model):
    """1.3. Создать сущность урока. Урок может принадлежать только одному продукту. В уроке должна быть базовая
    информация: название, ссылка на видео. **(1 балл)**"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_link = models.URLField()


class Group(models.Model):
    """1.4. Создать сущность группы. По каждому продукту есть несколько групп пользователей, которые занимаются в этом
        продукте. Минимальное и максимальное количество юзеров в группе задается внутри продукта.
        Группа содержит следующую информацию: ученики, которые состоят в группе, название группы, принадлежность группы
        к продукту **(2 балла)**
        2.1. Реализации логики распределения пользователей в группы при получении доступа к продукту."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    student_names = models.JSONField(default=list)
    student_count = models.IntegerField(default=0)
