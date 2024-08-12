from django.urls import path
from movie import views

urlpatterns = [
    path('', views.base, name='base'),
    path('', views.cheatsheet, name="cheatsheet"),
    path('download/<int:cheatsheet_id>/',
         views.download_cheatsheet, name='download_cheatsheet'),
    path('old/', views.old, name='old'),
]
