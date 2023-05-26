from rest_framework import serializers
from pythonInter_app.models import User, ProjectPlatform

class ProjectPlatformSerializer(serializers.ModelSerializer):
    
    # len_name = serializers.SerializerMethodField()
    
    class Meta:
        model = ProjectPlatform
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    
    # len_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = "__all__"
    
'''
    def get_len_name(self, object):
        return len(object.name)    
    
    def validate(self, data):
            if data['name'] == data['Self_description']:
                raise serializers.ValidationError("Name and self description should be different")
            else:
                return data
        
        
    def validate_name(self, value):
        
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value
'''
'''
def name_length(value):
    if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    Self_description = serializers.CharField()
    available = serializers.BooleanField()
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.Self_description = validated_data.get('Self_description', instance.self_description)
        instance.available = validated_data.get('available', instance.available)
        instance.save()
        return instance
    
    def validate(self, data):
        if data['name'] == data['Self_description']:
            raise serializers.ValidationError("Name and self description should be different")
        else:
            return data
    
    #
    #def validate_name(self, value):
    #    
    #    if len(value) < 2:
    #        raise serializers.ValidationError("Name is too short!")
    #    else:
    #        return value
    #
'''