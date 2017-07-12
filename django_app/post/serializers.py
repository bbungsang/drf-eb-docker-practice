from rest_framework import serializers

from post.models import Post


class PostCerializer(serializers.ModelSerializer):
    post_pk = serializers.PrimaryKeyRelatedField(source='pk', read_only=True)

    # level 은 아래 get_level() 에 대한 함수 자체이다.
    level = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()



    class Meta:
        model = Post
        fields = (
            'post_pk',
            'level',
            'author',
            'title',
            'my_comment',
        )

    def get_level(self, obj):
        # key 에 대한 value 를 보여준다.
        return obj.get_level_display()

    def get_author(self, obj):
        return obj.author.username

