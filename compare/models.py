from django.db import models

class UploadFile(models.Model):
	file = models.FileField(upload_to='files/input')


class UploadFile1(models.Model):
	file = models.FileField(upload_to='files/output')
