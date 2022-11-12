import pandas as pd
import numpy as np
import sklearn
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
Ure = pd.read_csv("/Users/priyodarshighosh/Swaad/RAW_interactions 2.csv")
Re = pd.read_csv("/Users/priyodarshighosh/Swaad/RAW_recipes 2.csv")

def create_mat(df):
    N = len(df['user_id'].unique())
    M = len(df['recipe_id'].unique())
    user_map = dict(zip(np.unique(df['user_id']), list(range(N))))
    recipe_map = dict(zip(np.unique(df['recipe_id']), list(range(M))))
    user_inv_map = dict(zip(list(range(N)), np.unique(df['user_id'])))
    recipe_inv_map = dict(zip(list(range(M)), np.unique(df['recipe_id'])))
    
    user_idx = [user_map[i] for i in df['user_id']]
    recipe_idx = [recipe_map[i] for i in df['recipe_id']]
    
    X = csr_matrix((df["rating"], (recipe_idx, user_idx)), shape=(M, N))
      
    return X, user_map, recipe_map, user_inv_map, recipe_inv_map
X, user_map, recipe_map, user_inv_map, recipe_inv_map = create_mat(Ure)
def find_similar_recipes(recipe_id, X, k, metric='cosine', show_distance=False): 
    neighbour_ids = []
      
    recipe_ind = recipe_map[recipe_id]
    recipe_vec = X[recipe_ind]
    k+=1
    kNN = NearestNeighbors(n_neighbors=k, algorithm="brute", metric=metric)
    kNN.fit(X)
    recipe_vec = recipe_vec.reshape(1,-1)
    neighbour = kNN.kneighbors(recipe_vec, return_distance=show_distance)
    for i in range(0,k):
        n = neighbour.item(i)
        neighbour_ids.append(recipe_inv_map[n])
    neighbour_ids.pop(0)
    return neighbour_ids
def dish_recommender(dish):
    dfund = pd.DataFrame(Re['name'],Re['id'])
    recipe_map_ni = dict(zip(Re['name'],Re['id']))
    Rdf = pd.DataFrame(Ure)
    n_rate = len(Ure)
    n_recipe = len(Ure['recipe_id'].unique())
    n_user = len(Ure['user_id'].unique())
    user_freq = Ure[['user_id', 'recipe_id']].groupby('user_id').count().reset_index()
    user_freq.columns = ['user_id', 'n_rate']
    mean_rat = Ure.groupby('recipe_id')[['rating']].mean()
    lower_rated = mean_rat['rating'].idxmin()
    Re.loc[Re['id'] == lower_rated]
    highest_rated = mean_rat['rating'].idxmax()
    Re.loc[Re['id']== highest_rated]
    recipe_stats = Ure.groupby('recipe_id')[['rating']].agg(['count', 'mean'])
    recipe_stats.columns = recipe_stats.columns.droplevel()
    
    recipe_titles = dict(zip(Re['id'], Re['name']))
    dish_name = dish
    similar_dish = recipe_map_ni[dish_name]
    similar_ids = find_similar_recipes(similar_dish, X, k = 10)
    recipe_title = recipe_titles[similar_dish]
    print(f"Since you ate {recipe_title}")
    titles=[]
    for i in similar_ids:
        titles.append(recipe_titles[i])
    return titles



#print(recipe_map_ni['mojito lemon lime cocktail']) # Test




