from django import forms
from .models import Project, TechStack, Inquiry, Testimony


class ProjectForm(forms.ModelForm):

    tech_stack = forms.ModelChoiceField(
        queryset=TechStack.objects.all(),
        widget=forms.RadioSelect,
        required=True,
        empty_label=None,
        help_text=''
    )

    class Meta:
        model = Project

        fields = [
            'project_name',
            'description',
            'tech_stack',
            'project_link',
        ]

        widgets = {
            'project_name': forms.TextInput(attrs={
                'placeholder': 'Enter project name'
            }),

            'description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Enter project description'
            }),

            'project_link': forms.URLInput(attrs={
                'placeholder': 'https://example.com'
            }),
        }


class TechStackForm(forms.ModelForm):

    class Meta:
        model = TechStack

        fields = [
            'name'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter tech stack name'
            }),
        }


class InquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        fields = '__all__'


class TestimonyForm(forms.ModelForm):

    class Meta:
        model = Testimony

        fields = [
            'full_name',
            'content',
        ]