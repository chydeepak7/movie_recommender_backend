import numpy as np
from rest_framework import serializers

class RecommendationSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    tags = serializers.CharField()


class RecommendMovieSerializer(serializers.Serializer):
    title = serializers.CharField()

