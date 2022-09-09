from django.shortcuts import render,redirect
from .models import Customer
from .forms import CustomerForm
# Create your views here.

def customer_list(request):
    records=Customer.objects.all()
    mydict={'records':records}
    return render(request,'listingpage.html',context=mydict)

def addCustomer(request):
    mydict={}
    form=CustomerForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    mydict['form']=form
    return render(request,'addc.html',mydict)

def editCustomer(request,id=None):
    one_rec=Customer.objects.get(pk=id)
    form=CustomerForm(request.POST or None,request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict= {'form':form}
    return render(request,'edit.html',context=mydict)
def deleteCustomer(request,eid=None):
    one_rec = Customer.objects.get(pk=eid)
    if  request.method=="POST":
         one_rec.delete()
         return redirect('/')
    return render(request,'delete.html')
def viewCustomer(request,eid=None):
    mydict={}
    one_rec = Customer.objects.get(pk=eid)
    mydict['customer']=one_rec
    return render(request,'''view.html''',mydict)