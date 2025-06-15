from django.urls import path
from .views import chat_api
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('api/chat/', views.chat_api, name='chat_api'),
    path('chatbot/', views.chatbot_view, name='chatbot_view'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
     path('api/chat/', chat_api, name='chat_api'),
]
