from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.title
    # 어드민 사이트에 타이틀 띄워주는 함수
