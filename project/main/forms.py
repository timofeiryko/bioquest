from .models import Question, MultipleImage
from django.forms import ModelForm

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = {
        'year', 'stage', 'grade', 'part', 'number',
        'text', 'tags', 'topics',
        'flag', 'type'}
