from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""

    # Define serializer class
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic'
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


    def post(self, request):
        """Create a hello message with our name"""
        # Create serializer object
        serializer = self.serializer_class(data=request.data)

        # Validate serializer object
        if serializer.is_valid():
            # Retrieve name from validated data
            name = serializer.validated_data.get('name')
            # Create message
            message = f'Hello {name}!'
            # Return response
            return Response({'message': message})
        else:
            # Return error message
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        """Handle updating an object"""
        # Return response
        return Response({'method': 'PUT'})


    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        # Return response
        return Response({'method': 'PATCH'})


    def delete(self, request, pk=None):
        """Delete an object"""
        # Return response
        return Response({'method': 'DELETE'})