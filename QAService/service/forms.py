from django import forms
from .models import Question, Answer


#DjangoForms генерит свою html форму на основе модели, обрабатывает ввод пользователя и проверяет данные.

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(
                attrs={'rows': 4, 'placeholder': 'Введите содержимое вопроса...', 'class': 'textarea'}),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Введите ваш ответ...'}),
        }
        labels = {
            'content': ''  # Убираем надпись "Content:"
        }

