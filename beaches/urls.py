from django.urls import path
from . import views
urlpatterns = [
    path('', views.beaches, name='beachlistings'),
    path('<int:beach_id>', views.beach, name='beach')
]