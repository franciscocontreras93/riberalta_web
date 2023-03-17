from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from components.models import (
    CaracterTitular,
    Forma,
    MaterialVia, 
    Terrenos19, 
    DocumentoPropiedad, 
    Adquisicion, 
    TipoDocumento,
    TipoVia,
    Titular,
    Topografia,
    Zonas,
    Ubicacion,
    TipoVia
)
from components.forms import (
    TitularForm
)
from django.db import connection

from django.template.defaulttags import register

# Create your views here.

class ComponentView(TemplateView):
    pass

def MapView(request):
    terrenos = Terrenos19.objects.filter(titular__isnull=True) 
    terrenos = serialize('geojson',terrenos,geometry_field='geom')

    return render(request,'components/maps/maps-leaflet.html',{
        'terrenos': terrenos
    })

def MapViewInspect(request,cod):
    terreno = Terrenos19.objects.get(codigo=cod)
    terrenos = Terrenos19.objects.filter(codigo=cod)
    terrenos = serialize('geojson',terrenos,geometry_field='geom')
    doc_propiedad = [[p['id'],p['documento'],p['codigo']]for p in DocumentoPropiedad.objects.all().order_by('id').values('id','documento','codigo')]
    adquisicion = [[p['id'],p['adquisicion'],p['codigo']]for p in Adquisicion.objects.all().order_by('id').values('id','adquisicion','codigo')]
    tipo_doc = [[p['id'],p['tipo']] for p in TipoDocumento.objects.all().order_by('id').values('id','tipo')]
    caracter = [[p['id'],p['caracter']] for p in CaracterTitular.objects.all().values('id','caracter')]
    datos_terreno = terreno.codigo.split('.')
    zonas = [[p['id'],p['etiqueta']] for p in Zonas.objects.all().values('id','etiqueta')]
    topo = [[p['id'],p['nombre'],p['descripcion']] for p in Topografia.objects.all().values('id','nombre','descripcion')]
    ubicacion = [[p['id'],p['ubicacion']] for p in Ubicacion.objects.all().values('id','ubicacion')]
    calzada = [[p['id'],p['material']] for p in MaterialVia.objects.all().values('id','material')]
    tipo_via = [[p['id'],p['tipo']] for p in TipoVia.objects.all().values('id','tipo')]
    forma = [[p['id'],p['forma']] for p in Forma.objects.all().values('id','forma')]

    return render(request,'components/maps/maps-inspect.html',{
        'terrenos': terrenos,
        'codigo_catastral': cod,
        'datos_terreno': datos_terreno,
        'titular' : terreno.titular,
        'tipo_doc' : tipo_doc,
        'doc_propiedad': doc_propiedad,
        'adquisicion': adquisicion,
        'caracter' : caracter,
        'zonas':zonas,
        'topo':topo,
        'ubicacion':ubicacion,
        'calzada': calzada,
        'tipo_via': tipo_via,
        'forma': forma
    })

def Form(request,cod):
    terreno = Terrenos19.objects.get(codigo=cod)
    doc_propiedad = [[p['id'],p['documento'],p['codigo']]for p in DocumentoPropiedad.objects.all().values('id','documento','codigo')]
    adquisicion = [[p['id'],p['adquisicion'],p['codigo']]for p in Adquisicion.objects.all().values('id','adquisicion','codigo')]
    tipo_doc = [[p['id'],p['tipo']] for p in TipoDocumento.objects.all().values('id','tipo')]
    caracter = [[p['id'],p['caracter']] for p in CaracterTitular.objects.all().values('id','caracter')]
    datos_terreno = terreno.codigo.split('.')
    zonas = [[p['id'],p['etiqueta']] for p in Zonas.objects.all().values('id','etiqueta')]
    topo = [[p['id'],p['nombre'],p['descripcion']] for p in Topografia.objects.all().values('id','nombre','descripcion')]
    ubicacion = [[p['id'],p['ubicacion']] for p in Ubicacion.objects.all().values('id','ubicacion')]
    calzada = [[p['id'],p['material']] for p in MaterialVia.objects.all().values('id','material')]
    tipo_via = [[p['id'],p['tipo']] for p in TipoVia.objects.all().values('id','tipo')]
    forma = [[p['id'],p['forma']] for p in Forma.objects.all().values('id','forma')]
    
    return render(request,"components/forms/forms-wizard.html",{
        'codigo_catastral' : terreno.codigo,
        'datos_terreno': datos_terreno,
        'titular' : terreno.titular,
        'tipo_doc' : tipo_doc,
        'doc_propiedad': doc_propiedad,
        'adquisicion': adquisicion,
        'caracter' : caracter,
        'zonas':zonas,
        'topo':topo,
        'ubicacion':ubicacion,
        'calzada': calzada,
        'tipo_via': tipo_via,
        'forma': forma
    })

