from rest_framework import serializers
from seminarioApi.models import seminario

class seminarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = seminario
        fields = '__all__'
