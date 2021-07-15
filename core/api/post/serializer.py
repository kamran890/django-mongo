from rest_framework_mongoengine import serializers

from core.models import Post


class PostSerializer(serializers.DynamicDocumentSerializer):
    class Meta:
        model = Post
        fields = '__all__'
