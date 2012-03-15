import datetime
from django.db import models

class blog(models.Model):
	title = models.CharField(max_length=32)
	date = models.DateTimeField(auto_now_add= True)
	text = models.TextField()
