from django.urls import path
from text_to_html_generator.html_generator.views import converter_view

urlpatterns = [
    path("", converter_view, name='converter-view')
]