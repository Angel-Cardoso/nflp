from django import forms
from .models import Equipos
from .models import Jugadores
from .models import Estadios
from .models import Asientos
from .models import Fanaticos
from .models import Palcos
from .models import Contrato_Palco
from .models import Reportes

class FormRegEquipo(forms.ModelForm):
	class Meta:
		model = Equipos
		fields = ["nombre_equipo", "fecha_creacion", "cd", "fundador",
		"director"]
			
class FormRegJugador(forms.ModelForm):
	class Meta:
		model = Jugadores
		fields = ["nombre_jugador", "edad", "posicion", "equipo"]

class FormRegEstadio(forms.ModelForm):
	class Meta:
		model = Estadios
		fields = ["nombre_estadio", "fecha_construccion", "direccion", 
		"propietario"]

class FormRegFanatico(forms.ModelForm):
	class Meta:
		model = Fanaticos
		fields = ["nombre_fanatico", "fecha_nacimiento", "equipo_fanatico", 
		"edad", "numero_cel", "palco"]

class FormRegAsiento(forms.ModelForm):
	class Meta:
		model = Asientos
		fields = ["numero_asiento", "categoria", "estadio"]

class FormRegPalco(forms.ModelForm):
	class Meta:
		model = Palcos
		fields = ["numero_palco", "categoria", "cantidad_asientos"]

class FormRegReporte(forms.ModelForm):
	class Meta:
		model = Reportes
		fields = ["descripcion", "nombre_fanatico", "numero_asiento"]
		
			
class FormRegContratoPalco(forms.ModelForm):
	class Meta:
		model = Contrato_Palco
		fields = ["numero_palco", "nombre_fanatico", "years_renta"]