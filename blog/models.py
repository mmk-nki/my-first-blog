from django.conf import settings
from django.db import models
from django.utils import timezone

#投稿
class Post(models.Model):
    #他のモデルへのリンク
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #文字数が制限されたテキストを定義するフィールド
    title = models.CharField(max_length=200)
    #文字数制限無しの長いテキスト用
    text = models.TextField()
    #日付と時間のフィールド
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #ポストのタイトルのテキスト（string）が返される。
    def __str__(self):
        return self.title
    
    #コメントの件数を表示
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


#コメント
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text