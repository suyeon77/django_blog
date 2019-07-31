# url을 효율적으로 정리하기 위해 app 안에 url.py를 만들어서 관리합니다
# blogapp 안에 있는 url.py이기 떄문에 blogapp에 관한 url을 넣어줍니다.

from django.contrib import admin
from django.urls import path
from . import views
# project 안에 url에서 가져온 import blogapp.views 를 from . import views 라고 수정해 줬습니다.

urlpatterns = [
    path('<int:blog_id>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create', views.create, name='create'),
    # path('update/<int:blog_id>', views.update, name='update'),
    # path('delete/<int:blog_id>', views.delete, name='delete'),
   
    # blogapp 에 있는 url로 가져오면서 겹치는 것들을 지워줍니다.
    path('newblog/', views.blogpost, name='newblog'),
    # path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:blog_id>', views.delete, name='delete'),
]