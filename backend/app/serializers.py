from rest_framework import serializers

from . import models


class DatasourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Datasource
        fields = '__all__'


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Campaign
        fields = '__all__'


class DayStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DayStats
        fields = ('id', 'date', 'clicks', 'impressions', 'datasource', 'campaign')

    datasource = DatasourceSerializer()
    campaign = CampaignSerializer()
