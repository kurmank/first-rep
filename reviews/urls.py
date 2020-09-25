from django.urls import path
from .views import (
    ReviewListView,
    ReviewUpdateView,
    ReviewDetailView,
    ReviewDeleteView,
    ReviewCreateView,
)

urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),
    path('new/', ReviewCreateView.as_view(), name= 'review_new'),
    path('<int:pk>/edit/', ReviewUpdateView.as_view(), name='review_edit'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    
]