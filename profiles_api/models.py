from django.db import models
# from django.contrib.auth.models import User


class UserProfile(models.Model):
    """ Creating User profile """

    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, unique=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # pip install pillow to use this
    # profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    # class Meta:
        # ordering = ['-id']

    def __str__(self):
        """ Shows the built-in User Name """
        return self.name


class ProfileFeedItem(models.Model):
    """ Profile status update """

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Shows the status_text """
        return self.status_text

