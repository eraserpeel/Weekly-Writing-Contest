from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from allauth.account.models import EmailAddress

@receiver(user_signed_up)
def create_profile(sender, sociallogin=None, **kwargs):
    request = kwargs['request']
    user = kwargs['user']
    userprofile = UserProfile()
    print(sociallogin)
    if sociallogin != None:
        if sociallogin.account.provider == 'facebook':
            user.username = sociallogin.account.extra_data['name']
            user.save()
            userprofile.user = user
    else:
        userprofile.user = user
    
    userprofile.location = "Here"
    userprofile.website = "http://www.anonymous.com"
    userprofile.coins = 0
    userprofile.save()
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    location = models.CharField(max_length=100)
    website = models.URLField()
    coins = models.IntegerField(default=0)

    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])