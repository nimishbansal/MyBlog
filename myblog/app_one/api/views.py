from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework import permissions

from app_one.api.serializers import PostModelSerializer
from app_one.api.paginators import StandardResultsPagination
from app_one.models import Post

class POSTListAPIView(ListAPIView):
    serializer_class = PostModelSerializer
    pagination_class = StandardResultsPagination


    def get_queryset(self):
        param=self.request.GET.get("post_type",None)
        if param==None:
            return Post.objects.all()

        return Post.objects.filter(post_type=param)


class POSTCreateAPIView(CreateAPIView):
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
