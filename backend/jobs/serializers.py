from rest_framework import serializers
from .models import Job
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'id', 'title', 'company_name', 'location', 'description',
            'requirements', 'posted_date', 'apply_link'
        ]