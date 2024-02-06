from django import forms

from .models import *


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
            'description': forms.Textarea(attrs={
                'rows': 3,
                'cols': 3,
                'placeholder': 'Ingrese una descripción'
            }),
        }

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
            'code': forms.TextInput(attrs={'placeholder': 'Ingrese un código'}),
            'description': forms.Textarea(attrs={'placeholder': 'Ingrese una descripción', 'rows': 3, 'cols': 3}),
            'category': forms.Select(attrs={'class': 'form-control select2', 'style': 'width: 100%;'}),
            'price': forms.TextInput(),
            'pvp': forms.TextInput(),
            'stock': forms.TextInput(),
            'is_service': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'with_tax': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ServicioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Servicio
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
        }

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class PlanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['servicio'].widget.attrs['autofocus'] = True

    class Meta:
        model = Plan
        fields = ['servicio', 'duracion', 'precio']
        widgets = {
            'servicio': forms.Select(attrs={'class': 'form-control select2', 'style': 'width: 100%;'}),
            'duracion': forms.TextInput(attrs={'placeholder': 'Ingrese los dias'}),
            'precio': forms.TextInput(),
        }

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombres'].widget.attrs['autofocus'] = True

    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
            'apellidos': forms.TextInput(attrs={'placeholder': 'Ingrese los apellidos'}),
            'ci': forms.TextInput(attrs={'placeholder': 'Ingrese un número de cedula de identidad'}),
            'genero': forms.Select(attrs={
                'class': 'select2',
                'style': 'width: 100%'
            }),
            'celular': forms.TextInput(attrs={'placeholder': 'Ingrese el nro de celular'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ingrese el email'}),
            'fecha_nacimiento': forms.DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-control datetimepicker-input',
                'id': 'fecha_nacimiento',
                'value': datetime.now().strftime('%Y-%m-%d'),
                'data-toggle': 'datetimepicker',
                'data-target': '#birthdate'
            }),
            'direccion': forms.TextInput(attrs={
                'placeholder': 'Ingrese la dirección'
            }),
        }

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                data = super().save().toJSON()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class CompanyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese un nombre de razón social'}),
            'ruc': forms.TextInput(attrs={'placeholder': 'Ingrese un ruc'}),
            'address': forms.TextInput(attrs={'placeholder': 'Ingrese una dirección'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Ingrese un teléfono celular'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ingrese un teléfono convencional'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ingrese un email'}),
            'website': forms.TextInput(attrs={'placeholder': 'Ingrese una dirección web'}),
            'description': forms.TextInput(attrs={'placeholder': 'Ingrese una descripción'}),
            'iva': forms.TextInput(),
        }

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'names': forms.TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
            'dni': forms.TextInput(attrs={'placeholder': 'Ingrese un número de cedula'}),
            'gender': forms.Select(attrs={
                'class': 'select2',
                'style': 'width: 100%'
            }),
            'mobile': forms.TextInput(attrs={'placeholder': 'Ingrese un teléfono celular'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ingrese un email'}),
            'birthdate': forms.DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-control datetimepicker-input',
                'id': 'birthdate',
                'value': datetime.now().strftime('%Y-%m-%d'),
                'data-toggle': 'datetimepicker',
                'data-target': '#birthdate'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Ingrese una dirección'
            }),
        }

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                data = super().save().toJSON()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class InscripcionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.none()

    class Meta:
        model = Inscripcion
        fields = '__all__'
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select select2'}),
            'date_joined': forms.DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-control datetimepicker-input',
                'id': 'date_joined',
                'value': datetime.now().strftime('%Y-%m-%d'),
                'data-toggle': 'datetimepicker',
                'data-target': '#date_joined'
            }),
            'subtotal_0': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True
            }),
            'subtotal_12': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True
            }),
            'iva': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True
            }),
            'total_iva': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True
            }),
            'dscto': forms.TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }),
            'total_dscto': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True
            }),
            'total': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True
            }),
            'cash': forms.TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }),
            'change': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': True
            }),
        }


class SaleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.none()

    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'client': forms.Select(attrs={'class': 'form-select select2'}),
            'date_joined': forms.DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-control datetimepicker-input',
                'id': 'date_joined',
                'value': datetime.now().strftime('%Y-%m-%d'),
                'data-toggle': 'datetimepicker',
                'data-target': '#date_joined'
            }),
            'subtotal_0': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True
            }),
            'subtotal_12': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True
            }),
            'iva': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True
            }),
            'total_iva': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True
            }),
            'dscto': forms.TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }),
            'total_dscto': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True
            }),
            'total': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': True
            }),
            'cash': forms.TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }),
            'change': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': True
            }),
        }
