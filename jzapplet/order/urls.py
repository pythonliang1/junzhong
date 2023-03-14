from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from order import views

urlpatterns = [
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:pk>/', views.OrderDetail.as_view()),

    path('employee/', views.EmployeeList.as_view()),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view()),

    path('or/', views.OrderRelationshipList.as_view()),
    path('or/<int:pk>/', views.OOrderRelationshipDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)