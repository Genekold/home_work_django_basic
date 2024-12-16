from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product, Category
from catalog.services import ProductService, CategoryService


class ProductListView(ListView):
    model = Product


class ProductListByCategoryView(ListView):
    model = Product
    template_name = "catalog/product_by_category.html"
    context_object_name = "products"

    def get_queryset(self):
        return ProductService.get_product_by_category(self.kwargs['category_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['additional_information'] = {
            'len_product': len(ProductService.get_product_by_category(self.kwargs['category_id']))
        }

        return context


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class CategoryListView(ListView):
    model = Category
