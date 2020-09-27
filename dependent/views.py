from django.shortcuts import render , redirect
from django.views import View, generic
from .models import Person , SubDistrict , District , Division , Country
from .forms import PersonCreationForm , PersonFilterForm

def index(request):
    person = Person.objects.all()
    form = PersonFilterForm(request.GET)
    if form.is_valid():
        country_id = request.GET.get('country')
        division_id = request.GET.get('division')
        district_id = request.GET.get('district')
        subdistrict_id = request.GET.get('subdistrict')
        person = Person.objects.filter(subdistrict__id=subdistrict_id)
        return render(request , "index.html" , {'form':form,'person':person} )
    return render(request , "index.html" , {'form':form,'person':person} )

def create(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST,request.FILES or None)
        if form.is_valid():
            instance=form.save(commit=False)
            form.save()
            return redirect('dependent:home')
    return render(request , "create.html" , {'form':form} )


# # AJAX
def load_division(request):
    country_id = request.GET.get('country_id')
    dividions = Division.objects.filter(country_id=country_id).all()
    return render(request, 'city_dropdown_list_options.html', {'dividions': dividions})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def load_district(request):
    division_id = request.GET.get('division_id')
    districts = District.objects.filter(division_id=division_id).all()
    return render(request, 'district_dropdown_list_options.html', {'districts': districts})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def load_subdistrict(request):
    district_id = request.GET.get('district_id')
    subdistricts = SubDistrict.objects.filter(district_id=district_id).all()
    return render(request, 'subdistrict_dropdown_list_options.html', {'subdistricts': subdistricts})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
