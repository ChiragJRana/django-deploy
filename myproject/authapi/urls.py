from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('instrument-list', views.instrumentList, name='instrument-list'),
    path('instrument-detail/<str:pk>/', views.instrumentDetail, name='instrument-detail'),
    path('instrument-create/', views.instrumentCreate, name='instrument-create'),
    path('instrument-update/<str:pk>', views.instrumentUpdate, name='instrument-update'),
    path('instrument-delete/<str:pk>', views.instrumentDelete, name='instrument-delete'),
]