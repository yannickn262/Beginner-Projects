import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#fetch data and format it
data = fetch_movielens(min_rating = 4.0)

#print training and testing data
print(repr(data['train']))
print(repr(data['test']))

#create model
#warp creates recommendations by looking at user pair ratings
model = LightFM(loss ='warp')
#train model
model.fit(data['train'], epochs = 30, num_threads = 2)

def sample_recommendation(model, data, user_ids):
    #number of movies in training data
    n_users, n_items = data['train'].shape

    #generate recommendations for each user we input
    for user_id in user_ids:
        #movie's they've rated positive
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
        #movies our model predicts they'll enjoy
        scores = model.predict(user_id, np.arange(n_items))
        #rank them from most liked to least
        top_items = data['item_labels'][np.argsort(-scores)]

        #print out results
        print("User %s" %user_id)
        print("      Known Positives: ")
        #prints top 3
        for x in known_positives[:3]:
            print("       %s" % x)
        print("         Recommended Movies: ")
        for x in top_items[:3]:
            print("        %s" % x)
sample_recommendation(model,data,[3,25,450])
