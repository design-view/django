from django.db import models

# Create your models here.
# 숫자형 : IntegerField, FloatField
# 문자형 : CharField, TextField, EmailField, URLField
# 날짜형 : DateTimeField, DateField, TimeField
# 기타유형 : BooleanField, FileField, ImageField, NullBooleanField,SlugField

# 필드 속성 
# primary_key : pk설정, pk설정이 없을 경우 ID열을 자동 생성
# max_length: 데이터 길이 설정
# blank: 공백 허용 여부
# null : null값 허용 여부
# default : 기본값 설정
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    # Post클래스를 문자열로 출력할 시 postname을 반환함
    def __str__(self):
        return self.postname
    