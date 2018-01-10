#coding:utf-8
from django.db import models
from django import  forms
# Create your models here.

# Create your models here.
LEVEL_CHOICES = (
    ('N1', 'N1'),
    ('N2', 'N2'),
    ('N3', 'N3'),
    ('N4', 'N4'),
    ('N5', 'N5'),
    ('NO', 'NO'),
)

class ExamInfo(models.Model):
    name = models.CharField('姓名',max_length=10)
    level = models.CharField('难度',max_length=2, choices=LEVEL_CHOICES)

   # ENV = forms.ChoiceField(widget=forms.RadioSelect, choices=choices.ENV_CHOICES, initial='test',required=False)