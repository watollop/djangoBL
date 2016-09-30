from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
    title =models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __unicode__(self):
        return self.title

    def get_absolut_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})
        #return "post/%s/" %(self.id)
