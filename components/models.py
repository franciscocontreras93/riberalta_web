# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class Adquisicion(models.Model):
    adquisicion = models.CharField(max_length=255, blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adquisicion'


class CaracterTitular(models.Model):
    id = models.AutoField(primary_key=True)
    caracter = models.CharField(max_length=255, blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caracter_titular'


class Conservacion(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conservacion'


class Construcciones19(models.Model):
    cod = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    plantas = models.IntegerField(blank=True, null=True)
    anyo = models.CharField(max_length=255, blank=True, null=True)
    conservacion = models.IntegerField(blank=True, null=True)
    uso = models.IntegerField(blank=True, null=True)
    superficie = models.FloatField(blank=True, null=True)
    dormitorios = models.IntegerField(blank=True, null=True)
    banyos = models.IntegerField(blank=True, null=True)
    revestimiento = models.IntegerField(blank=True, null=True)
    ascensores = models.BooleanField(blank=True, null=True)
    calefaccion = models.BooleanField(blank=True, null=True)
    aire = models.BooleanField(blank=True, null=True)
    escalera = models.BooleanField(blank=True, null=True)
    tanque = models.BooleanField(blank=True, null=True)
    lavanderia = models.BooleanField(blank=True, null=True)
    servicio = models.BooleanField(blank=True, null=True)
    sanitarios = models.BooleanField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'construcciones19'


class Construcciones20(models.Model):
    cod = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    plantas = models.IntegerField(blank=True, null=True)
    anyo = models.IntegerField(blank=True, null=True)
    conservacion = models.IntegerField(blank=True, null=True)
    uso = models.IntegerField(blank=True, null=True)
    superficie = models.FloatField(blank=True, null=True)
    dormitorios = models.IntegerField(blank=True, null=True)
    banyos = models.IntegerField(blank=True, null=True)
    revestimiento = models.IntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=32720, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'construcciones20'


class ConstruccionesPlantas19(models.Model):
    id_construccion = models.IntegerField(blank=True, null=True)
    id_planta = models.IntegerField(blank=True, null=True)
    cimiento = models.IntegerField(blank=True, null=True)
    estructura = models.IntegerField(blank=True, null=True)
    muros = models.IntegerField(blank=True, null=True)
    muros_ext = models.IntegerField(blank=True, null=True)
    muros_int = models.IntegerField(blank=True, null=True)
    cubierta = models.IntegerField(blank=True, null=True)
    pisos = models.IntegerField(blank=True, null=True)
    carpinteria = models.IntegerField(blank=True, null=True)
    anyo = models.CharField(max_length=255, blank=True, null=True)
    superficie = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'construcciones_plantas19'


class ConstruccionesPlantas20(models.Model):
    id_construccion = models.IntegerField(blank=True, null=True)
    id_planta = models.IntegerField(blank=True, null=True)
    cimiento = models.IntegerField(blank=True, null=True)
    estructura = models.IntegerField(blank=True, null=True)
    muros = models.IntegerField(blank=True, null=True)
    muros_ext = models.IntegerField(blank=True, null=True)
    muros_int = models.IntegerField(blank=True, null=True)
    cubierta = models.IntegerField(blank=True, null=True)
    pisos = models.IntegerField(blank=True, null=True)
    carpinteria = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'construcciones_plantas20'


class Departamentos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamentos'


class Distritos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distritos'


class DocumentoPropiedad(models.Model):
    documento = models.CharField(max_length=255, blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documento_propiedad'


class EdiCarpinteria(models.Model):
    id = models.AutoField(primary_key=True)
    material = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_carpinteria'


class EdiCimientos(models.Model):
    id = models.AutoField(primary_key=True)
    material = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_cimientos'


class EdiCubiertas(models.Model):
    id = models.AutoField(primary_key=True)
    material = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_cubiertas'


class EdiEstructura(models.Model):
    id = models.AutoField(primary_key=True)
    material = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_estructura'


class EdiMuros(models.Model):
    id = models.AutoField(primary_key=True)
    material = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_muros'


class EdiMurosExt(models.Model):
    id = models.AutoField(primary_key=True)
    material = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_muros_ext'


class EdiMurosInt(models.Model):
    id = models.AutoField(primary_key=True)
    material = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_muros_int'


class EdiPisos(models.Model):
    id = models.AutoField(primary_key=True)
    material = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edi_pisos'


class Ejevias(models.Model):
    manzana = models.IntegerField()
    nombre = models.CharField(max_length=255)
    geom = models.LineStringField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ejevias'


class Especiales(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especiales'


class Forma(models.Model):
    id = models.AutoField(primary_key=True)
    forma = models.CharField(max_length=255, blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forma'


class Imagenes(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.BinaryField(blank=True, null=True)
    terreno19 = models.CharField(max_length=255, blank=True, null=True)
    construccion19 = models.IntegerField(blank=True, null=True)
    terreno20 = models.CharField(max_length=255, blank=True, null=True)
    construccion20 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imagenes'


class Impuestos(models.Model):
    id = models.AutoField(primary_key=True)
    anyo = models.CharField(max_length=255, blank=True, null=True)
    terrenos19 = models.CharField(max_length=255, blank=True, null=True)
    terrenos20 = models.CharField(max_length=255, blank=True, null=True)
    pagado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'impuestos'


class Instalaciones(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instalaciones'


class Localidades(models.Model):
    id = models.AutoField(primary_key=True)
    municipio = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.IntegerField(blank=True, null=True)
    distrito = models.IntegerField(blank=True, null=True)
    provincia = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localidades'


class Manzanos(models.Model):
    manzana = models.IntegerField()
    superficie = models.FloatField(blank=True, null=True)
    perimetro = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manzanos'


class MaterialVia(models.Model):
    id = models.AutoField(primary_key=True)
    material = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material_via'


class Mejoras(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    superficie = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mejoras'


class Plantas(models.Model):
    id = models.AutoField(primary_key=True)
    planta = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plantas'


class Provincias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincias'


class Revestimiento(models.Model):
    id = models.AutoField(primary_key=True)
    revestimiento = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'revestimiento'


class Terrenos19(models.Model):
    codigo = models.CharField(unique=True, max_length=255)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    superficie = models.FloatField(blank=True, null=True)
    barrio = models.CharField(max_length=255, blank=True, null=True)
    via = models.ForeignKey('TipoVia', models.DO_NOTHING, db_column='via', blank=True, null=True)
    agua = models.BooleanField(blank=True, null=True)
    alcantarillado = models.BooleanField(blank=True, null=True)
    energia = models.BooleanField(blank=True, null=True)
    telefono = models.BooleanField(blank=True, null=True)
    transporte = models.BooleanField(blank=True, null=True)
    internet = models.BooleanField(blank=True, null=True)
    titular = models.ForeignKey('Titular', models.DO_NOTHING, db_column='titular', blank=True, null=True)
    topografia = models.ForeignKey('Topografia', models.DO_NOTHING, db_column='topografia', blank=True, null=True)
    forma = models.ForeignKey('Forma', models.DO_NOTHING, db_column='forma', blank=True, null=True)
    ubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='ubicacion', blank=True, null=True)
    frente = models.FloatField(blank=True, null=True)
    fondo = models.FloatField(blank=True, null=True)
    suptest = models.FloatField(blank=True, null=True)
    manzano = models.CharField(max_length=255, blank=True, null=True)
    predio = models.CharField(max_length=255, blank=True, null=True)
    subpredio = models.CharField(max_length=255, blank=True, null=True)
    norte = models.CharField(max_length=255, blank=True, null=True)
    sur = models.CharField(max_length=255, blank=True, null=True)
    este = models.CharField(max_length=255, blank=True, null=True)
    oeste = models.CharField(max_length=255, blank=True, null=True)
    base = models.CharField(max_length=255, blank=True, null=True)
    zona = models.ForeignKey('Zonas', models.DO_NOTHING, db_column='zona', blank=True, null=True)
    material_via = models.ForeignKey('MaterialVia', models.DO_NOTHING, db_column='material_via', blank=True, null=True)
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terrenos19'


class Terrenos20(models.Model):
    codigo = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    superficie = models.FloatField(blank=True, null=True)
    barrio = models.CharField(max_length=255, blank=True, null=True)
    via = models.IntegerField(blank=True, null=True)
    agua = models.BooleanField(blank=True, null=True)
    alcantarillado = models.BooleanField(blank=True, null=True)
    energia = models.BooleanField(blank=True, null=True)
    telefono = models.BooleanField(blank=True, null=True)
    transporte = models.BooleanField(blank=True, null=True)
    internet = models.BooleanField(blank=True, null=True)
    titular = models.IntegerField(blank=True, null=True)
    topografia = models.IntegerField(blank=True, null=True)
    forma = models.IntegerField(blank=True, null=True)
    ubicacion = models.IntegerField(blank=True, null=True)
    frente = models.CharField(max_length=255, blank=True, null=True)
    fondo = models.CharField(max_length=255, blank=True, null=True)
    suptest = models.CharField(max_length=255, blank=True, null=True)
    manzano = models.CharField(max_length=255, blank=True, null=True)
    predio = models.CharField(max_length=255, blank=True, null=True)
    subpredio = models.CharField(max_length=255, blank=True, null=True)
    norte = models.CharField(max_length=255, blank=True, null=True)
    sur = models.CharField(max_length=255, blank=True, null=True)
    este = models.CharField(max_length=255, blank=True, null=True)
    oeste = models.CharField(max_length=255, blank=True, null=True)
    base = models.CharField(max_length=255, blank=True, null=True)
    geom = models.MultiPolygonField(srid=32720, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terrenos20'


class TerrenosEspeciales19(models.Model):
    codigo = models.CharField(max_length=255, blank=True, null=True)
    id_esp = models.IntegerField(blank=True, null=True)
    cimiento = models.IntegerField(blank=True, null=True)
    estructura = models.IntegerField(blank=True, null=True)
    muros = models.IntegerField(blank=True, null=True)
    muros_ext = models.IntegerField(blank=True, null=True)
    muros_int = models.IntegerField(blank=True, null=True)
    cubierta = models.IntegerField(blank=True, null=True)
    pisos = models.IntegerField(blank=True, null=True)
    carpinteria = models.IntegerField(blank=True, null=True)
    anyo = models.CharField(max_length=255, blank=True, null=True)
    conservacion = models.IntegerField(blank=True, null=True)
    superficie = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terrenos_especiales19'


class TerrenosEspeciales20(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    id_esp = models.IntegerField(blank=True, null=True)
    cimiento = models.IntegerField(blank=True, null=True)
    estructura = models.IntegerField(blank=True, null=True)
    muros = models.IntegerField(blank=True, null=True)
    muros_ext = models.IntegerField(blank=True, null=True)
    muros_int = models.IntegerField(blank=True, null=True)
    cubierta = models.IntegerField(blank=True, null=True)
    pisos = models.IntegerField(blank=True, null=True)
    carpinteria = models.IntegerField(blank=True, null=True)
    plantas = models.IntegerField(blank=True, null=True)
    anyo = models.IntegerField(blank=True, null=True)
    conservacion = models.IntegerField(blank=True, null=True)
    uso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terrenos_especiales20'


class TerrenosMejoras19(models.Model):
    codigo = models.CharField(max_length=255, blank=True, null=True)
    id_mejora = models.IntegerField(blank=True, null=True)
    cimiento = models.IntegerField(blank=True, null=True)
    estructura = models.IntegerField(blank=True, null=True)
    muros = models.IntegerField(blank=True, null=True)
    muros_ext = models.IntegerField(blank=True, null=True)
    muros_int = models.IntegerField(blank=True, null=True)
    cubierta = models.IntegerField(blank=True, null=True)
    pisos = models.IntegerField(blank=True, null=True)
    carpinteria = models.IntegerField(blank=True, null=True)
    anyo = models.CharField(max_length=255, blank=True, null=True)
    conservacion = models.IntegerField(blank=True, null=True)
    superficie = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terrenos_mejoras19'


class TerrenosMejoras20(models.Model):
    codigo = models.CharField(max_length=255, blank=True, null=True)
    id_mejora = models.IntegerField(blank=True, null=True)
    cimiento = models.IntegerField(blank=True, null=True)
    estructura = models.IntegerField(blank=True, null=True)
    muros = models.IntegerField(blank=True, null=True)
    muros_ext = models.IntegerField(blank=True, null=True)
    muros_int = models.IntegerField(blank=True, null=True)
    cubierta = models.IntegerField(blank=True, null=True)
    pisos = models.IntegerField(blank=True, null=True)
    carpinteria = models.IntegerField(blank=True, null=True)
    plantas = models.IntegerField(blank=True, null=True)
    anyo = models.IntegerField(blank=True, null=True)
    conservacion = models.IntegerField(blank=True, null=True)
    uso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terrenos_mejoras20'


class TipoConstruccion(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_construccion'


class TipoDocumento(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class TipoVia(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_via'


class Titular(models.Model):
    # id = models.AutoField(primary_key=False)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apellidos = models.CharField(max_length=255, blank=True, null=True)
    documento = models.IntegerField(primary_key=True)
    tipo_doc = models.ForeignKey(TipoDocumento, models.DO_NOTHING, db_column='tipo_doc', blank=True, null=True)
    caracter = models.ForeignKey(CaracterTitular, models.DO_NOTHING, db_column='caracter', blank=True, null=True)
    documento_prop = models.ForeignKey(DocumentoPropiedad, models.DO_NOTHING, db_column='documento_prop', blank=True, null=True)
    adquisicion = models.ForeignKey(Adquisicion, models.DO_NOTHING, db_column='adquisicion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titular'


class Topografia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topografia'


class Ubicacion(models.Model):
    id = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ubicacion'


class Uso(models.Model):
    id = models.AutoField(primary_key=True)
    uso = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uso'


class Zonas(models.Model):
    id = models.AutoField(primary_key=True)
    valor_comercial = models.FloatField(blank=True, null=True)
    valor_catastral = models.FloatField(blank=True, null=True)
    etiqueta = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zonas'


class Zonificacion(models.Model):
    clase = models.CharField(max_length=3, blank=True, null=True)
    subclase = models.SmallIntegerField(blank=True, null=True)
    valor_comercial = models.FloatField(blank=True, null=True)
    valor_catastral = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zonificacion'


class Terrenosvista19(models.Model):
    id = models.BigIntegerField(blank=True, primary_key=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    superficie = models.FloatField(blank=True, null=True)
    barrio = models.CharField(max_length=255, blank=True, null=True)
    via = models.IntegerField(blank=True, null=True)
    agua = models.BooleanField(blank=True, null=True)
    alcantarillado = models.BooleanField(blank=True, null=True)
    energia = models.BooleanField(blank=True, null=True)
    telefono = models.BooleanField(blank=True, null=True)
    transporte = models.BooleanField(blank=True, null=True)
    internet = models.BooleanField(blank=True, null=True)
    titular = models.IntegerField(blank=True, null=True)
    topografia = models.IntegerField(blank=True, null=True)
    forma = models.IntegerField(blank=True, null=True)
    ubicacion = models.IntegerField(blank=True, null=True)
    frente = models.FloatField(blank=True, null=True)
    fondo = models.FloatField(blank=True, null=True)
    suptest = models.FloatField(blank=True, null=True)
    manzano = models.CharField(max_length=255, blank=True, null=True)
    predio = models.CharField(max_length=255, blank=True, null=True)
    subpredio = models.CharField(max_length=255, blank=True, null=True)
    norte = models.CharField(max_length=255, blank=True, null=True)
    sur = models.CharField(max_length=255, blank=True, null=True)
    este = models.CharField(max_length=255, blank=True, null=True)
    oeste = models.CharField(max_length=255, blank=True, null=True)
    base = models.CharField(max_length=255, blank=True, null=True)
    zona = models.IntegerField(blank=True, null=True)
    material_via = models.IntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apellidos = models.CharField(max_length=255, blank=True, null=True)
    documento = models.IntegerField(blank=True, null=True)
    tipo_doc = models.IntegerField(blank=True, null=True)
    caracter = models.IntegerField(blank=True, null=True)
    documento_prop = models.IntegerField(blank=True, null=True)
    adquisicion = models.IntegerField(blank=True, null=True)
    nombrecaracter = models.CharField(max_length=255, blank=True, null=True)
    codigocaracter = models.CharField(max_length=255, blank=True, null=True)
    nombreadquisicion = models.CharField(max_length=255, blank=True, null=True)
    codigoadquisicion = models.CharField(max_length=255, blank=True, null=True)
    codigodocumento = models.CharField(max_length=255, blank=True, null=True)
    tipodocumento = models.CharField(max_length=255, blank=True, null=True)
    codigodocumnetopropiedad = models.CharField(max_length=255, blank=True, null=True)
    documentopropiedad = models.CharField(max_length=255, blank=True, null=True)
    tipovia = models.CharField(max_length=255, blank=True, null=True)
    valorvia = models.FloatField(blank=True, null=True)
    nombretopo = models.CharField(max_length=255, blank=True, null=True)
    descrtopo = models.CharField(max_length=255, blank=True, null=True)
    valortopo = models.FloatField(blank=True, null=True)
    nombreforma = models.CharField(max_length=255, blank=True, null=True)
    codigoforma = models.CharField(max_length=255, blank=True, null=True)
    valorforma = models.FloatField(blank=True, null=True)
    nombreubicacion = models.CharField(max_length=255, blank=True, null=True)
    codigoubicacion = models.CharField(max_length=255, blank=True, null=True)
    valorubicacion = models.FloatField(blank=True, null=True)
    valorcatastralzona = models.FloatField(blank=True, null=True)
    idzona = models.IntegerField(blank=True, null=True)
    valorcomercialzona = models.FloatField(blank=True, null=True)
    materialvia = models.CharField(max_length=255, blank=True, null=True)
    valormaterialvial = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'terrenosvista19'