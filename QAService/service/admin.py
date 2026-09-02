from django.contrib import admin


from service.models import Question, Answer, QuestionLike, AnswerLike

@admin.register(Question) #декоратор, который регистрирует модель и навешивает на нее этот класс
class QuestionAdmin(admin.ModelAdmin):
    fields = [] #поля, которые будут отобржаться в форме вопроса
    list_display = ('id', 'author', 'title', 'is_active', 'time_create') #Отображаемые поля в адмнинке, для этого надо потом указать класс при регистрации модели
    list_display_links = ('id', 'author', 'title') #кликабельные поля, которые переносят на подробную инфу
    ordering = ['time_create', 'author'] #порядок сортировки(только в админке) ['-time_create'] - сортировка в обратном порядке
    list_editable = ['is_active'] #возможность редактировать поле
    list_per_page = 10 #пагинация
    search_fields = ['title', 'author__username']  # поиск(происходит только по своим полям, если поле ForiengKey, то выбросит ошибку. Чтобы ее исправить используем __(чтобы управлять процессом поиска) и указываем то поле, которое нас интересует в связанной модели)
    list_filter = ["author__username", "title", 'is_active'] #фильтрация в админке, можно делать свою собественную фильтрацию


# admin.site.register(Question, QuestionAdmin) вместо этого кода можно указать декоратор
#admin.site.register(Answer)
#admin.site.register(QuestionLike)
#admin.site.register(AnswerLike)

@admin.register(Answer) #декоратор, который регистрирует модель и навешивает на нее этот класс
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'is_active', 'time_create')
    list_display_links = ('id', 'author',)
    ordering = ['time_create', 'author']