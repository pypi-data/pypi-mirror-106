from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from lfl_admin.inventory.models.clothes import Clothes, ClothesManager


@JsonResponseWithException()
def Clothes_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Clothes.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=ClothesManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Clothes_Add(request):
    return JsonResponse(DSResponseAdd(data=Clothes.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Clothes_Update(request):
    return JsonResponse(DSResponseUpdate(data=Clothes.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Clothes_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Clothes.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Clothes_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Clothes.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Clothes_Info(request):
    return JsonResponse(DSResponse(request=request, data=Clothes.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Clothes_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Clothes.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
