from django.shortcuts import render
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.db.models import Sum
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm, InventoryUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


class HomeView(TemplateView):
  template_name = "inventory/home.html"

  def get_context_data(self):
    context = super().get_context_data()
    context["ingredients"] = Ingredient.objects.all()
    context["recipes"] = RecipeRequirement.objects.all()
    context["menu_items"] = MenuItem.objects.all()
    context["purchases"] = Purchase.objects.all()
    return context

class InventoryList(ListView):
    model= Ingredient
    template_name= "inventory/view_inventory.html"

class CreateInventoryView(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name= "inventory/add_ingredient.html"
    form_class= IngredientForm
class UpdateInventoryView(LoginRequiredMixin, UpdateView):
    model= Ingredient
    template_name= "inventory/update_ingredient.html"
    form_class= InventoryUpdateForm
class DeleteInventoryView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name= "inventory/delete_ingredient.html"
    success_url = "/inventory/"

class ListMenu(ListView):
    model = MenuItem
    template_name= "inventory/menu_view.html"

class CreateMenuView(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name= "inventory/add_menu_item.html"
    form_class = MenuItemForm
    success_url = "inventory/view_inventory"

class DeleteMenuView(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name= "inventory/delete_menu.html"
    success_url = "/inventory/"

class CrateRecipeView(CreateView):
    model = RecipeRequirement
    template_name = "inventory/add_recipe_requirements.html"
    form_class= RecipeRequirementForm
    success_url= "menu/"
class ListPurchase(ListView):
    model = Purchase
    template_name= "inventory/view_purchase.html"

class CreatePurchaseView(CreateView):
    model = Purchase
    template_name= 'inventory/record_purchase.html'
    form_class= PurchaseForm
    success_url = "/purchase/"
class ProfitRevenueView(TemplateView):
    template_name = 'inventory/profit_revenue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Calculate total revenue
        total_revenue = 0
        purchases = Purchase.objects.all()
        for purchase in purchases:
            total_revenue += purchase.menu_item.price
        
        # Calculate total cost (if applicable)
        # For example, sum of ingredient costs used in menu items
        total_cost = 0
        # Assuming you have a way to calculate total cost from ingredients or other sources
        
        # Calculate profit
        profit = total_revenue - total_cost

        context['total_revenue'] = total_revenue
        context['total_cost'] = total_cost
        context['profit'] = profit
        return context