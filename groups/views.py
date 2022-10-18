from contextlib import redirect_stderr
from multiprocessing import context
from unicodedata import name
from django.views.generic import TemplateView
# from Django.groups.models import Category
from groups.models import Student , Group , Teacher , Category , Tag 
from groups.forms import CreateCourseForm , CreateStudentForm
from django.shortcuts import redirect

from django.db.models import Q, F
from django.views.generic import TemplateView, ListView ,RedirectView , FormView ,CreateView




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


class CreateCourse(FormView):
    template_name = 'create_course.html'
    form_class = CreateCourseForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(CreateCourse, self).form_valid(form)


class CreateStudent(CreateView):
    template_name = 'create_student.html'
    model = Student
    form_class = CreateStudentForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(CreateStudent, self).form_valid(form)
