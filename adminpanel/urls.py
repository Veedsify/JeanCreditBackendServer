from .views import admin_dashboard
from django.urls import path

urlpatterns = [
    # Admin panel URLs
    path("api/", admin_dashboard, name="admin_dashboard"),
]
