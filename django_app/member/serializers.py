from rest_framework import serializers
from member.models import MyUser


class UserSerializer(serializers.ModelSerializer):
    # source : 테이블 내 필드로
    user_pk = serializers.PrimaryKeyRelatedField(source='pk', read_only=True)

    post = serializers.StringRelatedField(source='post_set', many=True)

    class Meta:
        model = MyUser
        fields = (
            'user_pk',
            'username',
            'email',
            'post',
        )