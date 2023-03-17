from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from components.models import Terrenos19
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from django.core.paginator import Paginator

# Create your views here.
class DashboardView(LoginRequiredMixin,TemplateView):
    pass
    


@login_required
def dashboard_view(request):
    user  = User.objects.get(username=User.username).pk
    terrenos = Terrenos19.objects.filter(titular__isnull=True).values('codigo')
    # Set up pagination
    p = Paginator(terrenos,6)
    page = request.GET.get('page')
    _paginator = p.get_page(page)
    
    # terrenos = serialize('geojson',terrenos,geometry_field='geom')
    data = [v['codigo'] for v in terrenos]

    
    return render(request, "dashboards/index.html",{
        'data_list': data,
        'data_len' : len(data),
        'data': _paginator
    })

@login_required
def Terrenos_List(request): 
    
    terrenos = Terrenos19.objects.filter(titular__isnull=True).values('codigo')
    # Set up pagination
    p = Paginator(terrenos,5)
    
    return render(request, "dashboards/index.html")



