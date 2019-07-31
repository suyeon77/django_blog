from django.db import models

# Create your models here.
# 클래스로 정의 해준다
class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    bohy = models.TextField()
    # 오타났는데 마이그레이션 해버려서 수정할수가 없다.. 잘 확인해 주자..

    # 제목으로 목록을 보이게 하는 함수
    def __str__(self): 
    # self 자기 자신을 객채로 받는다
        return self.title

    def summary(self):
        return self.bohy[:50]