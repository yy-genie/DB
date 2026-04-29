from django.urls import path
from . import views


app_name = 'diaries'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:diary_pk>/comments/', views.comments_create, name='comments_create'),
    # 댓글 삭제 요청 url
    path("comments/<int:comment_pk>/delete/", views.comments_delete, name="comments_delete"),
]