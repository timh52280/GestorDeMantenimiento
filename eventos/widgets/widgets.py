from django import forms
from django.utils.safestring import mark_safe

class PreformattedTextWidget(forms.Widget):
   def render(self, name, value, attrs=None):
    return mark_safe("<br/><pre>%s </pre>" %(value))