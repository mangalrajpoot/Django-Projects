from django.shortcuts import render
def fab(request):
    if request.method=="POST":
       num = int(request.POST["txtnum"])
       a=-1
       b=1
       s = []
       for i in range(1,num):
          c = a+b
          s.append(str(c))
          a=b
          b=c
       return render(request,"fabapp/fab.html",{"key":s})    

    else:
        return render(request,"fabapp/fab.html")    
