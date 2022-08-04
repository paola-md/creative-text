

from bertopic import BERTopic
from .metrics import get_fluency, get_flexibility, get_originality

climate_model = BERTopic.load("./models/climate_change_model")

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