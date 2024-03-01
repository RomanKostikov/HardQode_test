from django.core.management.base import BaseCommand
from myapp.models import Student, Product, StudentProduct
import random


# 1.1. Определить, каким образом мы будем понимать, что у пользователя(клиент/студент) есть доступ к продукту
# наполнение таблицы StudentProduct

class Command(BaseCommand):
    help = 'Populate the studentproduct table with random data'

    def handle(self, *args, **options):
        all_students = list(Student.objects.all())
        all_products = list(Product.objects.all())

        # Перемешиваем список продуктов для случайного выбора
        random.shuffle(all_products)

        for i, student in enumerate(all_students):
            product = all_products[i % len(
                all_products)]  # Используем остаток от деления, чтобы обеспечить каждому студенту уникальный продукт
            student_product = StudentProduct(student=student, product=product,
                                             name_student=student.name_student)  # Добавляем передачу имени студента
            student_product.save()

        self.stdout.write(
            self.style.SUCCESS(
                'Successfully populated the studentproduct table with unique data for each student, including student names'))
