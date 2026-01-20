from django.db import models

class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=None)
    # เพิ่มบรรทัดนี้: กำหนดค่าเริ่มต้นเป็น Medium (M)
    priority = models.CharField(max_length=1, default='M')