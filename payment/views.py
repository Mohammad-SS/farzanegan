from django.shortcuts import render , HttpResponse
from django.views import View
# Create your views here.


class Index(View):
    def get(self , request , *args , **kwargs):
        return render(request,'payment/index.html')