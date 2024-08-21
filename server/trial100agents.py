import random
import requests
import openai

# Placeholder API keys - replace with your actual keys
GROQ_API_KEY = "your_groq_api_key"
GPT4_API_KEY = "your_gpt4_api_key"

# Set the OpenAI API key
openai.api_key = GPT4_API_KEY

# Groq API URLs - replace these with the actual endpoints if different
LLAMA_API_URL = "https://api.groq.com/v1/llama/completions"
GEMMA_API_URL = "https://api.groq.com/v1/gemma/completions"

# Define a list of professions
PROFESSIONS = ["teacher", "barber", "dancer", "engineer", "doctor", "artist", "chef", "writer", "nurse", "lawyer", "musician", "actor", "scientist", "pilot"]

# Function to get response from Llama (using Groq)
def get_response_from_llama(pitch, age, profession):
    payload = {
        "model": "llama-3.1",
        "prompt": f"You are a {age}-year-old {profession}. The following is a marketing pitch: '{pitch}'. Would you buy this product? Please respond with 'Yes' or 'No' and explain why.",
        "max_tokens": 50
    }
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(LLAMA_API_URL, headers=headers, json=payload)
    result = response.json()
    text_response = result['choices'][0]['text'].strip().lower()
    return "yes" in text_response

# Function to get response from GPT-4 (using OpenAI API)
def get_response_from_gpt4(pitch, age, profession):
    response = openai.Completion.create(
        model="gpt-4",
        prompt=f"You are a {age}-year-old {profession}. The following is a marketing pitch: '{pitch}'. Would you buy this product? Please respond with 'Yes' or 'No' and explain why.",
        max_tokens=50,
        temperature=0.7,
    )
    text_response = response['choices'][0]['text'].strip().lower()
    return "yes" in text_response

# Function to get response from Gemma (using Groq)
def get_response_from_gemma(pitch, age, profession):
    payload = {
        "model": "gemma-2.0",
        "prompt": f"You are a {age}-year-old {profession}. The following is a marketing pitch: '{pitch}'. Would you buy this product? Please respond with 'Yes' or 'No' and explain why.",
        "max_tokens": 50
    }
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(GEMMA_API_URL, headers=headers, json=payload)
    result = response.json()
    text_response = result['choices'][0]['text'].strip().lower()
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

# Define the marketing pitch
marketing_pitch = "Introducing the ultimate gadget to simplify your life..."

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


# Define age categories (example: young adults)
age_category = (25, 35)  # Customize this as needed

# Create an audience of 100 people
audience = create_audience(100, age_category, PROFESSIONS)

# Get responses
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
