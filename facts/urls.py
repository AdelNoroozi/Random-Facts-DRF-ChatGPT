from django.urls import path

from facts.views import GenerateFact

urlpatterns = [
    path('generate-fact/', GenerateFact.as_view(), name='generate_fact')
]
