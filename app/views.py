from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import json
from .permissions import Check_API_KEY_Auth
from .models import Price
from .serializers import PriceSerializer
from rest_framework.renderers import JSONRenderer
from django.core.serializers.json import DjangoJSONEncoder

from app.tasks import exchangeRate

@api_view(['GET','POST'])
@permission_classes((Check_API_KEY_Auth, ))
def test(request):
    if request.method == "GET":
        data = exchangeRate.delay().get(timeout=10)
        return Response(data, content_type="application/json")
    else:
        price_queryset = Price.objects.all()
        serializer = PriceSerializer(price_queryset, many=True)
        json_data = JSONRenderer().render(serializer.data)
        #print(json_data)
        return JsonResponse(data=json_data.decode('utf8'), content_type="application/json", safe=False)
        #return Response(json_data,content_type="application/json")