from django import forms
from ckeditor.widgets import CKEditorWidget


class GeneratorForm(forms.Form):
    content = forms.CharField(
        widget=CKEditorWidget(), label=''
    )
