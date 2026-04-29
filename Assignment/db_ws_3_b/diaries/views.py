from django.shortcuts import render, redirect
from .models import Diary
from .forms import DiaryForm, CommentForm

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    context = {
        'diaries': diaries,
        'form' : CommentForm()
    }
    return render(request, 'diaries/index.html', context)

def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)

def comment_create(request, diary_pk):
    # pk를 통해서 diary 조회
    # 이 diary가 댓글이 달릴 diary
    diary = Diary.objects.get(pk=diary_pk)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            # 아직 form에는 diary 정보가 없으므로 DB에 저장 불가
            # Comment 인스턴스만 일단 반환 받을 수 있도록 commit=False
            # commit=False :DB에 저장 안함
            comment = form.save(commit=False)
            comment.diary = diary
            comment.save()

    return redirect('diaries:index')