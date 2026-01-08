
from django.contrib import admin
from django.urls import path
from lists import views  # ต้องมีบรรทัดนี้

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'), 
    path('about/', views.about, name='about'), # <--- เพิ่มaboutไป
]