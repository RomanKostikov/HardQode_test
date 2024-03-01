from django.core.management.base import BaseCommand
from myapp.models import Student
from faker import Faker  # Убедитесь, что у вас установлена библиотека Faker


# Создание команды для заполнения таблицы Student с рандомными данными

class Command(BaseCommand):
    help = 'Populate the student table with random data'

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(15):  # Генерация 15 рандомных студентов
            student = Student(name_student=fake.name())
            student.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated the student table with random data'))
