# # from django.shortcuts import render
# #
# # # Create your views here.
# # #1-QUICKSTART SAMPLE PROJECT
# from django.contrib.auth. models import User, Group
# from rest_framework import viewsets
# # from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
# from .serializers import UserSerializer, GroupSerializer
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#
#
# #
# # from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# # from rest_framework.permissions import IsAuthenticated
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# #
# # class ExampleView(APIView):
# #     authentication_classes = [SessionAuthentication, BasicAuthentication]
# #     permission_classes = [IsAuthenticated]
# #
# #     def get(self, request, format=None):
# #         content = {
# #             'user': unicode(request.user),  # `django.contrib.auth.User` instance.
# #             'auth': unicode(request.auth),  # None
# #         }
# #         return Response(content)