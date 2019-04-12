# imports needed and logging
import gensim, pandas as pd, re
import numpy as np

event_data = pd.read_csv('event_data4.csv')
descriptions = []

for description in event_data[' description']:
    description = re.sub("[^a-zA-Z]", " ", description)
    description = description.lower().split()
    descriptions += [description]
    
model = gensim.models.Word2Vec(descriptions, size=100, window=10, min_count=2, workers=10)  
model.train(descriptions, total_examples=len(descriptions), epochs=10)

def find_sim_event(query,top=5):
    best_score = 0
    best_description = None
    sims = model.wv.most_similar(positive = query)
    sims = list(zip(*sims))
    sim_words = list(sims[0])
    sim_words.append(query)
    
    event_scores = []
    for i in range(len(descriptions)):
        description = descriptions[i]
        description_total = 0

        ##finding ones that have similar words
        simcount = 0
        for sim_word in sim_words:
            simcount += description.count(sim_word)
        if len(description) > 0:
            description_score_sim = simcount/len(description)
        else:
            description_score_sim = 0
    
        #### adding similarity across all words
        for word in description:
            try:
                word_score = model.wv.similarity(w1=query, w2=word)
            except:
                word_score = 0

            description_total += word_score
        if len(description) > 0:
            description_score = description_total#/len(description) #since we already penalized in simcount for len of description
        else:
            description_score = 0
    
        ##combining both
        print(description_score_sim, description_score)
        description_score = description_score*description_score_sim
            
        event_scores.append((event_data['url'][i], description_score, event_data[' description'][i]))
    event_scores.sort(key=lambda event: event[1], reverse=True)
    return(event_scores[:top])