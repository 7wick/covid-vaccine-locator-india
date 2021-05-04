from django.urls import include, path

urlpatterns = [
    path('locator/', include('locator.urls')),
]
