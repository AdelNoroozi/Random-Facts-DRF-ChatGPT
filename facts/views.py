from django.shortcuts import render
import openai
from rest_framework import status, mixins
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from facts.models import Fact
from facts.serializers import FactSerializer
from difflib import SequenceMatcher


class GenerateFact(APIView):
    def post(self, request):
        try:
            topic = request.data['topic']
            frequency = int(request.data['frequency'])
            creator = request.data['creator']
        except:
            response = {'message': 'field error!'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        if frequency == 1:
            new_fact_flag = "a"
        elif frequency == 2:
            new_fact_flag = "another"
        elif frequency == 3:
            new_fact_flag = "a new"
        else:
            response = {'message': 'invalid frequency!'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        openai.api_key = ""
        openai.Model.list()
        ai_response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f'tell me {new_fact_flag} random fun fact about {topic}',
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        fact_text = (ai_response['choices'][0]['text']).strip()
        # fact = Fact.objects.create(topic=topic, fact=fact_text, creator=creator)
        try:
            last_fact_id = request.data['last_fact_id']
        except:
            fact = Fact.objects.create(topic=topic, fact=fact_text, creator=creator)
            serializer = FactSerializer(fact)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            if not Fact.objects.filter(id=last_fact_id).exists():
                response = {'message': 'last fact id is invalid!'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                last_fact = Fact.objects.get(id=last_fact_id)
                facts_similarity = SequenceMatcher(None, fact_text, last_fact.fact).ratio()
                if facts_similarity >= 0.6:
                    response = {'message': 'sorry, no more facts available!'}
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)
                else:
                    fact = Fact.objects.create(topic=topic, fact=fact_text, creator=creator)
                    serializer = FactSerializer(fact)
                    return Response(serializer.data, status=status.HTTP_200_OK)


class FactViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer
