from django.apps import AppConfig
import certifi
import pymongo

class WebConfig(AppConfig):
    uri = 'mongodb+srv://faris:yxUcNMs5ZiJmTPVE@cluster0.3knsc9a.mongodb.net/?retryWrites=true&w=majority'
    client = pymongo.mongo_client.MongoClient(uri, tlsCAFile=certifi.where())
    # Define DB Name
    db = client['Octopusdb']
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Apps.Web'
