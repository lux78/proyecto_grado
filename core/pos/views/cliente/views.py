import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView, TemplateView

from core.pos.forms import ClienteForm
from core.pos.models import Cliente
from core.security.mixins import GroupPermissionMixin

MODULE_NAME = 'Clientes'


class ClienteListView(TemplateView):
    template_name = 'cliente/list.html'
    permission_required = 'view_cliente'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'search':
                data = []
                for i in Cliente.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['list_url'] = reverse_lazy('cliente_list')
        context['create_url'] = reverse_lazy('cliente_create')
        context['module_name'] = MODULE_NAME
        return context


class ClienteCreateView( CreateView):
    template_name = 'cliente/create.html'
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('cliente_list')
    permission_required = 'add_cliente'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'add':
                data = self.get_form().save()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Nuevo registro de un Cliente'
        context['action'] = 'add'
        context['module_name'] = MODULE_NAME
        return context


class ClienteUpdateView( UpdateView):
    template_name = 'cliente/create.html'
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('cliente_list')
    permission_required = 'change_cliente'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'edit':
                data = self.get_form().save()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Edición de un Cliente'
        context['action'] = 'edit'
        context['module_name'] = MODULE_NAME
        return context


class ClienteDeleteView(GroupPermissionMixin, DeleteView):
    model = Cliente
    template_name = 'delete.html'
    success_url = reverse_lazy('cliente_list')
    permission_required = 'delete_cliente'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.get_object().delete()
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Cliente'
        context['list_url'] = self.success_url
        context['module_name'] = MODULE_NAME
        return context
