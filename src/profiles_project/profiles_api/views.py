from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from . import models

from . import permissions
from rest_framework.authentication import TokenAuthentication




class HelloApiView(APIView):
    """Test API View """

    serializer_class = serializers.HelloSerializers

    def get(self,request,format=None):

        an_apiview = [
            'Uses HTTP method as functions - get, post, patch, put, delete',
            'It is similar to traditional django view',
            'Gives you the most control over you logic',
            'It mapped manually to the URLs'
        ]

        return Response({'message':'Hello',  'an_apiview': an_apiview})

    def  post(self, request):
        """ Create a hello message with our name"""

        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handles updating an object"""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """ Patch request. Only handles fields provided in the request"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """ Deletes an object"""

        return Response({'method': 'delete'})


class HelloViewSets(viewsets.ViewSet):
    """ Test API View sets"""

    serializer_class = serializers.HelloSerializers

    def list(self,request,format=None):
        """ Returns a hello message """

        a_viewset = [
            'Uses actions - list, create, retrieve, update, partial update.',
            'Automatically maps to the urls using routers.',
            'Provides more functionality with less codes'
        ]

        return Response({'message':'Hello',  'a_viewset': a_viewset})

    def create(self,request):
        """ Create a new Hello Message"""

        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def  retrieve(self, request, pk=None):
        """Handles getting in an object by its Id"""

        return Response({'HTTP method': 'Get'})

    def update(self, request, pk=None):
        """ Handles updating an object"""

        return Response({'HTTP Method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ Handles updating an part of an object"""

        return Response({'HTTP Method': 'PATCH'})

    def destroy(self, request, pk=None):
        """ Handles removing an object """

        return Response({'HTTP Method' : 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating user profiles"""


    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.object.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
