from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    class PostChoice(models.TextChoices):
        BOAST = 'B', ('Boast')
        ROAST = 'R', ('Roast')
    
    title = models.CharField(max_length=280)
    boast_roast = models.CharField(max_length=1, choices=PostChoice.choices, default=PostChoice.BOAST)
    up_field = models.IntegerField(default=0)
    down_field = models.IntegerField(default=0)
    votes = models.IntegerField(default=0, null=True, blank=True, editable=False)
    post_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.votes = self.up_field - self.down_field
        super(Post, self).save()
    
    def __str__(self):
        return self.title