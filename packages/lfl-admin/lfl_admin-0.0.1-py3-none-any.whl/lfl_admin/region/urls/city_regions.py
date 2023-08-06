from django.urls import path

from lfl_admin.region.views import city_regions

urlpatterns = [

    path('City_regions/Fetch/', city_regions.City_regions_Fetch),
    path('City_regions/Add', city_regions.City_regions_Add),
    path('City_regions/Update', city_regions.City_regions_Update),
    path('City_regions/Remove', city_regions.City_regions_Remove),
    path('City_regions/Lookup/', city_regions.City_regions_Lookup),
    path('City_regions/Info/', city_regions.City_regions_Info),
    path('City_regions/Copy', city_regions.City_regions_Copy),

]
