from django.db import models
from .usuario import Usuario
from .pSalud import PersonalSalud

class Paciente(models.Model):
    documento = models.CharField(primary_key=True, max_length = 10, unique=True)
    fecha_nac = models.DateField('Fecha Nacimiento')
    ciudad = models.CharField('Ciudad', max_length = 50)
    direccion = models.CharField('Dirección', max_length = 100)
    username = models.ForeignKey(Usuario, unique=True, related_name='paciente', on_delete=models.CASCADE)
    pSalud_documento = models.ForeignKey(PersonalSalud, related_name='paciente', on_delete=modelsfrom django.db import models
from .usuario import Usuario
from .pSalud import PersonalSalud

class Paciente(models.Model):
    documento = models.CharField(primary_key=True, max_length = 10, unique=True)
    fecha_nac = models.DateField('Fecha Nacimiento')
    ciudad = models.CharField('Ciudad', max_length = 50)
    direccion = models.CharField('Dirección', max_length = 100)
    username = models.ForeignKey(Usuario, unique=True, related_name='paciente', on_delete=models.CASCADE)
    pSalud_documento = models.ForeignKey(PersonalSalud, related_name='paciente', on_delete=models.CASCADE)