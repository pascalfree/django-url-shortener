from django.urls import path

from shortener.views import follow

app_name = 'shortener'
urlpatterns = (
    path('<slug:slug>', follow, name='follow'),
)
