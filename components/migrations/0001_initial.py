# Generated by Django 4.1.7 on 2023-03-03 00:52

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adquisicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adquisicion', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'adquisicion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CaracterTitular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caracter', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'caracter_titular',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Conservacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'conservacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Construcciones19',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.IntegerField(blank=True, null=True)),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
                ('plantas', models.IntegerField(blank=True, null=True)),
                ('anyo', models.CharField(blank=True, max_length=255, null=True)),
                ('conservacion', models.IntegerField(blank=True, null=True)),
                ('uso', models.IntegerField(blank=True, null=True)),
                ('superficie', models.FloatField(blank=True, null=True)),
                ('dormitorios', models.IntegerField(blank=True, null=True)),
                ('banyos', models.IntegerField(blank=True, null=True)),
                ('revestimiento', models.IntegerField(blank=True, null=True)),
                ('ascensores', models.BooleanField(blank=True, null=True)),
                ('calefaccion', models.BooleanField(blank=True, null=True)),
                ('aire', models.BooleanField(blank=True, null=True)),
                ('escalera', models.BooleanField(blank=True, null=True)),
                ('tanque', models.BooleanField(blank=True, null=True)),
                ('lavanderia', models.BooleanField(blank=True, null=True)),
                ('servicio', models.BooleanField(blank=True, null=True)),
                ('sanitarios', models.BooleanField(blank=True, null=True)),
                ('tipo', models.IntegerField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=32719)),
            ],
            options={
                'db_table': 'construcciones19',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Construcciones20',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.IntegerField(blank=True, null=True)),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
                ('plantas', models.IntegerField(blank=True, null=True)),
                ('anyo', models.IntegerField(blank=True, null=True)),
                ('conservacion', models.IntegerField(blank=True, null=True)),
                ('uso', models.IntegerField(blank=True, null=True)),
                ('superficie', models.FloatField(blank=True, null=True)),
                ('dormitorios', models.IntegerField(blank=True, null=True)),
                ('banyos', models.IntegerField(blank=True, null=True)),
                ('revestimiento', models.IntegerField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=32720)),
            ],
            options={
                'db_table': 'construcciones20',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ConstruccionesPlantas19',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_construccion', models.IntegerField(blank=True, null=True)),
                ('id_planta', models.IntegerField(blank=True, null=True)),
                ('cimiento', models.IntegerField(blank=True, null=True)),
                ('estructura', models.IntegerField(blank=True, null=True)),
                ('muros', models.IntegerField(blank=True, null=True)),
                ('muros_ext', models.IntegerField(blank=True, null=True)),
                ('muros_int', models.IntegerField(blank=True, null=True)),
                ('cubierta', models.IntegerField(blank=True, null=True)),
                ('pisos', models.IntegerField(blank=True, null=True)),
                ('carpinteria', models.IntegerField(blank=True, null=True)),
                ('anyo', models.CharField(blank=True, max_length=255, null=True)),
                ('superficie', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'construcciones_plantas19',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ConstruccionesPlantas20',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_construccion', models.IntegerField(blank=True, null=True)),
                ('id_planta', models.IntegerField(blank=True, null=True)),
                ('cimiento', models.IntegerField(blank=True, null=True)),
                ('estructura', models.IntegerField(blank=True, null=True)),
                ('muros', models.IntegerField(blank=True, null=True)),
                ('muros_ext', models.IntegerField(blank=True, null=True)),
                ('muros_int', models.IntegerField(blank=True, null=True)),
                ('cubierta', models.IntegerField(blank=True, null=True)),
                ('pisos', models.IntegerField(blank=True, null=True)),
                ('carpinteria', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'construcciones_plantas20',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'departamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Distritos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'distritos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentoPropiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'documento_propiedad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EdiCarpinteria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('material', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'edi_carpinteria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EdiCimientos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('material', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'edi_cimientos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EdiCubiertas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('material', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'edi_cubiertas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EdiEstructura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('material', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'edi_estructura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EdiMuros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('material', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'edi_muros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EdiMurosExt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('material', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'edi_muros_ext',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EdiMurosInt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('material', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'edi_muros_int',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EdiPisos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('material', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'edi_pisos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ejevias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manzana', models.IntegerField()),
                ('nombre', models.CharField(max_length=255)),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(blank=True, null=True, srid=32719)),
            ],
            options={
                'db_table': 'ejevias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Especiales',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'especiales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Forma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('forma', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'forma',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.BinaryField(blank=True, null=True)),
                ('terreno19', models.CharField(blank=True, max_length=255, null=True)),
                ('construccion19', models.IntegerField(blank=True, null=True)),
                ('terreno20', models.CharField(blank=True, max_length=255, null=True)),
                ('construccion20', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'imagenes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Impuestos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('anyo', models.CharField(blank=True, max_length=255, null=True)),
                ('terrenos19', models.CharField(blank=True, max_length=255, null=True)),
                ('terrenos20', models.CharField(blank=True, max_length=255, null=True)),
                ('pagado', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'impuestos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Instalaciones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'instalaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Localidades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('municipio', models.CharField(blank=True, max_length=255, null=True)),
                ('departamento', models.IntegerField(blank=True, null=True)),
                ('distrito', models.IntegerField(blank=True, null=True)),
                ('provincia', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'localidades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manzanos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manzana', models.IntegerField()),
                ('superficie', models.FloatField(blank=True, null=True)),
                ('perimetro', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=32719)),
            ],
            options={
                'db_table': 'manzanos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MaterialVia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('material', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'material_via',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mejoras',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
                ('superficie', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'mejoras',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Plantas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('planta', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'plantas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'provincias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Revestimiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('revestimiento', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'revestimiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Terrenos19',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=255)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('superficie', models.FloatField(blank=True, null=True)),
                ('barrio', models.CharField(blank=True, max_length=255, null=True)),
                ('via', models.IntegerField(blank=True, null=True)),
                ('agua', models.BooleanField(blank=True, null=True)),
                ('alcantarillado', models.BooleanField(blank=True, null=True)),
                ('energia', models.BooleanField(blank=True, null=True)),
                ('telefono', models.BooleanField(blank=True, null=True)),
                ('transporte', models.BooleanField(blank=True, null=True)),
                ('internet', models.BooleanField(blank=True, null=True)),
                ('titular', models.IntegerField(blank=True, null=True)),
                ('topografia', models.IntegerField(blank=True, null=True)),
                ('forma', models.IntegerField(blank=True, null=True)),
                ('ubicacion', models.IntegerField(blank=True, null=True)),
                ('frente', models.FloatField(blank=True, null=True)),
                ('fondo', models.FloatField(blank=True, null=True)),
                ('suptest', models.FloatField(blank=True, null=True)),
                ('manzano', models.CharField(blank=True, max_length=255, null=True)),
                ('predio', models.CharField(blank=True, max_length=255, null=True)),
                ('subpredio', models.CharField(blank=True, max_length=255, null=True)),
                ('norte', models.CharField(blank=True, max_length=255, null=True)),
                ('sur', models.CharField(blank=True, max_length=255, null=True)),
                ('este', models.CharField(blank=True, max_length=255, null=True)),
                ('oeste', models.CharField(blank=True, max_length=255, null=True)),
                ('base', models.CharField(blank=True, max_length=255, null=True)),
                ('zona', models.IntegerField(blank=True, null=True)),
                ('material_via', models.IntegerField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=32719)),
            ],
            options={
                'db_table': 'terrenos19',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Terrenos20',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=255)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('superficie', models.FloatField(blank=True, null=True)),
                ('barrio', models.CharField(blank=True, max_length=255, null=True)),
                ('via', models.IntegerField(blank=True, null=True)),
                ('agua', models.BooleanField(blank=True, null=True)),
                ('alcantarillado', models.BooleanField(blank=True, null=True)),
                ('energia', models.BooleanField(blank=True, null=True)),
                ('telefono', models.BooleanField(blank=True, null=True)),
                ('transporte', models.BooleanField(blank=True, null=True)),
                ('internet', models.BooleanField(blank=True, null=True)),
                ('titular', models.IntegerField(blank=True, null=True)),
                ('topografia', models.IntegerField(blank=True, null=True)),
                ('forma', models.IntegerField(blank=True, null=True)),
                ('ubicacion', models.IntegerField(blank=True, null=True)),
                ('frente', models.CharField(blank=True, max_length=255, null=True)),
                ('fondo', models.CharField(blank=True, max_length=255, null=True)),
                ('suptest', models.CharField(blank=True, max_length=255, null=True)),
                ('manzano', models.CharField(blank=True, max_length=255, null=True)),
                ('predio', models.CharField(blank=True, max_length=255, null=True)),
                ('subpredio', models.CharField(blank=True, max_length=255, null=True)),
                ('norte', models.CharField(blank=True, max_length=255, null=True)),
                ('sur', models.CharField(blank=True, max_length=255, null=True)),
                ('este', models.CharField(blank=True, max_length=255, null=True)),
                ('oeste', models.CharField(blank=True, max_length=255, null=True)),
                ('base', models.CharField(blank=True, max_length=255, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=32720)),
            ],
            options={
                'db_table': 'terrenos20',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TerrenosEspeciales19',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
                ('id_esp', models.IntegerField(blank=True, null=True)),
                ('cimiento', models.IntegerField(blank=True, null=True)),
                ('estructura', models.IntegerField(blank=True, null=True)),
                ('muros', models.IntegerField(blank=True, null=True)),
                ('muros_ext', models.IntegerField(blank=True, null=True)),
                ('muros_int', models.IntegerField(blank=True, null=True)),
                ('cubierta', models.IntegerField(blank=True, null=True)),
                ('pisos', models.IntegerField(blank=True, null=True)),
                ('carpinteria', models.IntegerField(blank=True, null=True)),
                ('anyo', models.CharField(blank=True, max_length=255, null=True)),
                ('conservacion', models.IntegerField(blank=True, null=True)),
                ('superficie', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'terrenos_especiales19',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TerrenosEspeciales20',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
                ('id_esp', models.IntegerField(blank=True, null=True)),
                ('cimiento', models.IntegerField(blank=True, null=True)),
                ('estructura', models.IntegerField(blank=True, null=True)),
                ('muros', models.IntegerField(blank=True, null=True)),
                ('muros_ext', models.IntegerField(blank=True, null=True)),
                ('muros_int', models.IntegerField(blank=True, null=True)),
                ('cubierta', models.IntegerField(blank=True, null=True)),
                ('pisos', models.IntegerField(blank=True, null=True)),
                ('carpinteria', models.IntegerField(blank=True, null=True)),
                ('plantas', models.IntegerField(blank=True, null=True)),
                ('anyo', models.IntegerField(blank=True, null=True)),
                ('conservacion', models.IntegerField(blank=True, null=True)),
                ('uso', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'terrenos_especiales20',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TerrenosMejoras19',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
                ('id_mejora', models.IntegerField(blank=True, null=True)),
                ('cimiento', models.IntegerField(blank=True, null=True)),
                ('estructura', models.IntegerField(blank=True, null=True)),
                ('muros', models.IntegerField(blank=True, null=True)),
                ('muros_ext', models.IntegerField(blank=True, null=True)),
                ('muros_int', models.IntegerField(blank=True, null=True)),
                ('cubierta', models.IntegerField(blank=True, null=True)),
                ('pisos', models.IntegerField(blank=True, null=True)),
                ('carpinteria', models.IntegerField(blank=True, null=True)),
                ('anyo', models.CharField(blank=True, max_length=255, null=True)),
                ('conservacion', models.IntegerField(blank=True, null=True)),
                ('superficie', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'terrenos_mejoras19',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TerrenosMejoras20',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
                ('id_mejora', models.IntegerField(blank=True, null=True)),
                ('cimiento', models.IntegerField(blank=True, null=True)),
                ('estructura', models.IntegerField(blank=True, null=True)),
                ('muros', models.IntegerField(blank=True, null=True)),
                ('muros_ext', models.IntegerField(blank=True, null=True)),
                ('muros_int', models.IntegerField(blank=True, null=True)),
                ('cubierta', models.IntegerField(blank=True, null=True)),
                ('pisos', models.IntegerField(blank=True, null=True)),
                ('carpinteria', models.IntegerField(blank=True, null=True)),
                ('plantas', models.IntegerField(blank=True, null=True)),
                ('anyo', models.IntegerField(blank=True, null=True)),
                ('conservacion', models.IntegerField(blank=True, null=True)),
                ('uso', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'terrenos_mejoras20',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Terrenosvista19',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('superficie', models.FloatField(blank=True, null=True)),
                ('barrio', models.CharField(blank=True, max_length=255, null=True)),
                ('via', models.IntegerField(blank=True, null=True)),
                ('agua', models.BooleanField(blank=True, null=True)),
                ('alcantarillado', models.BooleanField(blank=True, null=True)),
                ('energia', models.BooleanField(blank=True, null=True)),
                ('telefono', models.BooleanField(blank=True, null=True)),
                ('transporte', models.BooleanField(blank=True, null=True)),
                ('internet', models.BooleanField(blank=True, null=True)),
                ('titular', models.IntegerField(blank=True, null=True)),
                ('topografia', models.IntegerField(blank=True, null=True)),
                ('forma', models.IntegerField(blank=True, null=True)),
                ('ubicacion', models.IntegerField(blank=True, null=True)),
                ('frente', models.FloatField(blank=True, null=True)),
                ('fondo', models.FloatField(blank=True, null=True)),
                ('suptest', models.FloatField(blank=True, null=True)),
                ('manzano', models.CharField(blank=True, max_length=255, null=True)),
                ('predio', models.CharField(blank=True, max_length=255, null=True)),
                ('subpredio', models.CharField(blank=True, max_length=255, null=True)),
                ('norte', models.CharField(blank=True, max_length=255, null=True)),
                ('sur', models.CharField(blank=True, max_length=255, null=True)),
                ('este', models.CharField(blank=True, max_length=255, null=True)),
                ('oeste', models.CharField(blank=True, max_length=255, null=True)),
                ('base', models.CharField(blank=True, max_length=255, null=True)),
                ('zona', models.IntegerField(blank=True, null=True)),
                ('material_via', models.IntegerField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=32719)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=255, null=True)),
                ('documento', models.IntegerField(blank=True, null=True)),
                ('tipo_doc', models.IntegerField(blank=True, null=True)),
                ('caracter', models.IntegerField(blank=True, null=True)),
                ('documento_prop', models.IntegerField(blank=True, null=True)),
                ('adquisicion', models.IntegerField(blank=True, null=True)),
                ('nombrecaracter', models.CharField(blank=True, max_length=255, null=True)),
                ('codigocaracter', models.CharField(blank=True, max_length=255, null=True)),
                ('nombreadquisicion', models.CharField(blank=True, max_length=255, null=True)),
                ('codigoadquisicion', models.CharField(blank=True, max_length=255, null=True)),
                ('codigodocumento', models.CharField(blank=True, max_length=255, null=True)),
                ('tipodocumento', models.CharField(blank=True, max_length=255, null=True)),
                ('codigodocumnetopropiedad', models.CharField(blank=True, max_length=255, null=True)),
                ('documentopropiedad', models.CharField(blank=True, max_length=255, null=True)),
                ('tipovia', models.CharField(blank=True, max_length=255, null=True)),
                ('valorvia', models.FloatField(blank=True, null=True)),
                ('nombretopo', models.CharField(blank=True, max_length=255, null=True)),
                ('descrtopo', models.CharField(blank=True, max_length=255, null=True)),
                ('valortopo', models.FloatField(blank=True, null=True)),
                ('nombreforma', models.CharField(blank=True, max_length=255, null=True)),
                ('codigoforma', models.CharField(blank=True, max_length=255, null=True)),
                ('valorforma', models.FloatField(blank=True, null=True)),
                ('nombreubicacion', models.CharField(blank=True, max_length=255, null=True)),
                ('codigoubicacion', models.CharField(blank=True, max_length=255, null=True)),
                ('valorubicacion', models.FloatField(blank=True, null=True)),
                ('valorcatastralzona', models.FloatField(blank=True, null=True)),
                ('idzona', models.IntegerField(blank=True, null=True)),
                ('valorcomercialzona', models.FloatField(blank=True, null=True)),
                ('materialvia', models.CharField(blank=True, max_length=255, null=True)),
                ('valormaterialvial', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'terrenosvista19',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoConstruccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tipo_construccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tipo_documento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoVia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tipo_via',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Titular',
            fields=[
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=255, null=True)),
                ('documento', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'titular',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Topografia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'topografia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ubicacion', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ubicacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Uso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uso', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'uso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zonas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('valor_comercial', models.FloatField(blank=True, null=True)),
                ('valor_catastral', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'zonas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zonificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase', models.CharField(blank=True, max_length=3, null=True)),
                ('subclase', models.SmallIntegerField(blank=True, null=True)),
                ('valor_comercial', models.FloatField(blank=True, null=True)),
                ('valor_catastral', models.FloatField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=32719)),
            ],
            options={
                'db_table': 'zonificacion',
                'managed': False,
            },
        ),
    ]