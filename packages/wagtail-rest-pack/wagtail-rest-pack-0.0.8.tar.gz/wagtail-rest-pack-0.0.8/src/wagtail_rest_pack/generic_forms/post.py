import json
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponse
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission
from wagtail_rest_pack.generic_forms.models import FormBuilder

from wagtail_rest_pack.exception.handler import custom_exception_handler
from .models import FormBuilder, security_choices
from .handlers.handler import handle
from .validation import validate_form_data
from django.utils.translation import gettext as _


class PostFormSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    action = serializers.CharField(max_length=50)
    data = serializers.DictField()

    class Meta:
        fields = ['name', 'action', 'data', ]


class PostFormView(APIView):
    permission_classes = [AllowAny]
    queryset = FormBuilder.objects.all()

    def get_serializer(self, *args, **kwargs):
        return PostFormSerializer(*args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, *args, **kwargs)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        form: FormBuilder = self.queryset.get(name=data['name'])
        action = form.find_action(action=data['action'])
        permission_classes = security_choices[form.security]['permission_classes']
        if any([not perm().has_permission(request, self) for perm in permission_classes]):
            raise PermissionDenied()
        context = {
            'request': request,
            'form': form,
            'data': data['data']
        }
        context['validated_data'] = validate_form_data(**context)
        result = handle(action, **context)
        return HttpResponse(json.dumps({
            'stream': result
        }))