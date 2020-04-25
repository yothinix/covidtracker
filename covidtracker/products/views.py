from django.views.generic import TemplateView


class ProductView(TemplateView):
    template_name = "product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_menu"] = "active"
        return context
