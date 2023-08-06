from django.urls import path

from lfl_admin.region.views import region_zone_e_mails

urlpatterns = [

    path('Region_zone_e_mails/Fetch/', region_zone_e_mails.Region_zone_e_mails_Fetch),
    path('Region_zone_e_mails/Add', region_zone_e_mails.Region_zone_e_mails_Add),
    path('Region_zone_e_mails/Update', region_zone_e_mails.Region_zone_e_mails_Update),
    path('Region_zone_e_mails/Remove', region_zone_e_mails.Region_zone_e_mails_Remove),
    path('Region_zone_e_mails/Lookup/', region_zone_e_mails.Region_zone_e_mails_Lookup),
    path('Region_zone_e_mails/Info/', region_zone_e_mails.Region_zone_e_mails_Info),
    path('Region_zone_e_mails/Copy', region_zone_e_mails.Region_zone_e_mails_Copy),

]
