from django import forms
from .models import Topic, Entry, Image


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['img_dir']
        labels = {'img_dir': ''}




