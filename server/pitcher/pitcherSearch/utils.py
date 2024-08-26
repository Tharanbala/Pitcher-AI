import requests
import environ
import json

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