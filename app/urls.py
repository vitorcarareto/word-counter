from django.urls import path
from .views import *

urlpatterns = [
    path('', WordCountView.as_view(template_name='word_count.html'), name='word_count'),
]
