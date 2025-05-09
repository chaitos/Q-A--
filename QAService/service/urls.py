from django.contrib.auth.views import LoginView
# это файл, созданный для того, чтобы можно было импортировать маршруты для include и соблюсти
# принцип независимости приложений,
# чтобы в этом приложении хранились те приложения, которые используют именно это приложение, а не весь сайт
# в джанго


from django.urls import path
from . import views
from .views import QuestionCreateView, RegisterView, ProfileView

urlpatterns = [
    path('', views.Home.as_view()), #as_view делает из класса функцию
    path('questions/<slug:slug>/', views.QuestionDetailView.as_view(), name='question_detail'),
    path('ask/', QuestionCreateView.as_view(), name='question_create'),
    path("login/", LoginView.as_view(template_name="service/login.html"), name="login"),
    path("registration/", RegisterView.as_view(template_name="service/registration.html"), name="registration"),
    path("profile/", ProfileView.as_view(template_name="service/profile.html"), name="profile"),

]
