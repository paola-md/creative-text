from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def get_fluency(preds_model, pred_topics):
  """
  The general idea is to sum up the ‘effort’ that each topic represents, which is expressed as the distance of each topic to zero. If you just count, the assumption is that the effort of each topic is 1.
  
  Returns: Value between 0 and 1 
  1 means that the user wrote about ALL the topics
  0 the user did not write about any of the topics
  """
  list_topics = list(np.unique(pred_topics))
  # -1 are outliers
  found_topics = [x for x in list_topics if x>-1]
  all_topics = preds_model.get_topics()
  fluency = len(found_topics)/len(all_topics) 
  return found_topics, fluency


def compute_flexibility(found_topics, similarity_matrix):
  """
  Range 0-1. Where 1 is that they are very distant and 0 that they are very close
  Greater is best

  If there is only one element it will return zero
  """
  global_similarity = 1


  if len(found_topics)>1:
    for i in found_topics:
      other_topics = [x for x in found_topics if x != i]
      topic_similarity = 0
      for j in other_topics:
        topic_similarity +=  similarity_matrix[i,j]

      topic_similarity = topic_similarity/len(other_topics)
      global_similarity += topic_similarity/len(found_topics)


  return 1 - global_similarity


def get_flexibility(preds_model, found_topics):
  """
  Average pairwise distance between all user topics
  """
  embeddings = np.array(preds_model.topic_embeddings)

  # remove -1 (outliers)
  embeddings = embeddings[1:]

  similarity_matrix = cosine_similarity(embeddings)
  flexibility = compute_flexibility(found_topics, similarity_matrix)
  return flexibility


def get_originality(pred_topics):
  """
  How many were outliers TBD
  """
  originality = pred_topics.count(-1)/len(pred_topics)
  return originality