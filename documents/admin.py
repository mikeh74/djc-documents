from django.contrib import admin
from .models import Document, DocumentCategory, DocumentAuthor

admin.site.register(Document)
admin.site.register(DocumentCategory)

class DocumentAuthorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'position')

admin.site.register(DocumentAuthor, DocumentAuthorAdmin)

