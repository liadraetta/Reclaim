

def drop_duplicates(file_name) :
    import pandas as pd
    df = pd.read_csv(file_name, header=None)
    df.columns = ["created_at", "user.name" , "user.description", "text" , "extended_tweet.full_text"," entities.hashtags"]
    def first_five_words(text):
        return " ".join(str(text).split()[:5])  # Convert to string to avoid NaN issues
    df["text_key"] = df["text"].apply(first_five_words)
    df_cleaned = df.drop_duplicates(subset="text_key", keep="first")

    df_cleaned = df_cleaned.drop(columns=["text_key"])

    return df_cleaned.to_csv("cleaned_file_2022.csv", index=False, header=False)

