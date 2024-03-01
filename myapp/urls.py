from django.urls import path, include
from myapp.views import *

urlpatterns = [
    path('api/', include(router.urls)),
    path('products/', product_list),
    path('products/<int:product_id>/lessons/', LessonList.as_view(), name='lesson-list'),
]
