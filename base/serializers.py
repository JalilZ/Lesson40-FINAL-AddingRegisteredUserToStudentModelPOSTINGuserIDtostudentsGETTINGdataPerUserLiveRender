# https://www.django-rest-framework.org/api-guide/serializers/   # Serializer: django-rest-framework documentation

from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # Serializer classes can also include reusable validators that are applied to the complete set of field data. 
    # These validators are included by declaring them on an inner Meta class, like so:
    class Meta:
        model = Student
        fields = '__all__'
        
    def create(self, validated_data):                               # Adding Registered User ID to student model (Django4kids Getting data per user) we add this so the post actually updates the database (save is required afterwards)
       user = self.context['user']                                  # Adding Registered User ID to student model (Django4kids Getting data per user) we add this so the post actually updates the database (save is required afterwards)
       print(user)                                                  # Adding Registered User ID to student model (Django4kids Getting data per user) we add this so the post actually updates the database (save is required afterwards)
       return Student.objects.create(**validated_data, user=user)   # Adding Registered User ID to student model (Django4kids Getting data per user) we add this so the post actually updates the database (save is required afterwards)



# the below is NOT requied !        
        #fields = ['name','age', 'createdTime'] # also works

    #def create(self, validated_data):  
    #    return Student.objects.create(**validated_data) 
    # no need for create, because if we instantiate TaskSerializer object, 
    # an object will be created in the Table (but we should save() for it to be actually created)
    
    #def update(self, instance, validated_data):
    #instance.name = validated_data.get('name', instance.name)
    #instance.age = validated_data.get('age', instance.age)
    #instance.save()
    #return instance
    # no need for update ! it is already a method in StudentSerializer!!!!!!!!!!!!