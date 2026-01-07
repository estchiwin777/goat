from django.contrib import admin
from django.urls import path
from django.http import HttpResponse # เพิ่มการ import นี้

# สร้างฟังก์ชันหน้าแรกแบบง่ายๆ
def home_page(request):
    return HttpResponse('''
        <html>
            <head>
                <title>Hello,Django</title>
            </head>
            <body>
                <h1>Hello,Django</h1>
                
                <textarea id="id_body" placeholder="Body"></textarea>
            </body>
        </html>
    ''')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page), # เพิ่มบรรทัดนี้เพื่อตั้งหน้าแรก
]