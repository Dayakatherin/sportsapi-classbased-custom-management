from rest_framework import serializers
from .models import sports
class sportsSerializer(serializers.ModelSerializer):

      class Meta:
          model = sports
          fields = '__all__'