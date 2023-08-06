from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from lfl_admin.competitions.models.disqualification_zones import Disqualification_zones, Disqualification_zonesManager


@JsonResponseWithException()
def Disqualification_zones_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Disqualification_zones.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Disqualification_zonesManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Disqualification_zones_Add(request):
    return JsonResponse(DSResponseAdd(data=Disqualification_zones.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Disqualification_zones_Update(request):
    return JsonResponse(DSResponseUpdate(data=Disqualification_zones.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Disqualification_zones_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Disqualification_zones.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Disqualification_zones_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Disqualification_zones.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Disqualification_zones_Info(request):
    return JsonResponse(DSResponse(request=request, data=Disqualification_zones.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Disqualification_zones_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Disqualification_zones.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
