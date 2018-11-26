from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from .models import Jugadores
from .models import Estadios
from .models import Equipos
from .models import Fanaticos
from .models import Asientos
from .models import Palcos
from .models import Contrato_Palco
from .models import Asiento_Palco
from .models import Reportes
from .forms import FormRegEquipo
from .forms import FormRegJugador
from .forms import FormRegEstadio
from .forms import FormRegFanatico
from .forms import FormRegAsiento
from .forms import FormRegContratoPalco
from .forms import FormRegReporte


def nflp(request):
	return render(request, "reportes/nflp.html")

def categoria_alta(request):
	return render(request, "reportes/categoria_alta.html")

def categoria_media(request):
	return render(request, "reportes/categoria_media.html")

def categoria_baja(request):
	return render(request, "reportes/categoria_baja.html")

class fanaticos_list_class(generic.ListView):
	template_name = "reportes/fanaticos.html"
	queryset = Fanaticos.objects.all()
	def get_queryset(self, *args, **kwargs):
	 	qs = Fanaticos.objects.all()
	 	print(self.request.GET)
	 	query = self.request.GET.get("q",None)
	 	if query is not None:
	 		qs = qs.filter(Q(contrato_palco=query)| Q(nombre_fanatico__icontains=query))
	 	return qs

class reportes_list(generic.ListView):
	template_name = "reportes/reportes.html"
	queryset = Reportes.objects.all()

# def fanaticos_list(request):
# 	queryset = Fanaticos.objects.all()busquedas

# 	def get_queryset(self, *args, **kwargs):
# 		qs = Fanaticos.objects.all()
# 		print(self.request.GET)
# 		query = self.request.GET.get("q",None)
# 		if query is not None:
# 			qs = qs.filter(edad_icontains=query)
# 		return qs
# 	return render(request, "reportes/fanaticos.html",{ "Fanaticos" : queryset})

def fanaticos_vip(request):
	queryset = Fanaticos.objects.filter(palco='con palco')
	return render(request, "reportes/fanaticos_vip.html",{ "Fanaticos" : queryset})

def contratos_palcos_list(request):
	queryset = Contrato_Palco.objects.all()
	return render(request, "reportes/contratos_palcos.html",{ "Contratos_Palcos" : queryset})

def palcos_list(request):
	queryset = Palcos.objects.all()
	return render(request, "reportes/palcos.html",{ "Palcos" : queryset})

def estadios_list(request):
	queryset = Estadios.objects.all()
	return render(request, "reportes/estadios.html",{ "Estadios" : queryset})

def equipos_list(request):
	queryset = Equipos.objects.all()
	return render(request, "reportes/equipos.html", { "Equipos" : queryset})

def jugadores_list(request):
	queryset = Jugadores.objects.all()
	return render(request, "reportes/jugadores.html", { "Jugadores": queryset})

def detalle_jugador(request, id=1):
	queryset = Jugadores.objects.get(id=id)
	return render(request, "reportes/detalle_jugador.html", { "Detalle" : queryset})

def detalle_equipo(request, id=1):
	queryset = Equipos.objects.get(id=id)
	return render(request, "reportes/detalle_equipo.html", {"Detalle" : queryset})

def detalle_estadio(request, id=1):
	queryset = Estadios.objects.get(id=id)
	return render(request, "reportes/detalle_estadio.html", {"Detalle" : queryset})

def asientos_list(request):
	categoria_alta = Asientos.objects.filter(categoria= 'alta')
	categoria_media = Asientos.objects.filter(categoria= 'media')
	categoria_baja = Asientos.objects.filter(categoria= 'baja')
	contexto = {
	"CatBaj" : categoria_baja,
	"CatMed" : categoria_media,
	"CatAlt" : categoria_alta
	}
	return render(request, "reportes/asientos.html", contexto)

def detalle_fanatico(request, id=1):
	queryset = Fanaticos.objects.get(id=id)
	return render(request, "reportes/detalle_fanatico.html", {"Fanatico": queryset})

def detalle_reporte(request, id=1):
	queryset = Reportes.objects.get(id=id)
	return render(request, "reportes/detalle_reporte.html", {"Reporte": queryset})

def detalle_palco(request, id=1):
	asientos = Asiento_Palco.objects.filter(numero_palco=id)
	palco = Palcos.objects.get(id=id)
	rentero = (Contrato_Palco.objects.get(numero_palco=id))
	contexto = {
	"asientos" : asientos,
	"palco" : palco,
	"rentero" : rentero
	}
	return render(request, "reportes/detalle_palco.html", contexto)

def detalle_palco_sin_rentero(request, id=1):
	asientos = Asiento_Palco.objects.filter(numero_palco=id)
	palco = Palcos.objects.get(id=id)
	contexto = {
	"asientos" : asientos,
	"palco" : palco,
	}
	return render(request, "reportes/detalle_palco_sin_rentero.html", contexto)

def registrar_equipo(request):
	form = FormRegEquipo(request.POST or None)
	if request.user.is_authenticated:
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
	# equipo = {"form": form}
	return render(request, "reportes/registrar_equipo.html", {"form": form})

def registrar_jugador(request):
	form = FormRegJugador(request.POST or None)
	if request.user.is_authenticated:
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
	# equipo = {"form": form}
	return render(request, "reportes/registrar_jugador.html", {"form": form})

def registrar_estadio(request):
	form = FormRegEstadio(request.POST or None)
	if request.user.is_authenticated:
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
	# equipo = {"form": form}
	return render(request, "reportes/registrar_estadio.html", {"form": form})

def registrar_fanatico(request):
	form = FormRegFanatico(request.POST or None)
	if request.user.is_authenticated:
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
	return render(request, "reportes/registrar_fanatico.html", {"form": form})

def registrar_asiento(request):
	form = FormRegAsiento(request.POST or None)
	if request.user.is_authenticated:
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
	return render(request, "reportes/registrar_asiento.html", {"form": form})

def registrar_contrato(request):
	form = FormRegContratoPalco(request.POST or None)
	if request.user.is_authenticated:
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
	contexto = {
		"form": form,
	}
	return render(request, "reportes/registrar_contrato.html", contexto)


class actualizar_fanatico(generic.UpdateView):
	template_name = "reportes/actualizar_fanatico.html"
	model = Fanaticos
	fields = ["nombre_fanatico", "fecha_nacimiento", "equipo_fanatico", 
		"edad", "numero_cel", "palco"]
	success_url = "/fanaticos_list/"



def registrar_reporte(request):
	form = FormRegReporte(request.POST or None)
	if request.user.is_authenticated:
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
	success_url = "/fanaticos_list/"
	return render(request, "reportes/registrar_reporte.html", {"form": form})

# Create your views here.
