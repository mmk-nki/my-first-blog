#まずはモデルをインポートする
#自分で作成したモデルのインポートは,で続けてok
from django import forms
from .models import Post, Comment

#投稿フォームの追加
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

#コメントフォームの追加
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)