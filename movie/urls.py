from django.urls import path
from movie import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.base, name='base'),
    path('', views.cheatsheet, name="cheatsheet"),
    path('download/<int:cheatsheet_id>/',
         views.download_cheatsheet, name='download_cheatsheet'),
    path('old/', views.old, name='old'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)