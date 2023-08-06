from django.urls import path

from lfl_admin.region.views import region_zone_phones

urlpatterns = [

    path('Region_zone_phones/Fetch/', region_zone_phones.Region_zone_phones_Fetch),
    path('Region_zone_phones/Add', region_zone_phones.Region_zone_phones_Add),
    path('Region_zone_phones/Update', region_zone_phones.Region_zone_phones_Update),
    path('Region_zone_phones/Remove', region_zone_phones.Region_zone_phones_Remove),
    path('Region_zone_phones/Lookup/', region_zone_phones.Region_zone_phones_Lookup),
    path('Region_zone_phones/Info/', region_zone_phones.Region_zone_phones_Info),
    path('Region_zone_phones/Copy', region_zone_phones.Region_zone_phones_Copy),

]
