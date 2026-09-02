from django.db import models
from account.models import Users
from files.models import Files

class FileShare(models.Model):
    file = models.ForeignKey(Files, on_delete=models.CASCADE)
    shared_with = models.ForeignKey(Users, on_delete=models.CASCADE)
    permission = models.CharField(max_length=50)
    shared_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'fileshare'