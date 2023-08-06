from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from lfl_admin.competitions.models.clubs import Clubs, ClubsManager


@JsonResponseWithException()
def Clubs_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Clubs.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=ClubsManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Clubs_Add(request):
    return JsonResponse(DSResponseAdd(data=Clubs.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Clubs_Update(request):
    return JsonResponse(DSResponseUpdate(data=Clubs.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Clubs_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Clubs.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Clubs_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Clubs.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Clubs_Info(request):
    return JsonResponse(DSResponse(request=request, data=Clubs.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Clubs_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Clubs.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
