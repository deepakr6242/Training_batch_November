from rest_framework import serializers 
from pylabz.models import Contact
 
 
class ContactSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Contact
        fields = ('id',
                  'firstname',
                  'email',
                  )