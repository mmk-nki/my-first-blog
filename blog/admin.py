from django.contrib import admin
from .models import Post, Comment

#投稿とコメントのモデルを登録
admin.site.register(Post)
admin.site.register(Comment)
