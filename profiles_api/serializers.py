from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=15)



class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        # Set extra keyword arguments
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }


    # Override create method
    def create(self, validated_data):
        """Create and return a new user"""
        # Create and return user
        return models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )


    # Override update method
    def update(self, instance, validated_data):
        """Handle updating user account"""
        # Check if password is in validated data
        if 'password' in validated_data:
            # Retrieve password from validated data
            password = validated_data.pop('password')
            # Set password
            instance.set_password(password)

        # Update and return user instance
        return super().update(instance, validated_data)