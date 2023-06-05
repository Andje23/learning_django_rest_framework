from django.shortcuts import render
from django.http import JsonResponse

def blog_list(reguest) -> JsonResponse:
    data: dict = {
        "Message": "Hello Word"
    }
    
    return JsonResponse(data)
