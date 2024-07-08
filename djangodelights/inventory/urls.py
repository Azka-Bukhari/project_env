from django.urls import path

from . import views

urlpatterns =[
    path('', views.HomeView.as_view(), name='home'),
    path('inventory/', views.InventoryList.as_view(), name="inventory"),
    path('inventory/create', views.CreateInventoryView.as_view(), name="createIngredient"),
    path('inventory/<pk>/update', views.UpdateInventoryView.as_view(), name="updateIngredient"),
    path('inventory/<pk>/delete', views.DeleteInventoryView.as_view(), name="deleteIngredient"),
    path('menu/', views.ListMenu.as_view(), name="menu"),
    path('menu/create', views.CreateMenuView.as_view(), name="createMenu"),
    path('menu/<pk>/delete', views.DeleteMenuView.as_view(), name="deleteMenu"),
    path('purchase/', views.ListPurchase.as_view(), name="purchase"),
    path('purchase/create', views.CreatePurchaseView.as_view(), name="createPurchase"),
    path('profit_revenue/', views.ProfitRevenueView.as_view(), name="profit_revenue"),
    path('add_recipe/', views.CrateRecipeView.as_view(), name="addrecipe"),
]