def FormTest(request): 
    form = TitularForm() 

    return render(request,"components/forms/forms-wizard.html",{
        'titular_form':form
    })
    # return HttpResponse('Hola')

def TestForm(request): 

    return HttpResponse()

def saveDatosTerreno(request):
    if request.method == 'POST':
       
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        documento = request.POST.get('documento')
        tipo_doc = TipoDocumento.objects.get(id=request.POST.get('tipo_documento'))
        caracter = CaracterTitular.objects.get(id=request.POST.get('titularidad'))
        documento_prop = DocumentoPropiedad.objects.get(id=request.POST.get('documento_propiedad'))
        adquisicion = Adquisicion.objects.get(id=request.POST.get('adquisicion'))

        # print(documento[0])
        titular = Titular(
            nombre = nombre,
            apellidos = apellidos,
            documento = documento,
            tipo_doc =  tipo_doc,
            caracter =  caracter,
            documento_prop = documento_prop,
            adquisicion = adquisicion
            )
        
        # cod_catastral = request.POST.get('cod_catastral')
        titular.save()

        
        terreno = Terrenos19.objects.get(codigo=request.POST.get('cod_catastral'))
        terreno.direccion = request.POST.get('direccion')
        terreno.barrio = request.POST.get('barrio')
        terreno.via = TipoVia.objects.get(id=request.POST.get('tipo_via'))
        terreno.agua = request.POST.get('agua_potable','') == 'on'
        terreno.alcantarillado = request.POST.get('alcantarillado','') == 'on'
        terreno.energia = request.POST.get('electricidad','') == 'on'
        terreno.telefono = request.POST.get('telefono','') == 'on'
        terreno.transporte = request.POST.get('transporte','') == 'on'
        terreno.internet = request.POST.get('internet','') == 'on'
        terreno.titular = Titular.objects.get(documento=request.POST.get('documento'))
        terreno.topografia = Topografia.objects.get(id=request.POST.get('topo_terreno'))
        terreno.forma = Forma.objects.get(id=request.POST.get('forma'))
        terreno.ubicacion = Ubicacion.objects.get(id=request.POST.get('ubi_terreno'))
        terreno.frente = request.POST.get('frente')
        terreno.fondo = request.POST.get('fondo')
        terreno.suptest = request.POST.get('sup_test')
        terreno.manzano = request.POST.get('manzano')
        terreno.predio = request.POST.get('predio')
        terreno.subpredio = request.POST.get('subpredio')
        terreno.base  = request.POST.get('base')
        terreno.zona = Zonas.objects.get(id=request.POST.get('zona'))
        terreno.material_via = MaterialVia.objects.get(id=request.POST.get('calzada'))

        # terreno.geom = terreno.geom

        

        terreno.save()
        
        return redirect('/')

@register.filter
def get_item(dict,key): 
    return dict.get(key)




