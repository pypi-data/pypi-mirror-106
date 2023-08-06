from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from lfl_admin.region.models.region_zone_phones import Region_zone_phones, Region_zone_phonesManager


@JsonResponseWithException()
def Region_zone_phones_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Region_zone_phones.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Region_zone_phonesManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Region_zone_phones_Add(request):
    return JsonResponse(DSResponseAdd(data=Region_zone_phones.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Region_zone_phones_Update(request):
    return JsonResponse(DSResponseUpdate(data=Region_zone_phones.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Region_zone_phones_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Region_zone_phones.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Region_zone_phones_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Region_zone_phones.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Region_zone_phones_Info(request):
    return JsonResponse(DSResponse(request=request, data=Region_zone_phones.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Region_zone_phones_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Region_zone_phones.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
