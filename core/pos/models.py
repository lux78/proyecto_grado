import os
from datetime import datetime

from django.db import models
from django.db.models import Sum, FloatField
from django.db.models.functions import Coalesce
from django.forms import model_to_dict

from config import settings
from core.pos.choices import GENDER
from core.user.models import User


class Servicio(models.Model):
    nombre = models.CharField(
        max_length=50, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'


class Plan(models.Model):
    servicio = models.ForeignKey(
        Servicio, on_delete=models.PROTECT, verbose_name='Servicio')
    duracion = models.CharField(
        max_length=13, verbose_name='duracion en días ')
    precio = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Precio del servicio')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f' ({self.servicio.nombre})'

    def get_short_name(self):
        return f' ({self.servicio.nombre})'

    def toJSON(self):
        item = model_to_dict(self)
        item['full_name'] = self.get_full_name()
        item['short_name'] = self.get_short_name()
        item['servicio'] = self.servicio.toJSON()
        item['precio'] = float(self.precio)
        return item

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'


class Cliente(models.Model):
    nombres = models.CharField(max_length=150, verbose_name='Nombres')
    apellidos = models.CharField(max_length=150, verbose_name='Apellidos')
    ci = models.CharField(max_length=13, unique=True,
                          verbose_name='Número de cédula de identidad')
    genero = models.CharField(
        max_length=50, choices=GENDER, default=GENDER[0][0], verbose_name='Genero')
    celular = models.CharField(
        max_length=10, null=True, blank=True, verbose_name='Nro de Celular')
    email = models.CharField(max_length=50, null=True,
                             blank=True, verbose_name='Email')
    fecha_nacimiento = models.DateField(
        default=datetime.now, verbose_name='Fecha de nacimiento')
    direccion = models.CharField(
        max_length=500, null=True, blank=True, verbose_name='Dirección')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f'{self.nombres} ({self.ci})'

    def birthdate_format(self):
        return self.fecha_nacimiento.strftime('%Y-%m-%d')

    def toJSON(self):
        item = model_to_dict(self)
        item['text'] = self.get_full_name()
        item['genero'] = {'id': self.genero, 'name': self.get_genero_display()}
        item['fecha_nacimiento'] = self.fecha_nacimiento.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nombre')
    description = models.CharField(
        max_length=500, null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    code = models.CharField(max_length=20, unique=True, verbose_name='Código')
    description = models.CharField(
        max_length=500, null=True, blank=True, verbose_name='Descripción')
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name='Categoría')
    price = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Precio de Compra')
    pvp = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Precio de Venta')
    image = models.ImageField(
        upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    is_service = models.BooleanField(
        default=False, verbose_name='¿Es un servicio?')
    with_tax = models.BooleanField(
        default=True, verbose_name='¿Se cobra impuesto?')
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f'{self.name} ({self.code}) ({self.category.name})'

    def get_short_name(self):
        return f'{self.name} ({self.category.name})'

    def get_image(self):
        if self.image:
            return f'{settings.MEDIA_URL}{self.image}'
        return f'{settings.STATIC_URL}img/default/empty.png'

    def toJSON(self):
        item = model_to_dict(self)
        item['full_name'] = self.get_full_name()
        item['short_name'] = self.get_short_name()
        item['category'] = self.category.toJSON()
        item['price'] = float(self.price)
        item['pvp'] = float(self.pvp)
        item['image'] = self.get_image()
        return item

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name='Razón social')
    ruc = models.CharField(max_length=13, verbose_name='Número de RUC')
    address = models.CharField(max_length=200, verbose_name='Dirección')
    mobile = models.CharField(max_length=10, verbose_name='Teléfono celular')
    phone = models.CharField(
        max_length=9, verbose_name='Teléfono convencional')
    email = models.CharField(max_length=50, verbose_name='Email')
    website = models.CharField(
        max_length=250, verbose_name='Dirección de página web')
    description = models.CharField(
        max_length=500, null=True, blank=True, verbose_name='Descripción')
    iva = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=9, verbose_name='IVA')
    image = models.ImageField(
        null=True, blank=True, upload_to='company/%Y/%m/%d', verbose_name='Logotipo de la empresa')

    def __str__(self):
        return self.name

    def get_iva(self):
        return float(self.iva)

    def get_image(self):
        if self.image:
            return f'{settings.MEDIA_URL}{self.image}'
        return f'{settings.STATIC_URL}img/default/empty.png'

    def toJSON(self):
        item = model_to_dict(self)
        item['image'] = self.get_image()
        item['iva'] = float(self.iva)
        return item

    class Meta:
        verbose_name = 'Compañia'
        verbose_name_plural = 'Compañias'
        default_permissions = ()
        permissions = (
            ('view_company', 'Can view Empresa'),
        )


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombre')
    dni = models.CharField(max_length=13, unique=True,
                           verbose_name='Número de cedula')
    gender = models.CharField(
        max_length=50, choices=GENDER, default=GENDER[0][0], verbose_name='Genero')
    mobile = models.CharField(max_length=10, null=True,
                              blank=True, verbose_name='Teléfono')
    email = models.CharField(max_length=50, null=True,
                             blank=True, verbose_name='Email')
    birthdate = models.DateField(
        default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(
        max_length=500, null=True, blank=True, verbose_name='Dirección')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f'{self.names} ({self.dni})'

    def birthdate_format(self):
        return self.birthdate.strftime('%Y-%m-%d')

    def toJSON(self):
        item = model_to_dict(self)
        item['text'] = self.get_full_name()
        item['gender'] = {'id': self.gender, 'name': self.get_gender_display()}
        item['birthdate'] = self.birthdate.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Inscripcion(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, verbose_name='Compañia')
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT, verbose_name='Cliente')
    empleado = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='Empleado')
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha y hora de registro')
    date_joined = models.DateField(
        default=datetime.now, verbose_name='Fecha de registro')
    subtotal_12 = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Subtotal 12%')
    subtotal_0 = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Subtotal 0%')
    dscto = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Descuento')
    total_dscto = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Valor del descuento')
    iva = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Iva')
    total_iva = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Valor de iva')
    total = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Total a pagar')
    cash = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Efectivo recibido')
    change = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Cambio')

    def __str__(self):
        return self.cliente.get_full_name()

    def get_subtotal_without_taxes(self):
        return float(self.inscripciondetalle_set.filter().aggregate(result=Coalesce(Sum('subtotal'), 0.00, output_field=FloatField())).get('result'))

    def get_full_subtotal(self):
        return float(self.subtotal_0) + float(self.subtotal_12)

    def calculate_invoice(self):
        self.subtotal_0 = float(self.inscripciondetalle_set.filter(product__with_tax=False).aggregate(
            result=Coalesce(Sum('total'), 0.00, output_field=FloatField())).get('result'))
        self.subtotal_12 = float(self.inscripciondetalle_set.filter(product__with_tax=True).aggregate(
            result=Coalesce(Sum('total'), 0.00, output_field=FloatField())).get('result'))
        self.total_iva = float(self.inscripciondetalle_set.filter(product__with_tax=True).aggregate(
            result=Coalesce(Sum('total_iva'), 0.00, output_field=FloatField())).get('result'))
        self.total_dscto = float(self.get_full_subtotal()) * float(self.dscto)
        self.total = float(self.get_full_subtotal()) + \
            float(self.total_iva) - float(self.total_dscto)
        self.save()

    def calculate_detail(self):
        for detail in self.inscripciondetalle_set.filter():
            detail.precio = float(detail.precio)
            detail.iva = float(self.iva)
            detail.price_with_vat = detail.price + (detail.precio * detail.iva)
            detail.subtotal = detail.precio * detail.cant
            detail.total_dscto = detail.subtotal * float(detail.dscto)
            detail.total_iva = (
                detail.subtotal - detail.total_dscto) * detail.iva
            detail.total = detail.subtotal - detail.total_dscto
            detail.save()

    def toJSON(self):
        item = model_to_dict(self, exclude=['company', 'creation_date'])
        item['cliente'] = self.cliente.toJSON()
        item['empleado'] = self.empleado.toJSON()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['subtotal_12'] = float(self.subtotal_12)
        item['subtotal_0'] = float(self.subtotal_0)
        item['subtotal'] = float(self.get_subtotal_without_taxes())
        item['dscto'] = float(self.dscto)
        item['total_dscto'] = float(self.total_dscto)
        item['iva'] = float(self.iva)
        item['total_iva'] = float(self.total_iva)
        item['total'] = float(self.total)
        item['cash'] = float(self.cash)
        item['change'] = float(self.change)
        return item

    class Meta:
        verbose_name = 'Inscripcion'
        verbose_name_plural = 'Inscripciones'
        default_permissions = ()
        permissions = (
            ('view_inscripcion', 'Can view Inscripcion'),
            ('add_inscripcion', 'Can add Inscripcion'),
            ('delete_inscripcion', 'Can delete inscripcion'),
            ('view_inscripcion_cliente', 'Can view_inscripcion_cliente inscripcion'),
        )


