# Generated by Django 4.0.2 on 2024-01-12 01:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nombre')),
                ('dni', models.CharField(max_length=13, unique=True, verbose_name='Número de cedula')),
                ('gender', models.CharField(choices=[('male', 'Masculino'), ('female', 'Femenino')], default='male', max_length=50, verbose_name='Genero')),
                ('mobile', models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('birthdate', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de nacimiento')),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Razón social')),
                ('ruc', models.CharField(max_length=13, verbose_name='Número de RUC')),
                ('address', models.CharField(max_length=200, verbose_name='Dirección')),
                ('mobile', models.CharField(max_length=10, verbose_name='Teléfono celular')),
                ('phone', models.CharField(max_length=9, verbose_name='Teléfono convencional')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('website', models.CharField(max_length=250, verbose_name='Dirección de página web')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='IVA')),
                ('image', models.ImageField(blank=True, null=True, upload_to='company/%Y/%m/%d', verbose_name='Logotipo de la empresa')),
            ],
            options={
                'verbose_name': 'Compañia',
                'verbose_name_plural': 'Compañias',
                'permissions': (('view_company', 'Can view Empresa'),),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='Código')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio de Compra')),
                ('pvp', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio de Venta')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d', verbose_name='Imagen')),
                ('is_service', models.BooleanField(default=False, verbose_name='¿Es un servicio?')),
                ('with_tax', models.BooleanField(default=True, verbose_name='¿Se cobra impuesto?')),
                ('stock', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora de registro')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('subtotal_12', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Subtotal 12%')),
                ('subtotal_0', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Subtotal 0%')),
                ('dscto', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Descuento')),
                ('total_dscto', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Valor del descuento')),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Iva')),
                ('total_iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Valor de iva')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Total a pagar')),
                ('cash', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Efectivo recibido')),
                ('change', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Cambio')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pos.client', verbose_name='Cliente')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pos.company', verbose_name='Compañia')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'permissions': (('view_sale', 'Can view Venta'), ('add_sale', 'Can add Venta'), ('delete_sale', 'Can delete Venta'), ('view_sale_client', 'Can view_sale_client Venta')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('price_with_vat', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total_iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('dscto', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total_dscto', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pos.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.sale')),
            ],
            options={
                'verbose_name': 'Detalle de Venta',
                'verbose_name_plural': 'Detalle de Ventas',
                'default_permissions': (),
            },
        ),
    ]
