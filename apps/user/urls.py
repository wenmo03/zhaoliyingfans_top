from django.urls import path

from user.views import user_profile

urlpatterns = [
    path('profile/', user_profile),
]