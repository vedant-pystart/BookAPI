import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY") 

max_tokens = 500
temperature = 0.7
engine = "text-davinci-003"

# malelead = input("Enter info for the male lead: ")
# femalelead = input("Enter info for the female lead: ")
# director = input("Enter the director: ")

malelead = "Shah Rukh Khan"
femalelead = "Deepika Padukone"
director = "Aditya Chopra"

print(f"\n Success! Your information is: \n Male Lead: {malelead} \n Female Lead: {femalelead} \n Director: {director}" )

prompt = f"Write a short, roughly 10 sentence script idea given the male bollywood lead, {malelead}, female lead, {femalelead}, and the director, {director}, based on what kind of movies the director has made in the past. Also give a list of the locations the movie would be shot in for songs, the names of the songs, and justification for the movie based on the director at the start"

