import datetime
from django import forms


class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=100)
    pub_date = forms.DateField(initial=datetime.date.today)


class OptionForm(forms.Form):
    option_text = forms.CharField(max_length=100)
