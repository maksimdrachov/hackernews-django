from django import forms

from .models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = [
            'title',
            'description',
            'url',
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Enter job title"}
            ),
            "description": forms.Textarea(
                attrs={"placeholder": "Enter job description"}
            ),
            "url": forms.URLInput(
                attrs={"placeholder": "Enter apply link"}
            )
        }