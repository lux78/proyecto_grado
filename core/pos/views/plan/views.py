import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView, TemplateView

from core.pos.forms import PlanForm
from core.pos.models import Plan
from core.security.mixins import GroupPermissionMixin

MODULE_NAME = 'Planes'


class PlanListView(GroupPermissionMixin, TemplateView):
    template_name = 'plan/list.html'
    permission_required = 'view_plan'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'search':
                data = []
                for i in Plan.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Plan'
        context['list_url'] = reverse_lazy('plan_list')
        context['create_url'] = reverse_lazy('plan_create')
        context['module_name'] = MODULE_NAME
        return context


class PlanCreateView(GroupPermissionMixin, CreateView):
    template_name = 'plan/create.html'
    model = Plan
    form_class = PlanForm
    success_url = reverse_lazy('plan_list')
    permission_required = 'add_plan'

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
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo registro de un Servicio'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['module_name'] = MODULE_NAME
        return context


class PlanUpdateView(GroupPermissionMixin, UpdateView):
    template_name = 'plan/create.html'
    model = Plan
    form_class = PlanForm
    success_url = reverse_lazy('plan_list')
    permission_required = 'change_plan'

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
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Servicio'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['module_name'] = MODULE_NAME
        return context


class PlanDeleteView(GroupPermissionMixin, DeleteView):
    model = Plan
    template_name = 'delete.html'
    success_url = reverse_lazy('plan_list')
    permission_required = 'delete_plan'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.get_object().delete()
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Servicio'
        context['list_url'] = self.success_url
        context['module_name'] = MODULE_NAME
        return context
