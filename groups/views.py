from unicodedata import name
from django.views.generic import TemplateView
# from Django.groups.models import Category
from groups.models import Student , Group , Teacher , Category , Tag 


from django.db.models import Q, F
from django.views.generic import TemplateView, ListView




class IndexView(ListView):
    template_name = 'index.html'
    model = Group
    paginate_by = 10

    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        return queryset.select_related(
            'mentor'
        ).prefetch_related(
            "tags"
        )

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()

        return context