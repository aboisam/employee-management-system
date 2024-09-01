from django.shortcuts import render, redirect
from .models import Employee

def allemployees(request):
    emp = Employee.objects.all()
    return render(request, 'emp/allemployees.html', {"allemployees":emp})

def singleemployee(request, empid):
    return render(request, 'emp/singleemployee.html')
 
def addemployee(request):
    if request.method == "POST":
        #take all parameters from the form, by their names kept.
        employeeid = request.POST.get('employeeid')
        employeename = request.POST.get('employeename')
        employeeemail = request.POST.get('employeeemail')
        employeeaddress = request.POST.get('employeeaddress')
        employeephone = request.POST.get('employeephone')


        # creat an object of the Employee model. 
        e = Employee()
        e.employeeid    = employeeid
        e.employeename  = employeename
        e.email         = employeeemail
        e.address       = employeeaddress
        e.phone         = employeephone
        e.save()
        return redirect("/allemployees")
    return render(request, "emp/addemployee.html")

def deleteemployee(request, empid):
   e = Employee.objects.get(pk = empid)
   e.delete()
   return redirect("allemployees")


def updateemployee(request, empid):
    e = Employee.objects.get(pk = empid)
    return render(request, "emp/updateemployee.html", {"singleemp": e})

def doupdateemployee(request, empid):
    updatedemployeeid       = request.POST.get('employeeid')
    updatedemployeename     = request.POST.get('employeename')
    updatedemployeeemail    = request.POST.get('employeeemail')
    updatedemployeeaddress  = request.POST.get('employeeaddress')
    updatedemployeephone    = request.POST.get('employeephone')
    emp = Employee.objects.get(pk = empid)
    emp.employeeid     = updatedemployeeid
    emp.employeename   = updatedemployeename
    emp.email          = updatedemployeeemail
    emp.address        = updatedemployeeaddress
    emp.phone          = updatedemployeephone    

    emp.save()
    return redirect("allemployees")