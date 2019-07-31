from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# 밑에 create 함수에서 timezone now를 가져오기 위해 임포트 했다
from .models import Blog
from django.core.paginator import Paginator
# 페이지네이션을 위해 페이지네이터를 임포트
from .forms import BlogPost
# 폼 임포트

# Create your views here.
def home(reqeust):
    blogs = Blog.objects 
    blog_list = Blog.objects.all()
    # 블로그 리스트를 가져와라
    paginator = Paginator(blog_list, 4)
    # 한페이지에 몇개의 객체가 있을건가
    page = reqeust.GET.get('page')
    # get으로 얻어낸 value 값을 페이지에 받겠다
    posts = paginator.get_page(page)
    # get_page 안에 page 번호를 쓴다
    return render(reqeust, 'home.html', {'blogs' : blogs, 'posts':posts})

def detail(reqeust, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(reqeust, 'detail.html', {'details' : details})

def new(reqeust):
    return render(reqeust, 'new.html')

def create(reqeust):
    # 입력받은 내용을 데이터 베이스에 넣어주는 함수
    blog = Blog()
    blog.title = reqeust.GET['title']
    blog.bohy = reqeust.GET['bohy']
    blog.pub_date = timezone.datetime.now()
    # 장고 유틸에서 임포트 필요
    blog.save()
    # 쿼리셋 메소드 : 이겍체를 데이터 베이스에 저장해라 .save // .delete 객체에 대한것을 지워라
    return redirect('/blog/'+str(blog.id))
    # 장고.숏컷에서 임포트 해와야한다
    # redirect(URL) : 위에 있는 함수 전부 처리한후 url로 넘기세요
    # url은 항상 str 하지만 blog.id가 int 형이기 떄문에 형 변형을 시켜줌

    # redirect와 render의 차이
    # redirect(URL) : 다른 URL을 입력할수 있다.
    # ex) redirect(google.com) - 입력 받고 구글을 띄운다.

    # render
    # 3번째 인자로 딕셔너리 - html상에서 해결하고 싶을때 사용

def blogpost(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.now()
            blog.save()
            return redirect('home')
    else:
        form = BlogPost()
    return render(request,'new.html',{'forms':forms})

def delete(reqeust, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog. delete()
    return redirect('home')

def update(reqeust, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    form = NewBlog(request.POST, instance = blog)
    if form.is_valid():
        form.save()
        return redirect('home')
    


