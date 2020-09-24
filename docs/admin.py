from django.contrib import admin
from django.utils.html import mark_safe

from .models import Artist
from .models import Document
from .models import DocumentType
from .models import Tag

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
	list_display = ["name"]
	ordering = ["name"]

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
	list_display = ["title", "file_link", "document_type", "date", "artist"]
	list_filter = ["artist", "document_type", "tags"]
	ordering = ["title", "artist__name"]
	search_fields = ["title", "artist__name", "tags__name"]

	def file_link(self, obj):
		if obj.file:
			return mark_safe("<a href=\"{0}\">Download</a>".format(obj.file.url))
		else:
			return "-"

	file_link.short_description = "File"

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
	list_display = ["name"]
	ordering = ["name"]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ["name"]
	ordering = ["name"]