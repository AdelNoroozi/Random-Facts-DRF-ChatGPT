from django.shortcuts import render
import openai
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from facts.models import Fact
from facts.serializers import FactSerializer


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
        openai.api_key = "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"
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
        fact = Fact.objects.create(topic=topic, fact=fact_text, creator=creator)
        serializer = FactSerializer(fact)
        return Response(serializer.data, status=status.HTTP_200_OK)
