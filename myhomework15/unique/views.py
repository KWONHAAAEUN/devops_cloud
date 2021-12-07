from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from unique.models import Shop

def unique_list(request: HttpRequest) -> HttpResponse:
    qs=Shop.objects.all()
    query=request.GET.get("query","")
    if query:
        qs=qs.filter(name__icontains=query)
    context_data={
        "unique_list":qs,
        }
    return  render(request,"unique/unique_list.html",context_data)

def unique_detail(request: HttpRequest, pk:int) -> HttpResponse:
    unique=Shop.objects.get(pk=pk)
    context_data={
        "unique":unique,
    }
    return render(request,"unique/unique_detail.html",context_data)
