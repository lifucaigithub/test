__author__ = 'Elvis'
#coding:utf-8
from django.forms import ModelForm
from  django import  forms
from models import ExamInfo
RADIO_CHOICES = (
    ('male', "male"),
    ('female', "female"),
)
class ExamInfoForm(ModelForm):
    sex = forms.ChoiceField(label='性别',widget=forms.RadioSelect, choices=RADIO_CHOICES, initial='male',required=False)
    class Meta:
        model = ExamInfo
        fields = '__all__'