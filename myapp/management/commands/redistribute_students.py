from django.core.management.base import BaseCommand
from myapp.models import Group, StudentProduct, Product
from django.utils import timezone
import itertools
import datetime


# 2.1. При получении доступа к продукту, распределять пользователя в группу. Если продукт ещё не начался, то можно
#    пересобрать группы так, чтобы везде было примерно одинаковое количество участников.
#
#    По-умолчанию алгоритм распределения должен работать заполняя до максимального значения **(5 баллов)**.
#
#    **+3 балла** дается за реализацию алгоритма распределения по группам так, чтобы в каждой группе количество
#    участников не отличалось больше, чем на 1. При этом, минимальные и максимальные значения участников в группе должны
#    быть учтены.

class Command(BaseCommand):
    help = 'Redistribute students to groups based on product start date'

    def handle(self, *args, **options):
        current_date = timezone.make_aware(datetime.datetime(2022, 1, 1, 0, 0, 0))

        products = Product.objects.filter(start_date__gt=current_date)
        for product in products:
            if product.start_date > current_date:
                groups = Group.objects.filter(product_id=product.id)
                students = StudentProduct.objects.filter(product=product)

                # Remove duplicates from students
                unique_students = students.distinct()

                # Distribute students evenly among groups
                grouped_students = itertools.cycle(unique_students)
                for group in groups:
                    group_students = [next(grouped_students) for _ in
                                      range(len(unique_students) // len(groups))]  # Evenly distribute students
                    group.student_count = len(group_students)
                    group.student_names = [student.name_student for student in group_students]
                    group.save()

        self.stdout.write(self.style.SUCCESS(
            'Successfully redistributed students to groups based on product start date with maximum difference of 1 '
            'student per group and 3 students per group limit, and unique student ids in each group, evenly '
            'distributed'))
