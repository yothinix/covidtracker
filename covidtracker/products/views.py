from django.views.generic import TemplateView

from products.models import Product


class ProductView(TemplateView):
    template_name = "product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_menu"] = "active"
        context["products"] = Product.objects.all()
        return context
