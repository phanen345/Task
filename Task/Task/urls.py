
 # core/urls.py
from django.urls import path
from mainapp.views import index_view,registration_view, login_view,task_view

urlpatterns = [
    path('', index_view, name='index'),
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('task/', task_view, name='task'),
    # ... other URL patterns ...
]
