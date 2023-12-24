from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','tickets')

class CommentSer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    ticket = serializers.ReadOnlyField(source='ticket.pk')
    class Meta:
        model = Comment
        fields = ('creator','content','date','ticket')
        
class TrackingSer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    ticket = serializers.ReadOnlyField(source='ticket.id')
    class Meta:
        model = Tracking
        fields = ('creator','time','date','ticket')

class TicketSer(serializers.ModelSerializer):
    comments = CommentSer(many=True)
    trackings = TrackingSer(many=True)
    class Meta:
        model = Ticket
        fields = ('id','creator','title','description','estimation','time','status','comments','trackings')
        
class StatusSer(serializers.ModelSerializer):
    tickets = serializers.HyperlinkedRelatedField(view_name='ticket-details',read_only=True,many=True)
    class Meta:
        model = Status
        fields = ('id','content','tickets')