from rest_framework import serializers

from facts.models import Fact


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = ('id', 'topic', 'fact', 'created_at', 'creator')
        read_only_fields = ('id',)
