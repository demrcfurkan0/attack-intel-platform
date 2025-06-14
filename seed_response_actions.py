from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["cyber_attack_sim_db"]
collection = db["response_actions"]

with open("response_action.json", "r") as f:
    actions = json.load(f)

if isinstance(actions, list):
    collection.insert_many(actions)
    print(f"{len(actions)} action inserted successfully.")