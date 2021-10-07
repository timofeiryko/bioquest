from .models import Question, QuImage, Comment, CoImage, CoFile
from django.forms import ModelForm, inlineformset_factory, BaseInlineFormSet

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = [
        'year', 'stage', 'grade', 'part', 'number',
        'text', 'tags', 'topics',
        'flag', 'type']


QuImageFormSet = inlineformset_factory(Question, QuImage, extra = 5, fields=['file', 'label'])
CommentFormSet = inlineformset_factory(Question, Comment, extra = 1, fields=['text'])
CoImageFormSet = inlineformset_factory(Comment, CoImage, extra = 3, fields=['file', 'label'])
