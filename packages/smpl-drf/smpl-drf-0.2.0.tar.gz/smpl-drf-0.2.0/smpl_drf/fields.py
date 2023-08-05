
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import fields
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework import serializers


class ObjectPrimaryKeyRelatedField(PrimaryKeyRelatedField):

    def to_internal_value(self, data):
        if isinstance(data, (dict,)):
            data = data.get('id', None)
        return super().to_internal_value(data)


class StringRepresentationPrimaryKeyRelatedField(PrimaryKeyRelatedField):

    def use_pk_only_optimization(self):
        return False

    def to_representation(self, value):
        return value.__str__()


class ContentTypeField(serializers.PrimaryKeyRelatedField):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_queryset(self):
        return ContentType.objects.all()

    def to_internal_value(self, data):
        search = {}
        if isinstance(data, (str,)) and data.count('.') == 1:
            app_label, model = data.split('.')
            search.update({
                'app_label': app_label,
                'model': model
            })
        else:
            search = {
                'pk': data
            }

        try:
            return self.get_queryset().get(**search)
        except ObjectDoesNotExist:
            self.fail('does_not_exist', pk_value=data)
        except (TypeError, ValueError):
            self.fail('incorrect_type', data_type=type(data).__name__)
