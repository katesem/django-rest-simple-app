from django.db import models

# Create your models here.


STATUS_CHOICES = (
    (0, 'Planned'),
    (1, 'In progress'),
    (2, 'Done')
)

class Notes(models.Model):
    name = models.CharField(max_length = 60)
    status = models.IntegerField(default = 0, choices = STATUS_CHOICES)
    description = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    