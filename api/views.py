from django.http import JsonResponse
from django.conf import settings
from .models import DieMap


def die_map_api(request):
    key = request.headers.get("X-Api-Key") or request.GET.get("api_key", "")
    if key != settings.EXTERNAL_API_KEY:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    qs = DieMap.objects.all()

    sapcode = (request.GET.get("sapcode") or "").strip()
    if sapcode:
        qs = qs.filter(sapcode=sapcode)

    results = list(qs.values("sapcode", "benkam"))
    return JsonResponse({"results": results, "count": len(results)})
