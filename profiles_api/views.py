from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings



from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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



# ViewSet is used for CRUD operations
# ViewSet is more similar to a traditional Django View
# ViewSet is mapped automatically to URLs
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    # Define serializer class
    serializer_class = serializers.HelloSerializer

    # Define list method, which is similar to get method in APIView
    def list(self, request):
        """Return a hello message"""
        # Create a list of viewset features
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code'
        ]

        # Return response
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


    def create(self, request):
        """Create a new hello message"""
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


    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        # Return response
        return Response({'http_method': 'GET'})


    def update(self, request, pk=None):
        """Handle updating an object"""
        # Return response
        return Response({'http_method': 'PUT'})


    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        # Return response
        return Response({'http_method': 'PATCH'})


    def destroy(self, request, pk=None):
        """Handle removing an object"""
        # Return response
        return Response({'http_method': 'DELETE'})




class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    autthentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES