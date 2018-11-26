from django.db import models

class Equipos(models.Model):
	nombre_equipo = models.CharField(max_length = 40)
	fecha_creacion = models.DateTimeField()
	cd = models.CharField(max_length = 20)
	fundador = models.CharField(max_length = 30)
	director = models.CharField(max_length = 30)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_equipo)

class Jugadores(models.Model):
	nombre_jugador = models.CharField(max_length = 40)
	edad = models.IntegerField()
	posicion = models.CharField(max_length = 15)
	equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_jugador)

class Estadios(models.Model):
	nombre_estadio = models.CharField(max_length = 30)
	fecha_construccion = models.DateTimeField()
	direccion = models.CharField(max_length = 25)
	propietario = models.CharField(max_length = 30)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_estadio)

class Fanaticos(models.Model):
	nombre_fanatico = models.CharField(max_length = 40)
	fecha_nacimiento = models.DateTimeField()
	equipo_fanatico = models.ForeignKey(Equipos, on_delete=models.CASCADE)
	edad = models.IntegerField()
	palco = models.CharField(max_length = 10, default = 'sin palco')
	numero_cel = models.CharField(max_length = 15)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_fanatico)
		
class Asientos(models.Model):
	numero_asiento = models.IntegerField()
	estadio = models.ForeignKey(Estadios, on_delete=models.CASCADE, default = 'desconocido')
	categoria = models.CharField(max_length = 15, default = 'baja')
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.numero_asiento)

class Palcos(models.Model):
	numero_palco = models.IntegerField()
	categoria = models.CharField(max_length = 15, default = 'club')
	cantidad_asientos = models.IntegerField()
	estado = models.CharField(max_length=15, default = 'disponible')
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.numero_palco)

class Asiento_Palco(models.Model):
	numero_asiento = models.ForeignKey(Asientos, on_delete=models.CASCADE)
	numero_palco = models.ForeignKey(Palcos, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.id)

class Reportes(models.Model):
	descripcion = models.TextField()
	nombre_fanatico = models.ForeignKey(Fanaticos, on_delete=models.CASCADE)
	numero_asiento = models.ForeignKey(Asientos, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_fanatico)

class Contrato_Palco(models.Model):
	numero_palco = models.ForeignKey(Palcos, on_delete=models.CASCADE)
	nombre_fanatico = models.ForeignKey(Fanaticos, on_delete= models.CASCADE)
	years_renta = models.IntegerField(default= 10)
	def _get_precio(self):
		return self.years_renta*5000
	precio_total = property(_get_precio)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.id)
	
# Create your models here.
