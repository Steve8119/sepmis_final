from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    admission_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    year_of_studies = models.IntegerField(blank=True, null=True)
    total_fees = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fees_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.full_name if self.full_name else self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    # Update profile fields whenever User instance is saved
    instance.profile.full_name = instance.get_full_name()
    instance.profile.save()






# models.py

# from django.db import models
# from django.contrib.auth.models import User
# from core.models import Profile

# class StudentUnits(models.Model):
#     user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     unit_name = models.CharField(max_length=100)
    

#     def __str__(self):
#         return f'{self.user_profile.user.username} - {self.unit_name}'



class Unit(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='units')
    name = models.CharField(max_length=100)
    result = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Notification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp}"






