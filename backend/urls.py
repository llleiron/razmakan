from django.urls import path
from backend.views import AndznakazmCreateAPIView, AndznakazmDetailAPIView, AndznakazmListAPIView
urlpatterns = [
    path('Andznakazm/create', AndznakazmCreateAPIView.as_view()),
    path('Andznakazm/list', AndznakazmListAPIView.as_view()),
    path('Andznakazm/detail/<int:pk>', AndznakazmDetailAPIView.as_view())
]
