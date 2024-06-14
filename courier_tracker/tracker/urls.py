from django.urls import path
from .views import dashboard_page

urlpatterns = [
    path('dashboard/', dashboard_page, name='dashboard-page'),
]

