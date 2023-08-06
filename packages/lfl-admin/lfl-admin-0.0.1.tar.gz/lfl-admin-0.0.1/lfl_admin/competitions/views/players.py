from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from lfl_admin.competitions.models.players import Players, PlayersManager


@JsonResponseWithException()
def Players_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Players.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=PlayersManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Players_Add(request):
    return JsonResponse(DSResponseAdd(data=Players.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Players_Update(request):
    return JsonResponse(DSResponseUpdate(data=Players.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Players_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Players.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Players_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Players.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Players_Info(request):
    return JsonResponse(DSResponse(request=request, data=Players.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Players_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Players.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
