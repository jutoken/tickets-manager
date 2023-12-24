from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class Status(models.Model):
    content = models.CharField(max_length=200)
    
    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name_plural = 'status'
    
class Ticket(models.Model):
    creator = models.ForeignKey('auth.User',related_name="tickets", on_delete=models.CASCADE)
    title = models.CharField(max_length =100)
    description = models.TextField(max_length = 500)
    estimation = models.DecimalField(max_digits=10,decimal_places=2)
    time = models.DecimalField(default=0,max_digits=10,decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    # relation with other models
    status = models.ForeignKey(Status,on_delete=models.CASCADE,related_name='tickets')
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    creator = models.ForeignKey('auth.User',related_name='comments',on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    # relation with other models
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE,related_name='comments')
    
    def __str__(self):
        return self.creator.username

class Tracking(models.Model):
    creator = models.ForeignKey('auth.User',related_name='trackings',on_delete=models.CASCADE)
    time = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    # relation with other models
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE,related_name='trackings')

@receiver(post_save,sender=Tracking)
def update_ticket_time(sender,instance,**kwargs):
    time = instance.time + instance.ticket.time
    Ticket.objects.filter(pk = instance.ticket.pk).update(time=time)
    
