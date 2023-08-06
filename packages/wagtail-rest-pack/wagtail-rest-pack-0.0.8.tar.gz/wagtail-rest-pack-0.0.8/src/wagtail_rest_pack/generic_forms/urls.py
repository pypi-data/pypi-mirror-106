
from django.urls import path

from .view import FormView
from .post import PostFormView

urlpatterns = [
    path('', PostFormView.as_view(), name='form_view'),
    path('<str:name>', FormView.as_view(), name='submit_form'),
]
