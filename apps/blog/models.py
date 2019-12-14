from django.db import models

# Create your models here.


class Blog(models.Model):
    b_title = models.CharField(max_length=124, null=True, blank=True)
    b_user = models.IntegerField(null=True)
    b_content = models.CharField(max_length=400, null=True, blank=True)
    b_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blog'
