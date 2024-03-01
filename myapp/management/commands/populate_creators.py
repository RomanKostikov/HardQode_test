from django.core.management.base import BaseCommand
from faker import Faker
from myapp.models import Creator


# Создание команды для заполнения таблицы Creator с рандомными данными

class Command(BaseCommand):
    help = 'Populate the Creator table with random data'

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(10):  # создаем 10 рандомных создателей
            Creator.objects.create(name=fake.name())

        self.stdout.write(self.style.SUCCESS('Successfully populated the Creator table with random data'))
