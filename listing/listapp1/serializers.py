from rest_framework.serializers import ModelSerializer
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from listapp1.models import pgdtl
from listapp1.models import Employee
class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

class pgdtlserializer(ModelSerializer):

    class Meta:
        model = pgdtl
        fields = '__all__'