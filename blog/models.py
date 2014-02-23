from django.db import models
import time

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=250, blank=True)
	date = models.DateField(default=time.strftime("%Y-%m-%d"))
	content = models.TextField(blank=True)
	author = models.CharField(max_length=50, blank=True)

	class Meta:
		ordering = ['-date']

	def __unicode__(self):
		return self.title