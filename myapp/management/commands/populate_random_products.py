from django.core.management.base import BaseCommand
from myapp.models import Product, Creator
from faker import Faker
import random
from datetime import timedelta, datetime


# Создание команды для заполнения таблицы Product с рандомными данными

class Command(BaseCommand):
    help = 'Populates the database and distributes users'

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(5):  # Создаем 5 случайных продуктов
            name = fake.word()
            price = fake.random_number(2)
            creators = Creator.objects.all()
            start_date = datetime.now() - timedelta(
                days=random.randint(1, 365))  # случайная дата в пределах последнего года
            random_creator = random.choice(creators)
            product = Product.objects.create(name=name, price=price, creator=random_creator,
                                             min_users_in_group=1, max_users_in_group=3, start_date=start_date)
            self.stdout.write(self.style.SUCCESS(f'Product {product.name} created'))
