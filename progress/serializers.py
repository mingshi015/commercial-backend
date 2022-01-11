from rest_framework import serializers
from progress.models import Commercial


class CommercialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commercial
        fields = [
            'id',
            'session_id',
            'step',
            'address',
            'experience',
            'first_name',
            'last_name',
            'company_name',
            'email',
            'phone',
            'created'
        ]
