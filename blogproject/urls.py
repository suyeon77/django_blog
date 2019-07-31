from django.contrib import admin
from django.urls import path, include
# blogapp에 있는 url.py에서 urlpattern을 불러오기 위해 include를 써준다
import blogapp.views
import portfolioapp.views

from django.conf import settings
from django.conf.urls.static import static
# media 파일을 임포트 하기 위해 필요한 것들

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name='home'),
    # path('blog/<int:blog_id>', blogapp.views.detail, name='detail'),
    # path('new/', blogapp.views.new, name='new'),
    # path('blog/create', blogapp.views.create, name='create'),
    # path가 있다고 무조건 html 띄우는건 x == path(어떤 url이 들어오면, (어디에 있는) 어떤 함수 실행시켜라)

    # 주석 처리해준 path는 blogapp에서 관리하기 위해 옮긴 path 입니다.
    path('blog/', include('blogapp.urls')),
    # blogapp에 url에서 가져온다
    path('portfolio/', portfolioapp.views.portfolio, name='portfolio'),
    path('accounts/', include('accounts.urls')),
    # accounts의 url 연결
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# url을 타고 들어와서 미디어 저장

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# # 이런식으로 추가 가능