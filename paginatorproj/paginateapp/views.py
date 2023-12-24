from django.shortcuts import render
from.models import cities
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    # obj = cities.objects.all()
    paginate = Paginator(cities.objects.all(), 2)
    pageno = request.GET.get('page')
    page_data = paginate.get_page(pageno)
    return render(request,'home.html',{'cities':page_data})
