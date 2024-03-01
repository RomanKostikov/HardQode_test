from django.core.management.base import BaseCommand
from myapp.models import Group, Product
import random


# Создание команды для заполнения таблицы Group с рандомными данными(заполняется только имя группы и id продукта)

class Command(BaseCommand):
    help = 'Populate the group table with random data'

    def handle(self, *args, **options):
        all_products = list(Product.objects.all())

        for _ in range(4):  # Генерация 4 рандомных записей
            product = random.choice(all_products)
            group = Group(name=f'Random Group for {product.name}', product=product)
            group.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated the group table with random data'))
