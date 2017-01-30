from django.db import models
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
#from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Comment(models.Model):
    #content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    highlighted = models.TextField()
    
    class Meta:
        ordering = ['timestamp']

