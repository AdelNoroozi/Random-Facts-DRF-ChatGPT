# Introduction
<img src="https://raw.githubusercontent.com/AdelNoroozi/Random-Facts-DRF-ChatGPT/main/resources/banner.jpg" width="400" >
This is a small project for generating random facts using GPT APIs. Users enter a topic and gets a random fact about that. The facts store in database and other users can read them. 

This operations do not need authentication. only admins need to authenticate for managing facts.

# Tools
<img src="https://raw.githubusercontent.com/AdelNoroozi/Random-Facts-DRF-ChatGPT/main/resources/python-icon.png" heigth="32" >
<img src="https://raw.githubusercontent.com/AdelNoroozi/Random-Facts-DRF-ChatGPT/main/resources/django-icon.png" heigth="32" >
<img src="https://raw.githubusercontent.com/AdelNoroozi/Random-Facts-DRF-ChatGPT/main/resources/openai-icon.png" heigth="32" >
<img src="https://raw.githubusercontent.com/AdelNoroozi/Random-Facts-DRF-ChatGPT/main/resources/django-rest-icon.png" heigth="32" >
<img src="https://raw.githubusercontent.com/AdelNoroozi/Random-Facts-DRF-ChatGPT/main/resources/jwt-icon.png" heigth="31" >

# Description
Users (unauthenticated):
  
  ● Generating new facts by a given topic
  
  ● Saving the fact by a custom name (facts that are too similar to existing facts don't get saved)
  
  ● Geting a list of all existing facts
  
Admin

  Authentication
  
   ● Change their password
  
  ● Change ther information
  
  ● Login (get JWT token)
  
  Managing facts

  ● Viewing all existing facts
  
  ● Deleting existing facts
  
SuperUser

  ● All admin accesses
  
  ● Adding new admins
