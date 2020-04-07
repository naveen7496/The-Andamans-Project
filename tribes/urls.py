from django.urls import path
from . import views
urlpatterns = [
    path('', views.tribes, name='tribelistings'),
    path('<int:tribe_id>', views.tribe, name='tribe')
]