from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.product_list_view),
    path('detail/<int:id>/', views.product_detail_view),
]