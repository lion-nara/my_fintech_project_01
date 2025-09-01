# notes/forms.py
from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={"class":"form-control", "rows":4, "placeholder":"메모를 작성하세요"}),
        }
