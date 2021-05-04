from django.urls import include, path

urlpatterns = [
    path('vaccine_finder/', include('locator.urls')),
]
