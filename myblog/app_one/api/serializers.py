from rest_framework import serializers

from app_one.models import Post


class PostModelSerializer(serializers.ModelSerializer):

    date_display = serializers.SerializerMethodField()

    class Meta():
        model=Post
        fields=["title","post_id","code_text","post_type","date_display"]

    def get_date_display(self,obj):
        return obj.timestamp.strftime("%b %d %I:%M %p")






