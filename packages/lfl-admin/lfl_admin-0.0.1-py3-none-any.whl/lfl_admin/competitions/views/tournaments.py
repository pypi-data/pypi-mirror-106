from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from lfl_admin.competitions.models.tournaments import Tournaments, TournamentsManager


@JsonResponseWithException()
def Tournaments_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Tournaments.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=TournamentsManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Tournaments_Add(request):
    return JsonResponse(DSResponseAdd(data=Tournaments.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Tournaments_Update(request):
    return JsonResponse(DSResponseUpdate(data=Tournaments.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Tournaments_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Tournaments.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Tournaments_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Tournaments.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Tournaments_Info(request):
    return JsonResponse(DSResponse(request=request, data=Tournaments.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Tournaments_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Tournaments.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
