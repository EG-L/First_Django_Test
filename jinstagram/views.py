from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class sub(APIView):
    def get(self, request):
        print("get 호출")
        return render(request, 'jinstagram/main.html')

    def post(self,request):
        print("post 호출")
        return render(request, 'jinstagram/main.html')