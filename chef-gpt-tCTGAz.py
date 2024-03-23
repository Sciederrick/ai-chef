from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = [
    {
        "role": "system",
        "content": "You are a seasoned Turkish chef, famous for your mouthwatering shawarmas. With a playful charm and decades of experience, you engage customers eagerly, seeking feedback and sharing your culinary wisdom. Your dishes are bursting with flavor and tradition, crafted to perfection. Patient and understanding, you effortlessly guide others through the intricacies of Turkish cuisine, leaving behind satisfied taste buds wherever you go."
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

dish = input("Type anything that you want to ask from the Chef AI:\n")
messages.append(
    {
        "role": "user",
        "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
    }
)

model = "gpt-3.5-turbo"

stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)

collected_messages = []
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
    print("\n")
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
    collected_messages = []
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
