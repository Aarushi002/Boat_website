from django.urls import path
from .views import*
from django.views.generic import TemplateView
urlpatterns = [
    path('',home_page, name="Home-Page"),
    path('gallery', TemplateView.as_view(template_name="root/gallery.html"), name='Gallery'),
    path('faq/learnmore', faq_page , name='Faq-learnmore'),
    
]