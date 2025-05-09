from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from slugify import slugify #используем слагифай не из стандартной библиотеки джанго, чтобы появлялся слаг кириллицы



class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions', verbose_name='Автор вопроса')
    title = models.CharField(max_length=255, verbose_name="Заголовок") #verbose_name отвечает за то, как отображается поле в админке
    content = models.TextField(blank=True, verbose_name="Содержание") #blank=True - возможность оставить поле пустым(в форме джанго)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания') #auto_now_add=True заполняется поле ТЕКУЩИМ временем при создании вопроса, при изменении время не меняется
    time_update =  models.DateTimeField(auto_now=True, verbose_name='Время изменения') #Меняется при изменении
    is_active = models.BooleanField(default=True, verbose_name='Статус') #soft delete - делаю данные неактивными, чтобы в случае случайного удаления - их можно было восстановить
    slug = models.SlugField(unique=True, blank=True)  # слаг

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == "":
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Question.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Вопрос' # заменяет название в админ панели
        verbose_name_plural = "Вопросы" # множественное число в названии(чтобы убрать s на конце)

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField(blank=False)
    time_create = models.DateTimeField(auto_now_add=True) #auto_now_add=True заполняется поле ТЕКУЩИМ временем при создании вопроса, при изменении время не меняется
    time_update =  models.DateTimeField(auto_now=True) #Меняется при изменении
    is_active = models.BooleanField(default=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    parent = models.ForeignKey(
        "self",  # ссылаемся на саму модель
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="child_answers"
    )
    #проверяет, является ли ответ ответом на ответ, или ответом на вопрос
    # (бланк нужен, чтобы мы при создании строки не указывали значение этого поля)
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = "Ответы"

# Промежуточная таблица, созданная в ручную для создания связи многие ко многим. Нужна для большей гибкости,
# т.к. если использовать класс ManyToManyField, то
# таблицу создаст джанго и изменить ее и добавить что-то будет труднее
class QuestionLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # класс метаданных для того, чтоб лайки были уникальными
    class Meta():
        unique_together = ('user', 'question') #специальный параметр внутри class Meta

        verbose_name = 'Лайк на вопрос'
        verbose_name_plural = "Лайки на вопросах"

# То же самое, что и с QuetionLike только для answer
class AnswerLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    # класс метаданных для того, чтоб лайки были уникальными
    class Meta():
        unique_together = ('user', 'answer')
        verbose_name = 'Лайк на ответ'
        verbose_name_plural = "Лайки на ответах"
