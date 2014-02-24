from django.db import models
from mptt.models import MPTTModel

class Food(models.Model):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children")

    def __unicode__(self):
        return self.title
        
        
class MPTTFood(MPTTModel):
    title = models.CharField(max_length = 50)
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children")

    # class MPTTMeta:
    #     parent_attr = 'parent_food'
    
    def __unicode__(self):
        return self.title
        
        
