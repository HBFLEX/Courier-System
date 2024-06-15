from django.shortcuts import render
from .data import (
    dashboard_links_top, 
    dashboard_links_bottom,
    analytics_card,
)

from .models import Package, TrackingEvent
from accounts.models import User


# get a list of a few random packages being traced
def get_a_few_packages_traced():
    packages = TrackingEvent.objects.all().order_by('-timestamp')[:3]
    return packages

# dashboard page
def dashboard_page(request):
    total_packages_in_shipment = Package.objects.filter(status_id__description='In Transit').count()
    customers = User.objects.filter(role__description='Customer')[:5]
    total_orders_pending = Package.objects.filter(status_id__description='Ordered').count()
    packages_traced = get_a_few_packages_traced()
    context = {
        'title': 'Welcome | Dashboard',
        'top_menu_links': dashboard_links_top,
        'bottom_menu_links': dashboard_links_bottom,
        'analytics_card': analytics_card,
        'shipment_count': total_packages_in_shipment,
        'customers': customers,
        'total_customers': customers.count(),
        'pending_orders': total_orders_pending,
        'packages_traced': packages_traced,
    }
    return render(request, 'tracker/dashboard.html', context)
