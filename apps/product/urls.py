from django.urls import path
from .views import *


urlpatterns = [
    path('list/', list_, name='product-list'),
    path('create/', create, name='product-create'),
    path('at_income_create/', product_create, name='product-create-at-income'),
    path('details/<int:pk>/', details, name='product-details'),
    path('update/<int:pk>/', update, name='product-update'),
    path('delete/<int:pk>/', delete, name='product-delete'),
    path('sale/', sale, name='product-sale'),
    path('income/', income, name='product-income'),
    path('get-product/', get_product, name='get-product'),
    path('create-sell-history/', create_sell_history, name='create-sell-history'),
    path('create-income-history/', create_income_history, name='create-income-history'),
    path('update-quantity/', update_quantity, name='update-quantity'),
    path('find-product/', find_product, name='find-product'),
    path('search-product/', search_product, name='search-product'),
    path('reports/', reports, name='reports'),
    path('export_zero_stock/', export_zero_stock, name='export_zero_stock'),
    path('export_low_stock/', export_low_stock, name='export_low_stock'),
    path('export_by_category/', export_by_category, name='export_by_category'),
    path('export_by_brand/', export_by_brand, name='export_by_brand'),
    path('export_all/', export_all, name='export_all'),
    path('product/report_selection/', report_selection, name='report-selection'),

]