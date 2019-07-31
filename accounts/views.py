from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# 유저에 대한 클래스를 가져온다
from django.contrib import auth
# 유저에 대한 권한을 가져온다



# Create your views here.
def signup(request):
    if request.method == 'POST':
        # post 방식으로 request가 온다면 = 회원가입 내용이 온다면
        if request.POST['password1'] == request.POST['password2']:
            # 첫번째 입력한 비밀번호와 두번째 입력한 비밀번호가 같아야한다
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            # 계정 생성 시 유저네임과 페스워드를 담겠다
            auth.login(request, user)
            # 로그인을 하는 함수
            return redirect('home')
            # 모든 내용이 완료 될시 블로그 페이지로 이동
    return render(request, 'signup.html')
    # 전부 실패할시 사인업에 계속 머물수 있도록

    
def login(request):
    if request.method == 'POST':
    # 로그인 페이지의 내용을 포스트 방식으로
        username = request.POST['username']
        password = request.POST['password']
        # 유저 내임과 페스워드에 담아준다
        user = auth.authenticate(request, username=username, password=password)
        # 유저 네임과 페스워드가 맞는지 확인
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        # 유저가 맞으면 로그인을 해주고 홈으로 보내준다
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')
    # 아닐시에 로그인 페이지로 계속 머문다

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # 지금 접속되 있는 사용자가 로그아웃
        return redirect('home')
        # 로그아웃 되면 홈으로 다시 돌아간다
    return render(request,'login.html')
    # 전부 아니라면 login.html로 돌아간다
    


