from django.http import Http404
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics

# Create your views here.
class TicketsList(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSer
    
class TicketDetails(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class StatusList(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class StatusDetails(generics.RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class CreateComment(generics.CreateAPIView):
    serializer_class = CommentSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        ticket = get_object_or_404(Ticket,pk=self.kwargs.get('pk'))
        serializer.save(creator=self.request.user,ticket=ticket)
        
class CommentUpdate(generics.UpdateAPIView):
    serializer_class = CommentSer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class CommentDelete(generics.DestroyAPIView):
    serializer_class = CommentSer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class CreateTracking(generics.CreateAPIView):
    serializer_class = TrackingSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        ticket = get_object_or_404(Ticket,pk=self.kwargs.get('pk'))
        serializer.save(creator = self.request.user,ticket=ticket)