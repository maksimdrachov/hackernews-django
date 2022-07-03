from django import forms

from .models import NewsPost

class NewsPostForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        fields = [
            'title',
            'url',
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Enter news title"}
            ),
            "url": forms.URLInput(
                attrs={"placeholder": "Enter news link"}
            )
        }
