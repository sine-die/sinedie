from .models import Business
from rest_framework import serializers
from intermediate.models import User


class BusinessSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.id', read_only=True)
    name = serializers.CharField(source='user.first_name')
    username = serializers.CharField(source='user.username')
    is_business = serializers.BooleanField(source='user.is_business')
    password = serializers.CharField(source='user.password', write_only=True)
    phone = serializers.CharField(source='user.phone')

    class Meta:
        model = Business
        fields = [
            'id', 'username', 'name', 'username', 'is_business', 'password', 'phone',
            'address', 'city', 'postcode', 'max_capacity', 'cur_capacity',
            'business_type', 'description'
        ]

    def create(self, validated_data):
        validated_user = validated_data.pop('user')
        u = User.objects.create_user(**validated_user)
        return Business.objects.create(user=u, **validated_data)

    def update(self, instance, validated_data):
        user = validated_data.pop('user', [])
        for key in user.keys():
            setattr(instance.user, key, user[key])
        instance.user.save()
        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()
        return instance
