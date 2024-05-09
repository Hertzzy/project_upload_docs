from django.db import models

# Create your models here.
class Document(models.Model):
    DOCUMENT_TYPE = (
        ('P', 'Prontuário'),
        ('R', 'Relatório'),
        ('A', 'Arquivo')
    )
    name = models.CharField(max_length=50)
    register = models.CharField(max_length=50)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    doc_type = models.CharField(max_length=1, choices=DOCUMENT_TYPE, blank=False, null=False,default='P')
    birthday = models.DateField(max_length=50)

    def __str__(self):
        return self.name
