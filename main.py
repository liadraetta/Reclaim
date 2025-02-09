import json
import os
import csv
from helper import drop_duplicates
import pandas as pd

target_words = [
    "frocie", "froci", "checca ", "culattone", "finocchi", "finocchietto", "finocchio", "frocio", " stesso sesso", "travestiti", "travestito", "travestita‍️", "travestite", "frocia", "ricchione", " trans "
]

#"pride", "lgbt", "orgoglio", "queer", "fierezza", "arcobaleno", " fobia", "diritti", "🏳️‍🌈", "🏳️‍⚧️", "🦄"


def contains_target_word(text):
    for word in target_words:
        if word in text.lower():
            return True
    return False



json_file_path = os.path.join(os.getcwd(), 'output/output_2022.json')

# with open(json_file_path, 'r', encoding='utf-8') as file:
#     tweets_data = json.load(file)
#
# total_tweets = 0
# filtered_tweets_count = 0
#
# filtered_tweets = []
#
# for tweet in tweets_data:
#     total_tweets += 1
#     tweet_text = tweet.get("extended_tweet", {}).get("full_text", tweet.get("text", ""))
#     if contains_target_word(tweet_text):
#         if "RT" not in tweet_text :
#             print(tweet_text)
#             filtered_tweets.append(tweet)
#             filtered_tweets_count += 1
#
# output_file_path = os.path.join(os.getcwd(), 'output/output_2022.json')
#
# with open(output_file_path, 'w', encoding='utf-8') as output_file:
#     json.dump(filtered_tweets, output_file, ensure_ascii=False, indent=4)
#
# print(f"Total tweets processed: {total_tweets}")
# print(f"Filtered tweets containing forbidden words: {filtered_tweets_count}")
#
#
with open(json_file_path, 'r', encoding='utf-8') as file:
     json_data = json.load(file)

directory = os.path.join(os.getcwd(), 'output')  # Adjust to your desired directory
csv_file = os.path.join(directory, "2022.csv")

fields = [
    "created_at",
    "user.name",
    "user.description",
    "text",
    "extended_tweet.full_text",
    "entities.hashtags"
]

with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(fields)

    if isinstance(json_data, list):
        for tweet in json_data:
            writer.writerow([
                tweet.get("created_at"),
                tweet.get("user", {}).get("name"),
                tweet.get("user", {}).get("description"),
                tweet.get("text"),
                tweet.get("extended_tweet", {}).get("full_text"),
                tweet.get("entities", {}).get("hashtags")
            ])
    else:
        writer.writerow([
            json_data.get("created_at"),
            json_data.get("user", {}).get("name"),
            json_data.get("user", {}).get("description"),
            json_data.get("text"),
            json_data.get("extended_tweet", {}).get("full_text"),
            json_data.get("entities", {}).get("hashtags")
        ])

print(f"CSV file saved successfully to '{csv_file}'.")

drop_duplicates("output/2022.csv")