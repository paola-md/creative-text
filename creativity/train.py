import pandas as pd 
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
from umap import UMAP
import itertools

DATA_DIR = "./../data"
MODEL_DIR = "./models"

def etl(theme):
    # load data
    df = pd.read_csv(f"{DATA_DIR}/Corpus-creative-essays-{theme}.csv")
    df.columns =['id', 'text']

    # preprocess
    docs_list = [df['text'][i].split(".") for i in range(len(df))]
    our_docs = list(itertools.chain.from_iterable(docs_list))
    docs_filtered = [x for x in our_docs if len(x.split())>1]

    return docs_filtered

def create_model(docs_filtered, theme):
    # Remove stop words from definition not from model
    vectorizer_model = CountVectorizer(ngram_range=(1, 2), stop_words="english")

    # Seed the model
    umap_model = UMAP(n_neighbors=10, n_components=5, 
                    min_dist=0.0, metric='cosine', random_state=42)

    topic_model = BERTopic(language="english", 
                        min_topic_size = 10,
                        umap_model=umap_model,
                        vectorizer_model=vectorizer_model, 
                        calculate_probabilities=True, 
                        verbose=True)

    # Fit the model with our data
    topics, probs = topic_model.fit_transform(docs_filtered)

    # Save the model
    topic_model.save(f"{MODEL_DIR}/{theme}_model")

def main():
    # Do for all themes
    theme = "climate-change"
    docs_filtered = etl(theme)
    create_model(docs_filtered, theme)




