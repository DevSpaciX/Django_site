from contextlib import redirect_stderr
from multiprocessing import context
from unicodedata import name
from django.views.generic import TemplateView
# from Django.groups.models import Category
from groups.models import Student , Group , Teacher , Category , Tag 
from groups.forms import CreateCourseForm , CreateStudentForm
from django.shortcuts import redirect

from django.db.models import Q, F
from django.views.generic import TemplateView, ListView ,RedirectView




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


class CreateCourse(TemplateView):
    template_name = 'create_course.html'

    def get_context_data(self, **kwargs):
        context = super(CreateCourse, self).get_context_data(**kwargs)
        context['form'] = CreateCourseForm()
        return context

    def post(self, request):
        form = CreateCourseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.create_course()
            return redirect('/')

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)



class CreateStudent(TemplateView):
    template_name = 'create_student.html'

    def get_context_data(self, **kwargs):
        context = super(CreateStudent, self).get_context_data(**kwargs)
        context['form'] = CreateStudentForm()
        return context

    def post(self, request):
        student_form = CreateStudentForm(data=request.POST, files=request.FILES)
        if student_form.is_valid():
            student_form.create_student()
            return redirect('/')

        context = self.get_context_data()
        context['form'] = student_form
        return self.render_to_response(context)