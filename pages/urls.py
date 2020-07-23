from django.urls import path
from .views import HomePageView

urlpatterns = [
    # HomePageView is a class so we use as_view
    path('', HomePageView.as_view(), name='home'),
]
