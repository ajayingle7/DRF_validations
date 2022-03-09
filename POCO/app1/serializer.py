from rest_framework import serializers
from .models import Employee


def eid_validation(value):
    if value<1:
        raise serializers.ValidationError("eid must above 1")



class EmployeeSerialzier(serializers.ModelSerializer):
    eid = serializers.IntegerField(validators=[eid_validation,])
    class Meta:
        model = Employee
        fields = "__all__"


    def validate_esal(self,value):
        if value<5000:
            raise serializers.ValidationError("salary should above 5000")
        return value

    def validate_email(self,value):

        tupl= ("gmail.com","yahoo.com","email.com","reddit.com")
        a = value.endswith(tupl)

        if a!=True:
            raise serializers.ValidationError("email invalid")

        return value


