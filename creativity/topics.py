

from sentence_transformers import SentenceTransformer
from bertopic import BERTopic
from bertopic.backend._utils import select_backend

from .metrics import get_fluency, get_flexibility, get_originality
from .load_model import get_models

# load models globally
#get_models()
sentence_model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
model = select_backend(sentence_model)
climate_model = BERTopic.load("./creativity/models/model_climate_change", embedding_model=model)


def preprocess(text):
  sentences = text.split('.') 
  sentences = [x for x in sentences if len(x.split())>1]
  return sentences

def get_metrics(text, dataset = "climate_change"):
  if dataset == "climate_change":
    # we can add the other models here
    preds_model = climate_model
  sentences = preprocess(text)
  pred_topics, pred_prob = preds_model.transform(sentences)
  found_topics, fluency = get_fluency(preds_model, pred_topics)
  flexibility = get_flexibility(preds_model, found_topics)
  originality = get_originality(pred_topics)
  return fluency, flexibility, originality 