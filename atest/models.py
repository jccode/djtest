from django.db import models

class Food(models.Model):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children")

    def __unicode__(self):
        return self.title
        
        
        
