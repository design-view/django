from django.db import models

# Create your models here.
class Notice(models.Model):
    # id 작성하지 않으면 자동생성함
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    views = models.IntegerField()
    create_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    