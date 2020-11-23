from django.urls import path
from .views import (
    HomeView,
    DeleteView,
    UpdateView
)
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('delete/<int:id>', DeleteView.as_view(), name='delete'),
    path('update/<int:id>', UpdateView.as_view(), name='update'),   
]
