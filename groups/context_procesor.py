from . models import Category , Student

def context(request):
    categories = Category.objects.all()
    students = Student.objects.all()
    return {"categories": categories , "students": students}
