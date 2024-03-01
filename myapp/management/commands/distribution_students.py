from django.core.management.base import BaseCommand
from myapp.models import Group, StudentProduct


# 2.1. При получении доступа к продукту, распределять пользователя в группу.

class Command(BaseCommand):
    help = 'Distribute students to groups and update student_count and student_names using StudentProduct table'

    def handle(self, *args, **options):
        all_groups = list(Group.objects.all())
        all_student_products = list(StudentProduct.objects.all())

        for student_product in all_student_products:
            groups = Group.objects.filter(
                product_id=student_product.product_id)  # Получаем все группы с соответствующим product_id
            for group in groups:
                if group.student_count < 3:  # Проверяем, что в группе меньше 3 студентов
                    group.student_count += 1
                    group.student_names.append(student_product.name_student)
                    group.save()
                    break  # Прерываем цикл, чтобы добавить студента только в одну группу

        self.stdout.write(self.style.SUCCESS(
            'Successfully distributed students to groups and updated student_count and student_names using StudentProduct table with limit of 3 students per group'))
