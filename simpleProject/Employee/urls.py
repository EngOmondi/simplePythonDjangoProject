from django.urls import path
from Employee import views
# importing views from views..py
from .views import Employee_Details
from .views import Image

urlpatterns = [
    path('simpleProject/', views.Employee_Info),
    path('',Employee_Details),
    path('image/', Image)
] 