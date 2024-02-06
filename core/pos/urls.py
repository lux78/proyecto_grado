from django.urls import path
from core.pos.views.category.views import *
from core.pos.views.client.views import *
from core.pos.views.company.views import *
from core.pos.views.product.views import *
from core.pos.views.sale.views import *
from core.pos.views.servicio.views import *
from core.pos.views.plan.views import *
from core.pos.views.cliente.views import *
from core.pos.views.inscripcion.views import *


urlpatterns = [
    # category
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    # product
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    
      # servicio
    path('servicio/', ServicioListView.as_view(), name='servicio_list'),
    path('servicio/add/', ServicioCreateView.as_view(), name='servicio_create'),
    path('servicio/update/<int:pk>/', ServicioUpdateView.as_view(), name='servicio_update'),
    path('servicio/delete/<int:pk>/', ServicioDeleteView.as_view(), name='servicio_delete'),
      # Plan
    path('plan/', PlanListView.as_view(), name='plan_list'),
    path('plan/add/', PlanCreateView.as_view(), name='plan_create'),
    path('plan/update/<int:pk>/', PlanUpdateView.as_view(), name='plan_update'),
    path('plan/delete/<int:pk>/', PlanDeleteView.as_view(), name='plan_delete'),
    
      # cliente
    path('cliente/', ClienteListView.as_view(), name='cliente_list'),
    path('cliente/add/', ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/update/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('cliente/delete/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
    
    # company
    path('company/update/', CompanyUpdateView.as_view(), name='company_update'),
    # client
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/add/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    # sale
    path('sale/admin/', SaleListView.as_view(), name='sale_admin_list'),
    path('sale/admin/add/', SaleCreateView.as_view(), name='sale_admin_create'),
    path('sale/admin/delete/<int:pk>/', SaleDeleteView.as_view(), name='sale_admin_delete'),
    path('sale/admin/print/invoice/<int:pk>/', SalePrintInvoiceView.as_view(), name='sale_admin_print_invoice'),
     # inscripcion
    path('inscripcion/admin/', IncripcionListView.as_view(), name='inscripcion_admin_list'),
    path('inscripcion/admin/add/', IncripcionCreateView.as_view(), name='inscripcion_admin_create'),
    path('inscripcion/admin/delete/<int:pk>/', InscripcionDeleteView.as_view(), name='inscripcion_admin_delete'),
    path('inscripcion/admin/print/invoice/<int:pk>/', InscripcionPrintInvoiceView.as_view(), name='inscripcion_admin_print_invoice'),
]
