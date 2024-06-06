from django.db import models
from django.utils import timezone
import random
import string
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    space = models.ForeignKey('Space', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='')
    information = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    in_use = models.BooleanField(default=False)
    last_changed_by = models.CharField(max_length=150, null=True, blank=True)
    last_changed_date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    return_by = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        permissions = [
            ("delete_log", "Can delete log"),
        ]

class Space(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_spaces')
    members = models.ManyToManyField(User, related_name='spaces')
    name = models.CharField(max_length=100)
    descriptions = models.TextField()
    code = models.CharField(max_length=8, unique=True, null=True)
    pinned = models.IntegerField(default=False)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def generateCode(self):
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for _ in range(8))
        while Space.objects.filter(code=code).exists():
            code = ''.join(random.choice(characters) for _ in range(8))
        return code

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generateCode()
        super().save(*args, **kwargs)

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class spaceRoles(models.Model):
    ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('member', 'Member'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
   
        if self.role == 'owner':
            self.assign_owner_permissions()
        elif self.role == 'member':
            self.assign_member_permissions()

    def assign_owner_permissions(self):
        
        content_type = ContentType.objects.get_for_model(UserLog)

  
        owner_permissions = Permission.objects.filter(content_type=content_type).filter(
            codename__in=['delete_log', 'can_edit_logs', 'can_delete_logs'])
        self.user.user_permissions.add(*owner_permissions)

    def assign_member_permissions(self):
      
        content_type = ContentType.objects.get_for_model(UserLog)

     
        member_permissions = Permission.objects.filter(content_type=content_type).filter(
            codename__in=['can_edit_logs'])
        self.user.user_permissions.add(*member_permissions)

    class Meta:
        permissions = [
            ('can_edit_logs', 'Can edit logs'),
            ('can_delete_logs', 'Can delete logs'),
        ]

def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{filename}'

class Profile(models.Model):
   
    profile_picture = models.ImageField(upload_to=user_directory_path, default='profile_pics/default.jpg', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()