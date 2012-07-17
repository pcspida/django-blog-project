from django.db import models
#from django.contrib import admin
from django.core.mail import send_mail
#from django.contrib.auth.models import User


# Create your models here.
from django.core.urlresolvers import reverse

class Post(models.Model):
    title=models.CharField(max_length=60)
    body=models.TextField()
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    def __unicode__(self):
        return self.title
    #@models.permalink
    def get_absolute_url(self):
        return '/blog/posts/%i/true' % self.id

class Comment(models.Model):
    
    body=models.TextField()
    author=models.CharField(max_length=60)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    post=models.ForeignKey(Post)
    def some_body(self):
        return self.body[:60]
    def __unicode__(self):
        return self.body

    def save(self, *args, **kwargs):
        """Email when a comment is added."""
        if "notify" in kwargs and kwargs["notify"] == True:
            message = "Comment was was added to '%s' by '%s': \n\n%s" % (self.post, self.author,
                                                                         self.body)
            from_addr = "no-reply@pcobby.com"
            recipient_list = ["pcobby@gmail.com"]
            send_mail("New comment added", message, from_addr, recipient_list)

        if "notify" in kwargs: del kwargs["notify"]
        super(Comment, self).save(*args, **kwargs)






