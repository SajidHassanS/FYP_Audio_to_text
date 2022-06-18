from django.shortcuts import redirect
from django.urls import path
from django.views.generic import TemplateView
from .views import ConvertRequestCreateView

app_name = "customer-portal"


def redirect_to(request):
    return redirect("admin-portal:dashboard")


urlpatterns = [
    path('dashboard/', redirect_to, name='dashboard'),
    path('convert-request/add/', ConvertRequestCreateView.as_view(), name='convert-request-add'),
]
