from django.urls import reverse_lazy
from django.views.generic import CreateView

from src.portals.customer.models import ConvertRequest


class ConvertRequestCreateView(CreateView):
    model = ConvertRequest
    fields = '__all__'
    template_name = 'customer/convert_create_add_form.html'
    success_url = reverse_lazy('customer-portal:dashboard')
