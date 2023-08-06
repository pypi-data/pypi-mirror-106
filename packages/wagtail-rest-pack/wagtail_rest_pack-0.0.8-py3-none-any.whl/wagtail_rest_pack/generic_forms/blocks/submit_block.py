from rest_framework import serializers
from wagtail.core import blocks
from wagtail_rest_pack.generic_forms.actions.send_email import SendEmailAction
from wagtail_rest_pack.generic_forms.response.snack import ShowSnackResponse
from wagtail_rest_pack.generic_forms.response.dialog import ShowDialogResponse
from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _

class SubmitBlockSerializer(serializers.Serializer):
    block_name = 'form_submit'
    name = serializers.CharField(max_length=30)
    text = serializers.CharField(max_length=30)
    expected_to_be_set = _('Expected "{field_name}" to be set, but is not')
    @staticmethod
    def block_definition():
        return SubmitBlockSerializer.block_name, SubmitBlock('submit')

    class Meta:
        fields = ('name', 'text',)

    def validate_field(self, value):
        instance = self.context['instance']
        if value.get(instance['name']) is None:
            raise ValidationError(self.expected_to_be_set.format(field_name=instance['name']))


class SubmitBlock(blocks.StructBlock):

    def get_responses(self):
        return [
            ShowDialogResponse.block_definition(),
            ShowSnackResponse.block_definition(),
        ]

    def get_actions(self):
        return [
            SendEmailAction.block_definition(),
        ]

    def __init__(self, *args, **kwargs):
        self.action_definitions = blocks.StreamBlock(self.get_actions(), min_num=1, max_num=1, label=_('Form action'))
        self.response_definition = blocks.StreamBlock(self.get_responses(), min_num=1, max_num=1, label=_('Form response'))
        super().__init__(local_blocks=[
            ('name', blocks.TextBlock(max_length=30, help_text=_('Technical name of a field, e.g. email_field'), label=_('Field name'), validators=[])),
            ('text', blocks.CharBlock(max_length=30, label=_('A text button label'))),
            ('action', self.action_definitions),
            ('response', self.response_definition)
        ], **kwargs)
