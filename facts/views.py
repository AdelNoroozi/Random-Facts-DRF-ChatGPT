from django.shortcuts import render
import openai

from rest_framework.views import APIView


class GenerateFact(APIView):
    def post(self, request):
        topic = request.data['topic']
        openai.api_key = ""
        openai.Model.list()
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f'tell me a random fact about {topic}',
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
