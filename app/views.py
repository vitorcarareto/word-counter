from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from .mixins import AjaxFormMixin
from .forms import *


class WordCountView(AjaxFormMixin, FormView):
    form_class = WordCountForm
    success_url = 'word_count'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def get_result(self, form, **kwargs):
        text = form.cleaned_data['text']
        result = {
            'count': self.count_words(text)
        }
        return result

    @staticmethod
    def count_words(text):
        return len(text.split(' '))
