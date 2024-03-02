from django.shortcuts import render
from rest_framework import serializers, viewsets, routers, generics, permissions
from myapp.models import Product, Lesson, Group, Student
from django.db.models import Count, F, FloatField, ExpressionWrapper


# Create your views here.

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'product']


class ProductSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(product=obj).count()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'lessons_count']
        template_name = 'rest_framework/api.html'


def product_list(request):
    """2.2. Реализовать API на список продуктов, доступных для покупки, которое бы включало в себя основную информацию
    о продукте и количество уроков, которые принадлежат продукту"""
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return render(request, 'rest_framework/product_list.html', {'products': serializer.data})


class LessonList(generics.ListAPIView):
    """"2.3.Реализовать API с выведением списка уроков по конкретному продукту к которому пользователь имеет доступ.
    Для тестирования необходим postman"""
    serializer_class = LessonSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']  # Получаем ID продукта из URL
        product = Product.objects.get(id=product_id)
        # Проверяем, имеет ли текущий пользователь доступ к этому продукту,
        # и получаем список уроков по этому продукту
        if self.request.user in product.allowed_users.all():
            return Lesson.objects.filter(product=product)
        else:
            # Если у пользователя нет доступа, возвращаем пустой queryset
            return Lesson.objects.none()

    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return render(request, 'rest_framework/lesson_list.html', {'lessons': serializer.data})


def product_stats_view(request):
    """
    Реализовать API для отображения статистики по продуктам.
Необходимо отобразить список всех продуктов на платформе, к каждому продукту приложить информацию:

Количество учеников занимающихся на продукте.
На сколько % заполнены группы? (среднее значение по количеству участников в группах от максимального значения
участников в группе).
Процент приобретения продукта (рассчитывается исходя из количества полученных доступов к продукту деленное на общее
количество пользователей на платформе).
    """
    products = Product.objects.annotate(
        num_students=Count('studentproduct', distinct=True),
        avg_group_fill_rate=ExpressionWrapper(
            100.0 * F('group__student_count') / F('max_users_in_group'),
            output_field=FloatField()
        ),
        purchase_percentage=ExpressionWrapper(
            100.0 * Count('studentproduct') / Student.objects.count(),
            output_field=FloatField()
        )
    ).values('id', 'name', 'num_students', 'avg_group_fill_rate', 'purchase_percentage')

    return render(request, 'rest_framework/product_stats.html', {'products': products})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
