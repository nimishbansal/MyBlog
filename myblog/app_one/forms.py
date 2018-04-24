from django import forms

from .models import Post,Comment
from django.utils.translation import ugettext_lazy as _

class CreateForm(forms.ModelForm):
    # title=forms.CharField(required=True,min_length=5,max_length=100)
    # code_text=forms.CharField(required=True,min_length=3)
    class Meta:
        model = Post
        fields=["title","code_text","post_type"]



class CommentModelForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=(
            # 'user',
            'comment_text',
        )
