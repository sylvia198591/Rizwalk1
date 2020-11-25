
from django.http import JsonResponse
from django.shortcuts import *
from django.views.generic import *
from django.urls import *
from listapp1.models import *
from listapp1.forms import *

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser, FileUploadParser
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from listapp1.models import *
from listapp1.serializers import *
import pyfacebook

from facebook import GraphAPI


class createEmployee(TemplateView):
    form_class=Employeecreateform
    model_name=Employee1
    template_name = "listapp1/Employeecreate.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            Name = form.cleaned_data["Name"]
            Telephone = form.cleaned_data["Telephone"]
            Age = form.cleaned_data["Age"]
            # if 'Profile_pic' in request.FILES:
            #     Profile_pic = request.FILES['Profile_pic']
            # Profile_pic = form.cleaned_data["Profile_pic"]
            Email = form.cleaned_data["Email"]
            Emptype = form.cleaned_data["Emptype"]
            Username = form.cleaned_data["Username"]
            Password = form.cleaned_data["Password"]
            # isActive=True
            qs = Employee.objects.create(Name=Name, Telephone=Telephone,Age=Age,Emptype=Emptype,\
                    Email=Email,Username=Username,Password=Password,isActive=True)
            print("d1")
            # form.save(commit=False)
            print("d2")
            qs.save()
            print("d3")
            return JsonResponse({"message": "loginSuccess", 'status': 200})

        else:
            return render(request, self.template_name,{"form":form})

class loginEmployee(TemplateView):
    form_class=Employeelogin
    model_name=Employee1
    template_name = "listapp1/Employeelogin.html"
    template_name1 = "listapp1/home.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        print("Hi0000")
        if form.is_valid():
            print("Hi1111")
            Telephone = form.cleaned_data["Telephone"]
            Password = form.cleaned_data["Password"]
            qs=Employee1.objects.get(Telephone=Telephone)
            print("Hi")
            print("Active:",qs.isActive)
            if((qs.Telephone==Telephone)&(qs.Password==Password)):
                request.session['Telephone']=Telephone
                context = {}
                context["qs"] = qs
                print(qs)
                print(context)
                # context["user"] = user
                print("hiiiiiiiiiiiiii")
                return render(request, self.template_name1, context)
                # return HttpResponseNotFound('<h1>Page not found</h1>')
            else:
                print("Hi2222")
                return redirect("User_login")
                # return HttpResponse('<h1>Page was not found</h1>')

        else:
            print("Hi33333")
            return render(request, self.template_name,{"form":form})

class viewEmployee(TemplateView):
    model_name=Employee1
    template_name = "listapp1/Employeeview.html"
    # Username = request.session["Username"]
    # def get_queryset(self):
    #
    #     return self.model_name.objects.filter(Username=request.session["Username"])
    def get(self, request, *args, **kwargs):
        # form.fields['Paymode'].queryset = Account.objects.filter(Username=request.session["Username"])
        qs=Employee1.objects.all()
        print("ddddd")
        context={}
        print(context)
        context["viewemployee"]=qs
        print(context)
        return render(request,self.template_name,context)

def logoutEmployee(request):
        del request.session['Telephone']
        return redirect("Employee_login")
class updateEmployee(UpdateView):
    model=Employee1
    fields = ["Name", "Telephone", "Age",  "Email", "Username", "Password","Emptype"]
    success_url = '/Employeeview'
    # success_url = reverse_lazy('getRes')
    #context_object_name = "form"
    template_name = 'listapp1/Employee_update.html'
class deleteEmployee(DeleteView):
    model = Employee1
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    fields = ["Name", "Telephone", "Age",  "Email", "Username", "Password","Emptype"]
    # template_name_suffix = "_del"
    success_url = '/Employeeview'
class EmployeeList(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self,request):
        serializer = EmployeeSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.data, status=400)

class EmployeeListCreateAPIView(ListCreateAPIView):
    parser_class = (FileUploadParser,)
    serializer_class =  EmployeeSerializer
    queryset = Employee1.objects.all()

    def get(self, request, *args, **kwargs):
        documents = Employee1.objects.all()
        serializer = EmployeeSerializer(documents,many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, *args, **kwargs):

        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)