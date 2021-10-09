from django.db import models
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver

def file_upload_path(instance, filename):
	return "uploads/{0}/{1}".format(instance.document_type.name, filename)

class Artist(models.Model):
	name = models.CharField(max_length = 200, unique = True)

	def __str__(self):
		return self.name

class DocumentType(models.Model):
	name = models.CharField(max_length = 200, unique = True)

	class Meta:
		verbose_name = "Document Type"

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length = 200, unique = True)
	
	def __str__(self):
		return self.name

class Document(models.Model):
	title = models.CharField(max_length = 200)
	file = models.FileField(upload_to = file_upload_path)
	document_type = models.ForeignKey(DocumentType, on_delete = models.CASCADE)
	date = models.DateField(null = True, blank = True)
	artist = models.ForeignKey(Artist, on_delete = models.CASCADE, null = True, blank = True)
	tags = models.ManyToManyField(Tag, blank = True)
	notes = models.TextField(blank = True)

	def __str__(self):
		return self.title