from django.core.management.base import BaseCommand
from myapp.models import Student, Product
# 1.1. Определить, каким образом мы будем понимать, что у пользователя(клиент/студент) есть доступ к продукту.
# При получении доступа к продукту, проверять, есть ли у него доступ к продукту. Если нет, то выдавать ошибку.


class Command(BaseCommand):
    help = 'Check available product for a student'

    def handle(self, *args, **options):
        student_name = input('Enter the student name: ')
        try:
            student = Student.objects.get(name_student=student_name)
            product = Product.objects.filter(students=student, is_available=True).first()
            if product:
                self.stdout.write(self.style.SUCCESS(f'The available product for {student_name} is: {product.name}'))
            else:
                self.stdout.write(self.style.ERROR(f'No available product for {student_name}'))
        except Student.DoesNotExist:
            self.stdout.write(self.style.ERROR('Student not found'))
