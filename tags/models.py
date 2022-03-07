from django.db import models
from django.contrib.contenttypes.models import ContentType


class TaggedItem(models.Model):
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    """def get_related_object(self):
        klass = self.content_type.model_class()
        return klass.objects.get(id=self.object_id)"""