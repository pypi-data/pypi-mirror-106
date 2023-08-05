
import django_filters

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms.fields import MultipleChoiceField, IntegerField
from django_filters.filters import Filter


class NullBooleanSelect(forms.Select):
    def __init__(self, attrs=None):
        choices = (
            ('false', _('No')),
            ('true', _('Yes')),
            ('', _('All')),
        )
        super().__init__(attrs, choices)

    def format_value(self, value):
        try:
            return {True: 'true', False: 'false'}[value]
        except KeyError:
            return ''

    def value_from_datadict(self, data, files, name):
        value = data.get(name)
        return {
            'true': True,
            True: True,
            'false': False,
            False: False,
        }.get(value)


class NullBooleanField(forms.NullBooleanField):
    widget = NullBooleanSelect


class NullBooleanFilter(django_filters.BooleanFilter):
    field_class = NullBooleanField


class MultipleValueField(MultipleChoiceField):
    def __init__(self, *args, field_class, **kwargs):
        self.inner_field = field_class()
        super().__init__(*args, **kwargs)

    def valid_value(self, value):
        return self.inner_field.validate(value)

    def clean(self, values):
        return values and [self.inner_field.clean(value) for value in values]


class MultipleNumberFilter(Filter):
    field_class = MultipleValueField

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('lookup_expr', 'in')
        super().__init__(*args, field_class=IntegerField, **kwargs)
