from django.urls import path
from . import views
urlpatterns = [
    path('', views.islandsListings, name='island_listing'),
    path('<int:island_id>', views.island, name='island')
]