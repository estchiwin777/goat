from django.urls import path, include # อย่าลืม import include เพิ่ม
from lists import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("lists/", include("lists.urls")), # ส่งต่อหน้าที่ให้แอปจัดการ
]