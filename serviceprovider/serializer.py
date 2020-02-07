from rest_framework import serializers
from .models import *

class SPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serviceprovider
        fields = ['usertype', 'full_name', 'email', 'password', 'mobile'] 
        extra_kwargs = {
            'password':{
                'style':{'input_type' : 'passord'}
            }
        }
    
    def create(self, validated_data):
        spobj = Serviceprovider.objects.create(
            usertype = validated_data['usertype'],
            full_name = validated_data['full_name'],
            email = validated_data['email'],
            password = validated_data['password'],
            mobile = validated_data['mobile'],
            services = [],
            appliedservices = []
        )
        return spobj