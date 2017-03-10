from django.shortcuts import render

# Create your views here.
def home(request):
    from blog.models import Person
    dict = Person.objects.filter(name = 'josh')
 #   dict = {'name': u'david', 'age': 20}
    return render(request, 'home.html', {'person': dict})