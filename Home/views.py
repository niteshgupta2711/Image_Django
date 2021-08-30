from django.shortcuts import render, HttpResponse
from Home.summarizer import Summarize
name="nitesh kumar gupta"


# Create your views here.
def index(request):
    #return HttpResponse("this is a response")
    context ={
        "variable" : name
    }
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
def services(requet):
    return HttpResponse('this is a service page')
def contact(request):
    return HttpResponse("this is a contact page")

def summa(request):
    if request.method=="POST":
        text=request.POST.get('Text')
        context={"incoming":text,"summary":Summarize(text)}
        return render(request,"Summarizer.html",context)
    else:
        return render(request,"Summarizer.html")
        



    

    
    
    
    