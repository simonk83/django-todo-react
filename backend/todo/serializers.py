
# todo/serializers.py

from rest_framework import serializers
from .models import Todo
      
class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = '__all__' #('id', 'title', 'description', 'completed', 'owner_lan', 'sme_lan', 'campus', 'workstream', 'ops_area', 'criticality', 'supported_by', 'euc_id', 'password', 'tool_platform', 'completed')