class InscripcionDetalle(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    precio = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    price_with_vat = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    subtotal = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    iva = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    total_iva = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    dscto = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    total_dscto = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return self.plan.nombre

    def get_iva_percent(self):
        return int(self.iva * 100)

    def toJSON(self):
        item = model_to_dict(self, exclude=['sale'])
        item['plan'] = self.plan.toJSON()
        item['precio'] = float(self.precio)
        item['price_with_vat'] = float(self.price_with_vat)
        item['subtotal'] = float(self.subtotal)
        item['iva'] = float(self.subtotal)
        item['total_iva'] = float(self.subtotal)
        item['dscto'] = float(self.dscto)
        item['total_dscto'] = float(self.total_dscto)
        item['total'] = float(self.total)
        return item

    class Meta:
        verbose_name = 'Detalle de Inscripcion'
        verbose_name_plural = 'Detalle de Inscripciones'
        default_permissions = ()


class Sale(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, verbose_name='Compañia')
    client = models.ForeignKey(
        Client, on_delete=models.PROTECT, verbose_name='Cliente')
    employee = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='Empleado')
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha y hora de registro')
    date_joined = models.DateField(
        default=datetime.now, verbose_name='Fecha de registro')
    subtotal_12 = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Subtotal 12%')
    subtotal_0 = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Subtotal 0%')
    dscto = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Descuento')
    total_dscto = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Valor del descuento')
    iva = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Iva')
    total_iva = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Valor de iva')
    total = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Total a pagar')
    cash = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Efectivo recibido')
    change = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00, verbose_name='Cambio')

    def __str__(self):
        return self.client.get_full_name()

    def get_subtotal_without_taxes(self):
        return float(self.saledetail_set.filter().aggregate(result=Coalesce(Sum('subtotal'), 0.00, output_field=FloatField())).get('result'))

    def get_full_subtotal(self):
        return float(self.subtotal_0) + float(self.subtotal_12)

    def calculate_invoice(self):
        self.subtotal_0 = float(self.saledetail_set.filter(product__with_tax=False).aggregate(
            result=Coalesce(Sum('total'), 0.00, output_field=FloatField())).get('result'))
        self.subtotal_12 = float(self.saledetail_set.filter(product__with_tax=True).aggregate(
            result=Coalesce(Sum('total'), 0.00, output_field=FloatField())).get('result'))
        self.total_iva = float(self.saledetail_set.filter(product__with_tax=True).aggregate(
            result=Coalesce(Sum('total_iva'), 0.00, output_field=FloatField())).get('result'))
        self.total_dscto = float(self.get_full_subtotal()) * float(self.dscto)
        self.total = float(self.get_full_subtotal()) + \
            float(self.total_iva) - float(self.total_dscto)
        self.save()

    def calculate_detail(self):
        for detail in self.saledetail_set.filter():
            detail.price = float(detail.price)
            detail.iva = float(self.iva)
            detail.price_with_vat = detail.price + (detail.price * detail.iva)
            detail.subtotal = detail.price * detail.cant
            detail.total_dscto = detail.subtotal * float(detail.dscto)
            detail.total_iva = (
                detail.subtotal - detail.total_dscto) * detail.iva
            detail.total = detail.subtotal - detail.total_dscto
            detail.save()

    def toJSON(self):
        item = model_to_dict(self, exclude=['company', 'creation_date'])
        item['client'] = self.client.toJSON()
        item['employee'] = self.employee.toJSON()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['subtotal_12'] = float(self.subtotal_12)
        item['subtotal_0'] = float(self.subtotal_0)
        item['subtotal'] = float(self.get_subtotal_without_taxes())
        item['dscto'] = float(self.dscto)
        item['total_dscto'] = float(self.total_dscto)
        item['iva'] = float(self.iva)
        item['total_iva'] = float(self.total_iva)
        item['total'] = float(self.total)
        item['cash'] = float(self.cash)
        item['change'] = float(self.change)
        return item

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        default_permissions = ()
        permissions = (
            ('view_sale', 'Can view Venta'),
            ('add_sale', 'Can add Venta'),
            ('delete_sale', 'Can delete Venta'),
            ('view_sale_client', 'Can view_sale_client Venta'),
        )


