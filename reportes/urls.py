

from django.contrib import admin
from django.urls import path
from reportes import views

urlpatterns = [
	
	path('', views.nflp, name='nflp_views'),
	path('fanaticos_vip/', views.fanaticos_vip, name= 'fanaticos_vip_views'),
    path('fanaticos_list/', views.fanaticos_list_class.as_view(), name='fanaticos_views'),
    # path('fanaticos_list/', views.fanaticos_list, name='fanaticos_views'),
	path('estadios_list/', views.estadios_list, name ='estadios_views'),
    path('jugadores_list/', views.jugadores_list, name ='jugadores_views'),
    path('equipos_list/', views.equipos_list, name ='equipos_views'),
    path('asientos_list/', views.asientos_list, name = 'asientos_views'),
    path('palcos_list/', views.palcos_list, name='palcos_views'),
    path('contratos_palcos_list/', views.contratos_palcos_list, name='contratos_palcos_views'),
    path('reportes_list/', views.reportes_list.as_view(), name= 'reportes_views'),
    #Actualizar
    path('actualizar_fanatico/<int:pk>/', views.actualizar_fanatico.as_view(), name= 'actualizar_fanatico_views'),

    # Detalles
    path('detalle_jugador/<int:id>/', views.detalle_jugador, name ='detalle_jugador_views'),
    path('detalle_equipo/<int:id>/', views.detalle_equipo, name ='detalle_equipo_views'),
    path('detalle_estadio/<int:id>/', views.detalle_estadio, name ='detalle_estadio_views'),
    path('detalle_fanatico/<int:id>/', views.detalle_fanatico, name = 'detalle_fanatico_views'),
    path('detalle_palco_sr/<int:id>/', views.detalle_palco_sin_rentero, name='detalle_palco_sr_views'),
    path('detalle_palco/<int:id>/', views.detalle_palco, name= 'detalle_palco_views'),
    path('categoria_alta/', views.categoria_alta, name='categoria_alta_views'),
    path('categoria_media/', views.categoria_media, name='categoria_media_views'),
    path('categoria_baja/', views.categoria_baja, name='categoria_baja_views'),
    path('detalle_reporte/<int:id>/', views.detalle_reporte, name= 'detalle_reporte_views'),

    # Registros
    path('registrar_equipo/', views.registrar_equipo, name ='registrar_equipo_views'),
    path('registrar_jugador/', views.registrar_jugador, name ='registrar_jugador_views'),
    path('registrar_estadio/', views.registrar_estadio, name ='registrar_estadio_views'),
    path('registrar_fanatico/', views.registrar_fanatico, name ='registrar_fanatico_views'),
    path('registrar_asiento/', views.registrar_asiento, name ='registrar_asiento_views'),
    path('registrar_contrato/', views.registrar_contrato, name = 'registrar_contrato_views'),
    path('registrar_reporte/', views.registrar_reporte, name='registrar_reporte_views'),
]