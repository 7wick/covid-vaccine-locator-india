from django.urls import path
from . import views

app_name = 'locator'
urlpatterns = [
    path('', views.DetailViewset.as_view({'post': 'get_details'})),
]
