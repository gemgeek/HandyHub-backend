from django.urls import path
from .views import ServiceCategoryListView

urlpatterns = [
    path('services/categories/', ServiceCategoryListView.as_view(), name='service-categories'),
]
