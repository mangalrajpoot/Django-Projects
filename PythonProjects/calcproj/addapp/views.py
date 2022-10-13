from django.shortcuts import render
from django.http import HttpResponse
def add(request):
   if request.method=="POST":
      a = request.POST["txtnum1"]
      b = request.POST["txtnum2"]
      c = int(a)+int(b)
      return HttpResponse("Result is "+str(c))
   else:    
      return render(request,"addapp/addition.html")

def prime(request):
    if request.method == "POST":
        num = int(request.POST["txtnum"])
        s = ""
        for i in range(2,num):
            if num%i==0:
                s = "Not prime"
                break
        else:
             s = "prime"  
        return HttpResponse(s)           

    return render(request,"addapp/prime.html")