from django.db import models
from djongo.models import ObjectIdField, DjongoManager

class Document(models.Model):
    id = ObjectIdField()  
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    original_content = models.TextField(blank=True)  
    positional_index = models.JSONField(default=dict, blank=True)
    objects = DjongoManager() 

    def __str__(self):
        return self.title
    


