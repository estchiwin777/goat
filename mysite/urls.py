from django.urls import path, include # อย่าลืม import include เพิ่ม
from lists import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("lists/", include("lists.urls")), # ส่งต่อหน้าที่ให้แอปจัดการ
    path('edit_priority/<int:item_id>/', views.edit_priority, name='edit_priority'), # ชื่อ name ต้องตรงกับใน {% url %}
]