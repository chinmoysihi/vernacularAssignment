from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .src.validate_finite_set import Validate_finite_Values
from .src.validate_numeric_set import Validate_Numeric_Values

import json

# Create your views here.
@api_view(['POST'])
def finite_set(request):
    requestData = json.loads(request.body)
    # print(requestData)
    values = requestData.get("values")
    supported_values = requestData.get("supported_values")
    invalid_trigger = requestData.get("invalid_trigger")
    key = requestData.get('key')
    support_multiple = requestData.get('support_multiple')
    pick_first = requestData.get('pick_first')

    validator = Validate_finite_Values()
    resp = validator.validate_finite_values_entity(values,supported_values,invalid_trigger,key,support_multiple,pick_first)
    print(resp)
    return Response(resp,status=status.HTTP_200_OK)

@api_view(['POST'])
def numeric_set(request):
    requestData = json.loads(request.body)

    values = requestData.get("values")
    invalid_trigger = requestData.get("invalid_trigger")
    key = requestData.get("key")
    support_multiple = requestData.get("support_multiple")
    pick_first = requestData.get("pick_first")
    constraint = requestData.get("constraint")
    var_name = requestData.get("var_name")

    validator = Validate_Numeric_Values()
    resp = validator.validate_numeric_entity(values,invalid_trigger,key,support_multiple,pick_first,constraint,var_name)
    return Response(resp,status=status.HTTP_200_OK)
