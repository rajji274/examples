
from rest_framework import serializers
from .models import registration

class registerserializer(serializers.ModelSerializer):
    firstname=serializers.CharField(required=True,max_length=100)
    lastname=serializers.CharField(required=True,max_length=100)
    emailid=serializers.EmailField(required=True,max_length=100)
    password=serializers.CharField(required=True,max_length=100)
    dateofbirth=serializers.DateField(required=True)
    mobilenumber=serializers.CharField(required=True,max_length=100)
    role=serializers.CharField(required=True,max_length=100)
    gender=serializers.CharField(required=True,max_length=100)
    question=serializers.CharField(required=True,max_length=100)
    answer=serializers.CharField(required=True,max_length=100)
    question1=serializers.CharField(required=True,max_length=100)
    answer1=serializers.CharField(required=True,max_length=100)
    question2=serializers.CharField(required=True,max_length=100)
    answer2=serializers.CharField(required=True,max_length=100)

    
    
    def create(self,validated_data):
        return registration.objects.create(**validated_data)

    def update(self, instance,validated_data):
        instance.firstname=validated_data.get('firstname',instance.firstname)
        instance.lastname=validated_data.get('lastname',instance.lastname)
        instance.emailid=validated_data.get('emailid',instance.emailid)
        instance.password=validated_data.get('password',instance.password)
        instance.dateofbirth=validated_data.get('dateofbirth',instance.dateofbirth)
        instance.mobilenumber=validated_data.get('mobilenumber',instance.mobilenumber)
        instance.role=validated_data.get('role',instance.role)
        instance.gender=validated_data.get('gender',instance.gender)
        instance.question=validated_data.get('question',instance.question)
        instance.answer=validated_data.get('answer',instance.answer)
        instance.question1=validated_data.get('question1',instance.question1)
        instance.answer1=validated_data.get('answer1',instance.answer1)
        instance.question2=validated_data.get('question2',instance.question2)
        instance.answer2=validated_data.get('answer2',instance.answer2)

        instance.save()
        return instance

    class Meta:
        model=registration
        fields=('firstname','lastname','emailid','password','dateofbirth','mobilenumber','role','gender','question','answer','question1','answer1','question2','answer2')