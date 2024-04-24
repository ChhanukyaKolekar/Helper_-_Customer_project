from django.shortcuts import render,redirect
from .models import Helper_Info,Customer_Info
# Create your views here.
from django.contrib import messages

def create_helper(request):
    if request.method=="POST":
        data=request.POST

        name=data.get("helper_name")
        age=data.get("helper_age")
        gender=data.get("helper_gender")
        skills=data.get("helper_skills")

        helper_id="HLP-"+str(Helper_Info.objects.count()+1000+1)

        obj=Helper_Info.objects.create(name=name,age=age,gender=gender,skills=skills,helper_id=helper_id)

        messages.success(request,"HELPER ADDED ")
        return redirect ("/add_helper")
    return render(request,"helper_form.html")

def create_customer(request):
    if request.method=="POST":
        data=request.POST

        name=data.get("customer_name")
        address=data.get("customer_address")
        contact=data.get("customer_contact")
     

        customer_id="CST-"+str(Customer_Info.objects.count()+1000+1)

        obj=Customer_Info.objects.create(name=name,address=address,phone_number=contact,customer_id=customer_id)

        messages.success(request," CUSTOMER ADDED ")
        return redirect ("/add_customer")
    return render (request,"customer__form.html")

def assign_helper(request):

    if request.method=="POST":
        data=request.POST
        cust_id=data.get("customer_id")
        helper_id_rx=data.get("helper_id")
        print(cust_id,helper_id_rx)
        try:
            get_row=Customer_Info.objects.get(customer_id=cust_id)
        except:
            messages.error(request,f"{cust_id} ID NOT FOUND")
            return redirect("/assign_helper")

        get_row.update_helper_assigned(hlp_id=helper_id_rx)

        update_helper_row=Helper_Info.objects.get(helper_id=helper_id_rx)
        update_helper_row.update_status()

        messages.success(request,"HELPER ASSIGNED SUCCESSFULLY")
        return redirect("/assign_helper")
    avialable_helpers=Helper_Info.objects.all().filter(status="AVAILABLE").values("helper_id")
    # print(avialable_helpers)
    return render (request,'assign_helper.html',{"list_of_available_helper":avialable_helpers})
    

def cust_info(request):
    cust_info_list=Customer_Info.objects.all().values()
    return render(request,"information.html",{"customer_data":cust_info_list})

def helper_info(request):
    helper_info_list=Helper_Info.objects.all().values()

    return render(request,"information.html",{"helpers_data":helper_info_list})
   