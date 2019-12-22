from django.db import models
from filer.fields.file import FilerFileField

class DocumentAuthor(models.Model):
  forename = models.CharField(max_length=60)
  surname = models.CharField(max_length=60)
  position = models.CharField(max_length=120)
  email = models.EmailField(max_length=254, blank=True)
  tel = models.CharField(max_length=20, blank=True)

  def __str__(self):
      return self.forename + ' ' + self.surname
  
  class Meta:
      verbose_name = 'Author'
      verbose_name_plural = 'Authors'

class DocumentCategory(models.Model):
  category = models.CharField(max_length=70)

  def __str__(self):
      return self.category
  
  class Meta:
      verbose_name = "Category"
      verbose_name_plural = "Category"

class Document(models.Model):
  title = models.CharField(max_length=255)
  pub_date = models.CharField("Publication Date", max_length=50)
  category = models.ForeignKey("DocumentCategory", on_delete=models.CASCADE)
  document = FilerFileField(on_delete=models.CASCADE, null=True)

  def __str__(self):
      return self.title
