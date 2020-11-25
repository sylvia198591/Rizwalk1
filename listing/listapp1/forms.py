from django.forms import ModelForm
from listapp1.models import *
from django  import forms

class Employeecreateform(ModelForm):
    Confirmpassword = forms.CharField(max_length=200, widget=forms.PasswordInput)
    class Meta:
        widgets = {
            'Password': forms.PasswordInput(render_value=True),
        }
        model = Employee1
        fields = ["Name", "Telephone", "Age",  "Email", "Username", "Password", "Confirmpassword","Emptype"]
        # fields = ["Name", "Telephone","Age","Profile_pic", "Email", "Username", "Password","Confirmpassword"]
    def clean(self):
        cleaned_data=super().clean() #mandatory
        Name=cleaned_data.get("Name")
        Telephone=cleaned_data.get("Telephone")
        Age = cleaned_data.get("Age")
        Email=cleaned_data.get("Email")
        Emptype = cleaned_data.get("Emptype")
        # Profile_pic=cleaned_data.get("Profile_pic")
        Username=cleaned_data.get("Username")
        Password=cleaned_data.get("Password")
        Confirmpassword=cleaned_data.get("Confirmpassword")

        if Password!=Confirmpassword:
            msg="Pls enter a valid password"
            self.add_error("Password",msg)

class Employeelogin(forms.Form):
    Telephone=forms.CharField(max_length=200,)
    Password=forms.CharField(max_length=200, widget=forms.PasswordInput)
    class Meta:
        widgets = {
            'Password': forms.PasswordInput(render_value=True),
        }
        model=Employee1
        fields=['Telephone','Password',]

    def clean(self):
        cleaned_data=super().clean() #mandatory
        Username = cleaned_data.get("Username")

class fbupdateform(forms.Form):
    message = forms.CharField(max_length=200, )

    class Meta:

        model = Employee1
        fields = ['message']

    def clean(self):
        cleaned_data = super().clean()  # mandatory
        message = cleaned_data.get("message")

# class pgdtlform(ModelForm):
#     # Confirmpassword = forms.CharField(max_length=200, widget=forms.PasswordInput)
#     class Meta:
#         # widgets = {
#         #     'Password': forms.PasswordInput(render_value=True),
#         # }
#         model = pgdtl
#         fields = ["pagename", "pageid", "pagecategory"]
#         # fields = ["Name", "Telephone","Age","Profile_pic", "Email", "Username", "Password","Confirmpassword"]
#     def clean(self):
#         cleaned_data=super().clean() #mandatory
#         pagename=cleaned_data.get("pagename")
#         pageid=cleaned_data.get("pageid")
#         pagecategory = cleaned_data.get("pagecategory")