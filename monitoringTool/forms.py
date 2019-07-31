from django import forms
from .models import Test


class ContentForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = ["content_title", "content_data"]

