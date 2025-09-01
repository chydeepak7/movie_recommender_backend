from django.shortcuts import render
import pickle
import requests
from rest_framework.response import Response
from .serializers import RecommendationSerializer
import os
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.

import gdown

FILE_PATH = "similarity.pkl"
FILE_ID = "1uFnK_xAVGskF3sjrdCHf-E3nnXGb8LOT"
URL = f"https://drive.google.com/uc?id={FILE_ID}"

# Download if not exists
if not os.path.exists(FILE_PATH):
    gdown.download(URL, FILE_PATH, quiet=False)

# Load similarity
similarity = pickle.load(open(FILE_PATH, "rb"))

movies_list = pickle.load(open('movies.pkl' , 'rb'))
# movies_list = movies_list['title'].values
# print(movies_list['title'][0])
# print(similarity)

@api_view(['GET'])
def movie_list(request):
    recommendations = movies_list.to_dict(orient='records')
    serializer = RecommendationSerializer(recommendations, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def recommend_movie(request, movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_recomm = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:10]
    final = []
    for i in movies_recomm:
        final.append(movies_list.iloc[i[0]].title)
    return Response(final)

