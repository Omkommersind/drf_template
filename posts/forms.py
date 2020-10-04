from django import forms

from drf_template import settings


class DateSpanForm(forms.Form):
    date_from = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    date_to = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
