from django.db import models
from account.models import Users
from files.models import Files

# Create your models here.
class Trash(models.Model):
    file = models.ForeignKey(Files, on_delete=models.CASCADE)
    deleted_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Trash'