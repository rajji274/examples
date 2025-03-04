from application.models import Register
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=['id','firstname','lastname','dateofbirth','gender','emailid','password','mobilenumber','role','securityquestion','securityanswer','securityquestion1','securityanswer1','securityquestion2','securityanswer2']
