from django.views import generic


class BaseIndexView(generic.TemplateView):
    """
    Base index view.
    """
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
