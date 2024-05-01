
from fastapi import FastAPI, UploadFile, File
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo
from PIL import Image
from pydantic import BaseModel
import pickle
import json
import io


app= FastAPI()


def f(link:str):

    youtube_video = link
    video_id = youtube_video.split("=")[1]
    YouTubeVideo(video_id)

    YouTubeTranscriptApi.get_transcript(video_id)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # print("--------------------------------------------------------")

    # print(transcript[0:5])


    result = ""
    for i in transcript:
        result += ' ' + i['text']
    #print(result)
    # print(len(result))

    def extract_ingredients_from_paragraph(paragraph, ingredients_list):
        paragraph_lower = paragraph.lower()
        extracted_ingredients = []
        for ingredient in ingredients_list:
            if ingredient.lower() in paragraph_lower:
                extracted_ingredients.append(ingredient)
        return extracted_ingredients
    paragraph = result

    ingredients_list = [
        "Salt", "Pepper", "Sugar", "Flour", "Eggs", "Milk", "Butter", "Olive oil", "Onion", "Garlic",
        "Tomato", "Potato", "Rice", "Pasta", "Chicken", "Beef", "Fish", "Carrot", "Bell pepper", "Spinach",
        "Apple", "Banana", "Orange", "Lemon", "Lime", "Grapefruit", "Pineapple", "Mango", "Papaya", "Kiwi",
        "Pear", "Peach", "Plum", "Cherry", "Berries", "Watermelon", "Cantaloupe", "Honeydew melon", "Coconut",
        "Fig", "Dates", "Raisins", "Prunes", "Cranberries", "Pomegranate",
        "Asparagus", "Avocado", "Bok choy", "Brussels sprouts", "Cabbage", "Cauliflower", "Celery", "Cucumber",
        "Eggplant", "Green beans", "Jalapeno", "Kale", "Lettuce", "Mushroom", "Okra", "Peas", "Radish", "Spinach",
        "Squash", "Sweet potato", "Turnip", "Zucchini",
        "Red pepper", "Green pepper", "Yellow pepper", "Orange pepper", "Bell pepper", "Jalapeno", "Poblano", "Serrano",
        "Habanero", "Anaheim pepper", "Cayenne pepper", "Chili pepper",
        "Sea salt", "Kosher salt", "Himalayan salt", "Table salt", "Rock salt",
        "Cumin", "Paprika", "Chili powder", "Turmeric", "Ginger", "Cinnamon", "Nutmeg", "Cloves", "Cardamom", "Coriander",
        "Mustard seed", "Fennel seed", "Cayenne", "Black pepper", "White pepper", "Allspice", "Bay leaf", "Oregano",
        "Basil", "Rosemary", "Thyme", "Sage", "Marjoram", "Dill", "Tarragon", "Chives", "Parsley", "Cilantro",
        "Vanilla extract", "Almond extract", "Lemon extract", "Orange extract", "Peppermint extract", "Coconut extract",
        "Mint extract", "Raspberry extract", "Strawberry extract", "Maple extract", "Coffee extract", "Rose water",
        "Orange blossom water", "Peppermint oil", "Lemon zest", "Lime zest", "Orange zest", "Lemon juice", "Lime juice",
        "Orange juice", "Grapefruit juice", "Pineapple juice", "Apple juice", "Cranberry juice", "Tomato juice",
        "Vegetable juice", "Clam juice", "Fish sauce", "Oyster sauce", "Hoisin sauce", "Teriyaki sauce", "Soy sauce",
        "Tamari", "Worcestershire sauce", "BBQ sauce", "Hot sauce", "Buffalo sauce", "Salsa", "Pesto", "Hummus",
        "Guacamole", "Tzatziki", "Baba ganoush", "Tapenade", "Chimichurri", "Chutney", "Relish", "Pickle", "Sauerkraut",
        "Kimchi", "Curry paste", "Harissa", "Miso", "Tahini", "Peanut butter", "Nutella", "Marshmallow fluff", "Lemon curd",
        "Caramel", "Marzipan", "Fondant", "Royal icing", "Cream cheese frosting", "Buttercream frosting", "Ganache",
        "Meringue", "Custard", "Pastry cream", "Pudding", "Jello", "Gelatin", "Ice cream", "Sorbet", "Sherbet",
        "Frozen yogurt", "Gelato", "Granita", "Popsicle", "Ice pop", "Ice cube", "Ice shard", "Ice ball", "Ice cone",
        "Ice cream cone", "Cone shell", "Cone snail", "Coneflower", "Cone beam", "Cone beam computed tomography",
        "Cone biopsy", "Cone calorimeter", "Cone pulley", "Cone clutch", "Cone crusher", "Cone snail venom",
        "Cone angle", "Cone of uncertainty", "Cone cell", "Cone mosaic",
    ]

    extracted_ingredients = extract_ingredients_from_paragraph(paragraph, ingredients_list)
    return extracted_ingredients

    # print("Extracted ingredients:", extracted_ingredients)

    # def fun():
#     return
class model_input(BaseModel):
     link : str




@app.post('/ingredient_extraction')
# def ingredient_extraction(input_parameters : model_input):
     
def ingredient_extraction(input_parameters :model_input):
    

    ans= f(input_parameters.link)
    return ans


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