#  Base UI
base_ui_alerts_view = ComponentView.as_view(template_name="components/base-ui/ui-alerts.html")
base_ui_badges_view = ComponentView.as_view(template_name="components/base-ui/ui-badges.html")
base_ui_buttons_view = ComponentView.as_view(template_name="components/base-ui/ui-buttons.html")
base_ui_colors_view = ComponentView.as_view(template_name="components/base-ui/ui-colors.html")
base_ui_cards_view = ComponentView.as_view(template_name="components/base-ui/ui-cards.html")
base_ui_carousel_view = ComponentView.as_view(template_name="components/base-ui/ui-carousel.html")
base_ui_dropdowns_view = ComponentView.as_view(template_name="components/base-ui/ui-dropdowns.html")
base_ui_grid_view = ComponentView.as_view(template_name="components/base-ui/ui-grid.html")
base_ui_images_view = ComponentView.as_view(template_name="components/base-ui/ui-images.html")
base_ui_tabs_view = ComponentView.as_view(template_name="components/base-ui/ui-tabs.html")
base_ui_accordions_view = ComponentView.as_view(template_name="components/base-ui/ui-accordions.html")
base_ui_modals_view = ComponentView.as_view(template_name="components/base-ui/ui-modals.html")
base_ui_offcanvas_view = ComponentView.as_view(template_name="components/base-ui/ui-offcanvas.html")
base_ui_placeholders_view = ComponentView.as_view(template_name="components/base-ui/ui-placeholders.html")
base_ui_progress_view = ComponentView.as_view(template_name="components/base-ui/ui-progress.html")
base_ui_notifications_view = ComponentView.as_view(template_name="components/base-ui/ui-notifications.html")
base_ui_media_view = ComponentView.as_view(template_name="components/base-ui/ui-media.html")
base_ui_embed_video_view = ComponentView.as_view(template_name="components/base-ui/ui-embed-video.html")
base_ui_typography_view = ComponentView.as_view(template_name="components/base-ui/ui-typography.html")
base_ui_lists_view = ComponentView.as_view(template_name="components/base-ui/ui-lists.html")
base_ui_general_view = ComponentView.as_view(template_name="components/base-ui/ui-general.html")
base_ui_ribbons_view = ComponentView.as_view(template_name="components/base-ui/ui-ribbons.html")
base_ui_utilities_view = ComponentView.as_view(template_name="components/base-ui/ui-utilities.html")
# Advance UI
adance_ui_sweetalerts_view = ComponentView.as_view(template_name="components/advance-ui/advance-ui-sweetalerts.html")
adance_ui_nestable_view = ComponentView.as_view(template_name="components/advance-ui/advance-ui-nestable.html")
adance_ui_scrollbar_view = ComponentView.as_view(template_name="components/advance-ui/advance-ui-scrollbar.html")
adance_ui_animation_view = ComponentView.as_view(template_name="components/advance-ui/advance-ui-animation.html")
adance_ui_tour_view = ComponentView.as_view(template_name="components/advance-ui/advance-ui-tour.html")
adance_ui_swiper_view = ComponentView.as_view(template_name="components/advance-ui/advance-ui-swiper.html")
adance_ui_ratings_view = ComponentView.as_view(template_name="components/advance-ui/advance-ui-ratings.html")
adance_ui_highlight_view = ComponentView.as_view(template_name="components/advance-ui/advance-ui-highlight.html")
adance_ui_scrollspy_view = ComponentView.as_view(template_name="components/advance-ui/advance-ui-scrollspy.html")
# Widgets
widgets_view=ComponentView.as_view(template_name="components/widgets.html")
# Forms
forms_elements_view=ComponentView.as_view(template_name="components/forms/forms-elements.html")
forms_select_view=ComponentView.as_view(template_name="components/forms/forms-select.html")
forms_checkboxs_radios_view=ComponentView.as_view(template_name="components/forms/forms-checkboxs-radios.html")
forms_pickers_view=ComponentView.as_view(template_name="components/forms/forms-pickers.html")
forms_masks_view=ComponentView.as_view(template_name="components/forms/forms-masks.html")
forms_advanced_view=ComponentView.as_view(template_name="components/forms/forms-advanced.html")
forms_range_sliders_view=ComponentView.as_view(template_name="components/forms/forms-range-sliders.html")
forms_validation_view=ComponentView.as_view(template_name="components/forms/forms-validation.html")
forms_wizard_view=ComponentView.as_view(template_name="components/forms/forms-wizard.html")
forms_editors_view=ComponentView.as_view(template_name="components/forms/forms-editors.html")
forms_file_uploads_view=ComponentView.as_view(template_name="components/forms/forms-file-uploads.html")
forms_layouts_view=ComponentView.as_view(template_name="components/forms/forms-layouts.html")
forms_select2_view = ComponentView.as_view(template_name="components/forms/forms-select2.html")
# Tables
tables_basic_view=ComponentView.as_view(template_name="components/tables/tables-basic.html")
tables_gridjs_view=ComponentView.as_view(template_name="components/tables/tables-gridjs.html")
tables_listjs_view=ComponentView.as_view(template_name="components/tables/tables-listjs.html")
tables_datatables_view=ComponentView.as_view(template_name="components/tables/tables-datatables.html")
# Charts
# Apex Charts
charts_apex_charts_line_view=ComponentView.as_view(template_name="components/charts/apex-charts/charts-apex-line.html")
charts_apex_charts_area_view=ComponentView.as_view(template_name="components/charts/apex-charts/charts-apex-area.html")
charts_apex_charts_column_view=ComponentView.as_view(template_name="components/charts/apex-charts/charts-apex-column.html")
charts_apex_charts_bar_view=ComponentView.as_view(template_name="components/charts/apex-charts/charts-apex-bar.html")
charts_apex_charts_mixed_view=ComponentView.as_view(template_name="components/charts/apex-charts/charts-apex-mixed.html")
charts_apex_charts_timeline_view=ComponentView.as_view(template_name="components/charts/apex-charts/charts-apex-timeline.html")
charts_apex_charts_candlestick_view=ComponentView.as_view(template_name="components/charts/apex-charts/charts-apex-candlestick.html")
charts_apex_charts_boxplot_view=ComponentView.as_view(template_name="components/charts/apex-charts/charts-apex-boxplot.html")
charts_apex_charts_bubble_view=ComponentView.as_view(template_name="components/charts/apex-charts/charts-apex-bubble.html")
charts_apex_charts_scatter_view=ComponentView.as_view(template_name="components/charts/apex-charts/charts-apex-scatter.html")
charts_apex_charts_heatmap_view=ComponentView.as_view(template_name="components/charts/apex-charts/charts-apex-heatmap.html")
charts_apex_charts_treemap_view=ComponentView.as_view(template_name="components/charts/apex-charts/charts-apex-treemap.html")
charts_apex_charts_pie_view=ComponentView.as_view(template_name="components/charts/apex-charts/charts-apex-pie.html")
charts_apex_charts_radialbar_view=ComponentView.as_view(template_name="components/charts/apex-charts/charts-apex-radialbar.html")
charts_apex_charts_radar_view=ComponentView.as_view(template_name="components/charts/apex-charts/charts-apex-radar.html")
charts_apex_charts_polar_view=ComponentView.as_view(template_name="components/charts/apex-charts/charts-apex-polar.html")
    # Chart JS
charts_chartjs_view=ComponentView.as_view(template_name="components/charts/charts-chartjs.html")
    # Echart
charts_echarts_view=ComponentView.as_view(template_name="components/charts/charts-echarts.html")
# Icons
icons_remix_view=ComponentView.as_view(template_name="components/icons/icons-remix.html")
icons_boxicons_view=ComponentView.as_view(template_name="components/icons/icons-boxicons.html")
icons_materialdesign_view=ComponentView.as_view(template_name="components/icons/icons-materialdesign.html")
icons_lineawesome_view=ComponentView.as_view(template_name="components/icons/icons-lineawesome.html")
icons_feather_view=ComponentView.as_view(template_name="components/icons/icons-feather.html")
icons_crypto_view=ComponentView.as_view(template_name="components/icons/icons-crypto.html")
# Maps
maps_google_view=ComponentView.as_view(template_name="components/maps/maps-google.html")
maps_vector_view=ComponentView.as_view(template_name="components/maps/maps-vector.html")
maps_leaflet_view=ComponentView.as_view(template_name="components/maps/maps-leaflet.html")