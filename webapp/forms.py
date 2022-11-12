from django import forms
from django.forms import widgets


class RecordForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label='Название', error_messages={
        'required': "Поле обязательное для заполнение"},
                            widget=widgets.TextInput(attrs={'rows': 3, 'class': 'form-control mb-3'}))
    email_author = forms.EmailField(max_length=40, required=True, label='Е-маил', error_messages={
        'required': "Поле обязательное для заполнение"},
                                    widget=widgets.TextInput(attrs={'rows': 3, 'class': 'form-control mb-3'}))
    content = forms.CharField(max_length=2000, required=True, label='Подробная описание',
                              widget=widgets.Textarea(attrs={'rows': 6, 'class': 'form-control mb-3'}))


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label='Название', error_messages={
        'required': "Поле обязательное для заполнение"})
