from rest_framework import serializers

from main.models import Station


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station