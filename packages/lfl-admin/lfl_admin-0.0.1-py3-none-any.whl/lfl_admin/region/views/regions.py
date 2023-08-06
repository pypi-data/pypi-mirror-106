from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from lfl_admin.region.models.regions import Regions, RegionsManager


@JsonResponseWithException()
def Regions_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Regions.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=RegionsManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Regions_Add(request):
    return JsonResponse(DSResponseAdd(data=Regions.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Regions_Update(request):
    return JsonResponse(DSResponseUpdate(data=Regions.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Regions_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Regions.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Regions_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Regions.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Regions_Info(request):
    return JsonResponse(DSResponse(request=request, data=Regions.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Regions_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Regions.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
