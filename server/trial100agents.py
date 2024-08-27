import random
from openai import OpenAI
import groq
import os
import json
from dotenv import load_dotenv, find_dotenv
from server.pitcher.PitchGenerate.getpitch import *

# Set the OpenAI API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Debug prints to verify API keys
print(f"OPENAI_API_KEY: {OPENAI_API_KEY}")
print(f"GROQ_API_KEY: {GROQ_API_KEY}")

# Ensure the keys are loaded correctly
if not OPENAI_API_KEY or not GROQ_API_KEY:
    raise ValueError("API keys are not set properly in the environment variables")

# Define a list of professions
PROFESSIONS = ["teacher", "barber", "dancer", "engineer", "doctor", "artist", "chef", "writer", "nurse", "lawyer", "musician", "actor", "scientist", "pilot"]

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def get_response_from_llama(pitch, age, profession):
 
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": f"You are a {age}-year-old {profession}. The following is a marketing pitch: '{pitch}'. Would you buy this product? Please respond with 'Yes' or 'No' and explain why."
            }
        ],
        temperature=1,
        max_tokens=50,
        top_p=1,
        stream=False
    )
    text_response = response.choices[0].message.content.strip().lower()
    return "yes" in text_response

clients = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
def get_response_from_gpt4(pitch, age, profession):
    response = clients.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": f"You are a {age}-year-old {profession}. The following is a marketing pitch: '{pitch}'. Would you buy this product? Please respond with 'Yes' or 'No' and explain why."
            }
        ],
        temperature=0.7,
        max_tokens=50,
        top_p=1,
        stream=False
    )
    text_response = response.choices[0].message.content.strip().lower()
    return "yes" in text_response

def get_response_from_gemma(pitch, age, profession):
    
    response = client.chat.completions.create(
        model="gemma-7b-it",
        messages=[
            {
                "role": "system",
                "content": f"You are a {age}-year-old {profession}. The following is a marketing pitch: '{pitch}'. Would you buy this product? Please respond with 'Yes' or 'No' and explain why."
            }
        ],
        temperature=1,
        max_tokens=50,
        top_p=1,
        stream=False
    )
    text_response = response.choices[0].message.content.strip().lower()
    return "yes" in text_response

# Function to create an audience member
def create_audience_member(age_category, professions):
    age = random.randint(age_category[0], age_category[1])
    profession = random.choice(professions)
    llm = random.choice(['llama', 'gpt4', 'gemma'])
    return {
        "age": age,
        "profession": profession,
        "llm": llm
    }

# Create the audience
def create_audience(num_people, age_category, professions):
    return [create_audience_member(age_category, professions) for _ in range(num_people)]

# Get the response from the audience
def get_audience_responses(audience, pitch):
    responses = []
    for person in audience:
        age = person['age']
        profession = person['profession']
        llm = person['llm']
        
        if llm == 'llama':
            response = get_response_from_llama(pitch, age, profession)
        elif llm == 'gpt4':
            response = get_response_from_gpt4(pitch, age, profession)
        elif llm == 'gemma':
            response = get_response_from_gemma(pitch, age, profession)
        
        responses.append({
            "age": age,
            "profession": profession,
            "response": response
        })
    return responses

# Load the marketing pitches from results.json
with open('results.json', 'r') as f:
    marketing_pitches = json.load(f)

# Define age categories (example: young adults)
age_category = (18, 35)  # Customize this as needed

# Create an audience of 100 people
audience = create_audience(100, age_category, PROFESSIONS)

# Get responses for each marketing pitch
for model, marketing_pitch in marketing_pitches.items():
    print(f"Evaluating pitch for model: {model}")
    audience_responses = get_audience_responses(audience, marketing_pitch)

    # Analyze the results
    true_count = sum(1 for response in audience_responses if response['response'] == True)
    false_count = len(audience_responses) - true_count

    # Output the results
    print(f"Number of people who would buy the product: {true_count}")
    print(f"Number of people who would not buy the product: {false_count}")

    # Optional: Print detailed responses
    for response in audience_responses:
        print(f"Age: {response['age']}, Profession: {response['profession']}, Would Buy: {response['response']}")