from . import views
from django.urls import path

urlpatterns = [
    path('view/', views.schoolListView.as_view()),
    path('create/', views.schoolCreateView.as_view()),
    path('update/<int:schl_id>/', views.schoolUpdateView.as_view()),
    path('delete/<int:schl_id>/', views.schoolDeleteView.as_view()),
]