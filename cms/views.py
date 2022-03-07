from django.shortcuts import render,redirect

# Create your views here.
from .models import Customer
from .forms import CustomerForm
def customer_list(request):
    mydict={}
    records=Customer.objects.all()
    mydict['records']=records
    return render(request,'listingpage.html',mydict)

def addCustomer(request):
    mydict={}
    form=CustomerForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    mydict['form']=form
    return render(request,'addc.html',mydict)

def editCustomer(request,id=None):
    print(id)
    one_rec=Customer.objects.get(pk=id)
    mydict={}
    form=CustomerForm(request.POST or None,request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict['form']=form
    return render(request,'edit.html',mydict)
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