from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text'] # only field we want to include in the form is text
        labels = {'text': ''} # tell Django not to generate a label for the text field


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # override Django's default widget choice for this field; Textarea element is a multi-line text input