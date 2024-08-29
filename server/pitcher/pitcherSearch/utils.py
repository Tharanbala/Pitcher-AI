import requests
import environ
import json
from .getPitch import PitchGenerator
import asyncio


env = environ.Env()
environ.Env.read_env()

def getPerplex(product):
    url = "https://api.perplexity.ai/chat/completions"
    api_key = env("PERPLEX_API_KEY")
    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {
                "role": "system",
                "content": "You are an intelligent assistant who surfs the internet and gain insights on products for pro/cons and reviews of the product."
            },
            {
                "role": "user",
                "content": f"What is the cost, dimensions, pros, cons, reviews and stars of {product}"
            }
        ]
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "accept": "application/json",
        "Content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    # # Parsing and converting to the desired format
    # content = response.text["choices"][0]["message"]["content"]

    # # Extracting information
    # lines = content.strip().splitlines()
    # price_line = next(line for line in lines if "starting price" in line.lower())
    # dimensions_line = next(line for line in lines if "dimensions" in line.lower() or "size" in line.lower())
    # weight_line = next(line for line in lines if "weight" in line.lower())

    # # Extracting price
    # price = int(price_line.split('$')[-1].split()[0].replace(',', ''))

    # # Extracting dimensions and weight
    # dimensions = {
    #     "length": float(dimensions_line.split(':')[1].split('x')[0].strip()),
    #     "width": float(dimensions_line.split('x')[1].strip().split(' ')[0]),
    #     "height": float(dimensions_line.split('x')[2].strip().split(' ')[0]),
    #     "weight": float(weight_line.split(':')[1].strip().split(' ')[0])
    # }

    # # Extracting pros and cons
    # pros = [line.split("**")[2] for line in lines if line.strip().startswith("1.") and "**" in line]
    # cons = [line.split("**")[2] for line in lines if line.strip().startswith("1. **")]

    # # Extracting reviews
    # reviews = []
    # review_lines = [line for line in lines if "- **" in line]
    # for line in review_lines:
    #     parts = line.split(":")
    #     reviewer = parts[0].replace("- **", "").replace("**", "").strip()
    #     summary = ":".join(parts[1:]).strip()
    #     reviews.append({
    #         "reviewer": reviewer,
    #         "summary": summary
    #     })

    # # Setting up the final JSON
    # final_json = {
    #     "name": product,
    #     "price": price,
    #     "dimensions": dimensions,
    #     "pros": pros,
    #     "cons": cons,
    #     "reviews": reviews,
    #     "stars": 4  # Average rating is not directly available in the input
    # }

    # # Printing the final JSON structure
    # result = json.dumps(final_json, indent=2)
    # print(result)
    return response.text

def getPitch(product_summary):
    pitch_generator = PitchGenerator(api_key=env("OPENAI_API_KEY"), groq_api_key=env("GROQ_API_KEY"),
                                             model_names=["llama3-8b-8192", "mixtral-8x7b-32768", "gemma-7b-it"])
    return asyncio.run(pitch_generator.generate_pitch(product_summary))


if __name__ == "__main__":
    # product_summary = " TCL 55\ Class 4-Series 4K UHD Smart Roku TV (55S455) Cost:- The current price of the TCL 55 Class 4-Series 4K UHD Smart Roku TV is $363.01 on Amazon. Size:- The screen size is 55 inches. Pros:- *Picture Quality: The TV offers stunning 4K Ultra HD with excellent brightness and contrast.\\n- **Value for Money: It provides a great value for its price, making it a budget-friendly option.- **Streaming Apps: Includes all major streaming apps, including HBO Max.- **Ease of Use: The Roku OS is user-friendly and easy to navigate. Cons:- **Remote Control: Some users find the remote control to be less user-friendly compared to other models.- **Sound Quality: The built-in speakers are decent but may not be sufficient for those who prefer better sound quality. Reviews:- **Customer Reviews: The TV has a 4.4 out of 5-star rating on Best Buy, with many users praising its picture quality and value for money.- **Overall Satisfaction: Users generally find the TV to be a great budget option, with some minor complaints about the remote control and sound quality. TCL 55\\\" Class 4-Series LED 4K UHD Smart Android TV (55S434) Cost:- The current price of the TCL 55\\\" Class 4-Series LED 4K UHD Smart Android TV is around $200 on Best Buy. Size:- The screen size is 55 inches.\\n\\n#### Pros:\\n- **Picture Quality: Users praise the excellent picture quality and brightness of the TV.\\n- **Price: The TV offers great value for its price, making it an excellent budget option.\\n- **Streaming Apps: Includes all major streaming apps, including HBO Max. Cons:\\n- **Remote Control: Some users find the remote control to be less user-friendly compared to other models.\\n- **Sound Quality: The built-in speakers are decent but may not be sufficient for those who prefer better sound quality.\\n\\n#### Reviews:\\n- **Customer Reviews: The TV has a 4.4 out of 5-star rating on Best Buy, with many users praising its picture quality and value for money.\\n- **Overall Satisfaction: Users generally find the TV to be a great budget option, with some minor complaints about the remote control and sound quality.\\n\\n### TCL 55\\\" 4K UHD Smart TV (55R646)\\n\\n#### Cost:\\n- The current price of the TCL 55\\\" 4K UHD Smart TV is around $949.99 on PCMag.\\n\\n#### Size:\\n- The screen size is 55 inches.\\n\\n#### Pros:\\n- **Picture Quality: The TV offers strong performance with excellent contrast and color accuracy.\\n- **Streaming Apps: Includes all major streaming apps, including Google Cast and hands-free Google Assistant.\\n- **Gaming Features: Supports 120Hz refresh rate and VRR, making it suitable for gaming.\\n\\n#### Cons:\\n- **Software Instability: There have been reports of software instability, although TCL has released updates to address this issue.\\n- **Input Lag: Some users have noted lower input lag, which is beneficial for gaming.\\n\\n#### Reviews:\\n- **Editor's Choice: The TV has earned an Editor's Choice award for its strong performance and features.\\n- **Overall Satisfaction*: Users praise the TV's picture quality, contrast, and color accuracy, but some have noted issues with software stability. In summary, the TCL 55\\\ Class 4-Series 4K UHD Smart Roku TV and the TCL 55\\\ Class 4-Series LED 4K UHD Smart Android TV are both excellent budget options, offering great picture quality and value for money. The TCL 55\\\ 4K UHD Smart TV (55R646) is a more premium model with strong performance and features, but it has had some issues with software stability.\n"
    product_summary = getPerplex("TCL 55")
    print(product_summary)
    result = getPitch(product_summary)
    print("\n***********************************************************************************\n")
    print(result)
    