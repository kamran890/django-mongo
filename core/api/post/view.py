from rest_framework_mongoengine import viewsets
from rest_framework.response import Response

from core.models import Post
from core.api.post.serializer import (
    PostSerializer,
)
from core.utils.exception import QueryInvalid
import json


class PostViewset(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def list(self, request):
        if 'query' in request.GET:
            try:
                query = json.loads(request.GET['query'])
                self.queryset = Post.objects(__raw__=query)
            except Exception as e:
                raise QueryInvalid()

        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data, many=True)
