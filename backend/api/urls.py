from django.urls import path
from .views import UserRegistrationView, UserLoginView, ToDoListCreateView, ToDoDetailView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('todos/', ToDoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', ToDoDetailView.as_view(), name='todo-detail')
]
