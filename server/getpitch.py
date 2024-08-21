import os
from dotenv import load_dotenv, find_dotenv
from groq import Groq
import asyncio
from groq import AsyncGroq
import nest_asyncio
nest_asyncio.apply()
from openai import AsyncClient
import json
import re


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

audience_age_group = (25,35)
speech_time ="2mins"
product_summary= " TCL 55\ Class 4-Series 4K UHD Smart Roku TV (55S455) Cost:- The current price of the TCL 55 Class 4-Series 4K UHD Smart Roku TV is $363.01 on Amazon. Size:- The screen size is 55 inches. Pros:- *Picture Quality: The TV offers stunning 4K Ultra HD with excellent brightness and contrast.\\n- **Value for Money: It provides a great value for its price, making it a budget-friendly option.- **Streaming Apps: Includes all major streaming apps, including HBO Max.- **Ease of Use: The Roku OS is user-friendly and easy to navigate. Cons:- **Remote Control: Some users find the remote control to be less user-friendly compared to other models.- **Sound Quality: The built-in speakers are decent but may not be sufficient for those who prefer better sound quality. Reviews:- **Customer Reviews: The TV has a 4.4 out of 5-star rating on Best Buy, with many users praising its picture quality and value for money.- **Overall Satisfaction: Users generally find the TV to be a great budget option, with some minor complaints about the remote control and sound quality. TCL 55\\\" Class 4-Series LED 4K UHD Smart Android TV (55S434) Cost:- The current price of the TCL 55\\\" Class 4-Series LED 4K UHD Smart Android TV is around $200 on Best Buy. Size:- The screen size is 55 inches.\\n\\n#### Pros:\\n- **Picture Quality: Users praise the excellent picture quality and brightness of the TV.\\n- **Price: The TV offers great value for its price, making it an excellent budget option.\\n- **Streaming Apps: Includes all major streaming apps, including HBO Max. Cons:\\n- **Remote Control: Some users find the remote control to be less user-friendly compared to other models.\\n- **Sound Quality: The built-in speakers are decent but may not be sufficient for those who prefer better sound quality.\\n\\n#### Reviews:\\n- **Customer Reviews: The TV has a 4.4 out of 5-star rating on Best Buy, with many users praising its picture quality and value for money.\\n- **Overall Satisfaction: Users generally find the TV to be a great budget option, with some minor complaints about the remote control and sound quality.\\n\\n### TCL 55\\\" 4K UHD Smart TV (55R646)\\n\\n#### Cost:\\n- The current price of the TCL 55\\\" 4K UHD Smart TV is around $949.99 on PCMag.\\n\\n#### Size:\\n- The screen size is 55 inches.\\n\\n#### Pros:\\n- **Picture Quality: The TV offers strong performance with excellent contrast and color accuracy.\\n- **Streaming Apps: Includes all major streaming apps, including Google Cast and hands-free Google Assistant.\\n- **Gaming Features: Supports 120Hz refresh rate and VRR, making it suitable for gaming.\\n\\n#### Cons:\\n- **Software Instability: There have been reports of software instability, although TCL has released updates to address this issue.\\n- **Input Lag: Some users have noted lower input lag, which is beneficial for gaming.\\n\\n#### Reviews:\\n- **Editor's Choice: The TV has earned an Editor's Choice award for its strong performance and features.\\n- **Overall Satisfaction*: Users praise the TV's picture quality, contrast, and color accuracy, but some have noted issues with software stability. In summary, the TCL 55\\\ Class 4-Series 4K UHD Smart Roku TV and the TCL 55\\\ Class 4-Series LED 4K UHD Smart Android TV are both excellent budget options, offering great picture quality and value for money. The TCL 55\\\ 4K UHD Smart TV (55R646) is a more premium model with strong performance and features, but it has had some issues with software stability.\n"
model_names = ["llama3-8b-8192" ,"mixtral-8x7b-32768", "gemma-7b-it"]


async def get_completion(client, model):
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You give product review pitches for social media content creators. You should provide the pitch only based on the product summary provided. You will tailor the speech for the audience type. Your content size depends on the speech time provided."
            },
            {
                "role": "user",
                "content": f"Audience Type: {audience_age_group}, Speech Time: {speech_time}, Product Summary: {product_summary}"

            }
        ],
        model=model,
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
    )
    return chat_completion.choices[0].message.content

async def chat_gpt_completion(client, model):
  chat_completion = await client.chat.completions.create(
      messages=[
            {
                "role": "system",
                "content": "You give product review pitches for social media content creators. You should provide the pitch only based on the product summary provided. You will tailor the speech for the audience type. Your content size depends on the speech time provided."
            },
            {
                "role": "user",
                "content": f"Audience Type: {audience_age_group}, Speech Time: {speech_time}, Product Summary: {product_summary}"

            }
        ],
        model=model,
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
    )
  return chat_completion.choices[0].message.content

def clean_text(text):
    # Remove unwanted characters and emojis
    text = re.sub(r'\\n', ' ', text)  # Replace \n with space
    text = re.sub(r'\\u[0-9A-Fa-f]{4}', '', text)  # Remove unicode characters
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Remove non-ASCII characters
    text = re.sub(r'\s+', ' ', text).strip()  # Replace multiple spaces with a single space and trim

    return text

async def main():
    client = AsyncGroq(api_key=groq_api_key)
    tasks = [get_completion(client, model) for model in model_names]
    tasks.append(chat_gpt_completion(AsyncClient(api_key=api_key), "gpt-4o"))
    results = await asyncio.gather(*tasks)
    model_names.append("gpt_4o")
    # for model, result in zip(model_names, results):
    #     print(f"Model: {model}\nCompletion: {result}\n")
    # Clean the results
    cleaned_results = {model: clean_text(result) for model, result in zip(model_names, results)}
    
    # Save the cleaned results to a JSON file
    with open('results.json', 'w') as f:
        json.dump(cleaned_results, f, indent=4)
    
    return cleaned_results

results = asyncio.run(main())
