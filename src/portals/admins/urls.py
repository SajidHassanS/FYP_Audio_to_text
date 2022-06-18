from django.urls import path, include

from src.portals.admins.views import FormView

app_name = "admin-portal"
urlpatterns = [
    path('dashboard/', FormView.as_view(), name='dashboard')
]
