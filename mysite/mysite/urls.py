
from django.contrib import admin
from django.urls import path
from lists import views  # ต้องมีบรรทัดนี้

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'), # ต้องชี้มาที่ views.home_page
]