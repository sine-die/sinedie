from .models import Client
from rest_framework import serializers
from intermediate.models import User


class ClientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.id', read_only=True)
    name = serializers.CharField(source='user.first_name')
    username = serializers.CharField(source='user.username')
    is_business = serializers.BooleanField(source='user.is_business', required=False)
    password = serializers.CharField(source='user.password', write_only=True)
    phone = serializers.CharField(source='user.phone')

    class Meta:
        model = Client
        fields = [
            'id', 'username', 'name', 'is_business', 'password', 'phone',
            'favorites', 'cur_postcode'
        ]
        optional_fields = ['favorites', 'cur_postcode']

    def create(self, validated_data):
        print(validated_data)
        validated_user = validated_data.pop('user')
        u = User.objects.create_user(**validated_user)
        return Client.objects.create(user=u, **validated_data)

    def update(self, instance, validated_data):
        user = validated_data.pop('user', [])
        for key in user.keys():
            setattr(instance.user, key, user[key])
        instance.user.save()
        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()
        return instance
