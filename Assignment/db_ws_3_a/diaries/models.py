from django.db import models

# Create your models here.
class Diary(models.Model):
    content = models.CharField(max_length=125)
    picture = models.ImageField(blank=True, upload_to='diary/%y/%b/%a')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    # 외래키 필드 설정
    # to : 참조하는 모델 클래스 (바로 위의 Diary)
    # on_delete : 참조하는 모델이 삭제될 때, 참조하는 모델의 레코드도 함께 삭제할지 여부
    # CASCADE : 참조하는 모델이 삭제될 때, 참조하는 모델의 레코드도 함께 삭제
    diary = models.ForeignKey(to=Diary, on_delete=models.CASCADE)
    content = models.CharField(max_length=125)
    created_at = models.DateTimeField(auto_now_add=True)
    