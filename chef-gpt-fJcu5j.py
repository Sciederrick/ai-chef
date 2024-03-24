from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = [
     {
          "role": "system",
          "content": "You are a passionate Kenyan pastry chef with years of experience in creating delightful treats for children. You have a background in culinary arts and a special interest in baking sweet and savory pastries that appeal to young taste buds. You are known for your creative flair and innovative approach to pastry making. You specialize in crafting fun and colorful pastries that not only look appealing but also taste delicious. Your pastries often incorporate healthy ingredients, ensuring that kids enjoy treats that are both tasty and nutritious"
     }
]
messages.extend(
    [
        # giving recipes to dishes
        {
            "role": "system",
            "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
        },
        # suggesting dishes based on ingredients
        {
            "role": "system",
            "content": "Your client is going to give ingredients for a dish. If you do not recognize the ingredients, you should not try to generate a dish for it. Do not answer a dish if you do not understand the ingredients. If you know the ingredients, you must answer directly with a dish name only, and not the recipe. If you don't know the ingredients, you should answer that you don't know the ingredient(s) and end the conversation.",
        },
        # criticizing the recipes given by the user input
        {
            "role": "system",
            "content": "Your client is going to ask for a critique about a recipe for a dish. If you do not recognize the recipe, you should not try to generate a critique for it. Do not critique a recipe if you do not understand the recipe of the dish. If you know the recipe, you must answer directly with a detailed critique for it. If you don't know the recipe, you should answer that you don't know the recipe and end the conversation.",
        },
    ]
)


user_input = input(
    "\nType anything that you want to ask from Chef Derrick (recipe for a dish, ingredients for a dish, critique for a recipe).\n👨🏾: "
)
messages.append(
    {
        "role": "user",
        "content": user_input
    }
)

model = "gpt-3.5-turbo"

stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

collected_messages = ["\n"]
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)

messages.append(
    {
        "role": "system",
        "content": "".join(collected_messages)
    }
)

while True:
    print("\n: ")
    user_input = input()
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = ["\n"]
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)
    
    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )
