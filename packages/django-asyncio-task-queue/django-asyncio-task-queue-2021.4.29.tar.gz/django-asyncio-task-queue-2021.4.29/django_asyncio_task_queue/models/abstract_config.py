from django.db import models


class AbstractConfig(models.Model):
    db_table = models.TextField(primary_key=True)
    enqueue_limit = models.IntegerField(default=42)
    is_debug = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)

    class Meta:
        abstract = True