class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    cant = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    price_with_vat = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    subtotal = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    iva = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    total_iva = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    dscto = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    total_dscto = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return self.product.name

    def get_iva_percent(self):
        return int(self.iva * 100)

    def toJSON(self):
        item = model_to_dict(self, exclude=['sale'])
        item['product'] = self.product.toJSON()
        item['price'] = float(self.price)
        item['price_with_vat'] = float(self.price_with_vat)
        item['subtotal'] = float(self.subtotal)
        item['iva'] = float(self.subtotal)
        item['total_iva'] = float(self.subtotal)
        item['dscto'] = float(self.dscto)
        item['total_dscto'] = float(self.total_dscto)
        item['total'] = float(self.total)
        return item

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        default_permissions = ()


class InscripcionDetail(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    cant = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    price_with_vat = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    subtotal = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    iva = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    total_iva = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    dscto = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    total_dscto = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return self.plan.id

    def get_iva_percent(self):
        return int(self.iva * 100)

    def toJSON(self):
        item = model_to_dict(self, exclude=['inscripcion'])
        item['plan'] = self.plan.toJSON()
        item['precio'] = float(self.precio)
        item['price_with_vat'] = float(self.price_with_vat)
        item['subtotal'] = float(self.subtotal)
        item['iva'] = float(self.subtotal)
        item['total_iva'] = float(self.subtotal)
        item['dscto'] = float(self.dscto)
        item['total_dscto'] = float(self.total_dscto)
        item['total'] = float(self.total)
        return item

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        default_permissions = ()
