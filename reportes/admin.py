from django.contrib import admin

# Register your models here.
from .models import Estadios
from .models import Jugadores
from .models import Equipos
from .models import Fanaticos
from .models import Asientos
from .models import Palcos
from .models import Contrato_Palco
from .models import Asiento_Palco
from .models import Reportes

admin.site.register(Estadios)
admin.site.register(Jugadores)
admin.site.register(Equipos)
admin.site.register(Fanaticos)
admin.site.register(Asientos)
admin.site.register(Palcos)
admin.site.register(Contrato_Palco)
admin.site.register(Asiento_Palco)
admin.site.register(Reportes)