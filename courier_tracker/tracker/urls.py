from django.urls import path
from .views import dashboard_page

urlpatterns = [
    path('', dashboard_page, name='dashboard-page'),
]

