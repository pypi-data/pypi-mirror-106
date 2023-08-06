from math import sqrt
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from collections import defaultdict
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

class MLRecommender():

    def __init__(self, user_df, item_df, user_id, item_id, item_rating, item_categories):
        """
        This class expects a user_df with user_ids and their given numeric ratings to items with item_ids.
        Also expects an item_df with item_ids and their given title and categories it falls under.

        Args:
            user_df (pd.DataFrame): User DataFrame with User_id, item_id, rating pairs
            item_df (pd.DataFrame): Item DataFrame with item_id, item_name, item_categories fields
            user_id (str): column name of corresponding to user_id
            item_id (str): column name of corresponding to item_id
            item_rating (str): column name of corresponding to rating
            item_categories (str): column name of corresponding to item_categories
            item_name (str): column name of corresponding to item_name
        """
        
        self.user_df = user_df
        self.item_df = item_df
        
        self.user_id = user_id
        self.item_id = item_id
        self.item_rating = item_rating
        self.item_categories = item_categories
        
        self.user_map = defaultdict(dict)
        
        for idx in range(len(self.user_df)):
            
            temp_row = self.user_df.iloc[idx]
            
            user_id = temp_row[self.user_id]
            item_id = temp_row[self.item_id]
            rating = temp_row[self.item_rating]
            
            self.user_map[int(user_id)][int(item_id)] = int(rating)

    def predict_rating(self, user_id, item_id, sep = " "):
        
        item_ids = []

        item_categories = list(self.item_df[self.item_df[self.item_id] == item_id][self.item_categories].str.strip().str.split(sep))
        if not item_categories:
            return
        else:
            item_categories = item_categories[0]

        for idx in range(len(self.item_df)):
            
            temp_row = self.item_df.iloc[idx]
            
            it_id = temp_row[self.item_id]
            it_category = temp_row[self.item_categories]
            
            found = False
            for category in item_categories:
                if category in it_category:
                    found = True
                    break
            
            if not found:
                continue
            
            item_ids.append(it_id)
            
        if len(item_ids) < 10:
            return
    
        X, y = [], []

        for user in self.user_map:
            
            if user == user_id:
                continue
                
            if item_id not in self.user_map[user]:
                continue
                
            user_row = []
            for it_id in item_ids:
                
                if it_id == item_id:
                    y.append(self.user_map[user][it_id])
                    
                else:
                    if it_id in self.user_map[user]:
                        user_row.append(self.user_map[user][it_id])
                    else:
                        user_row.append(0)
                    
            X.append(user_row)

        pred_sample = []

        for it_id in item_ids:
            
            if it_id == item_id:
                continue
            
            if it_id in self.user_map[user_id]:
                pred_sample.append(self.user_map[user_id][it_id])
            else:
                pred_sample.append(0)

        X = np.array(X)
        pred_sample = np.array(pred_sample).reshape((1, -1))
        y = np.array(y)
        
        rf = RandomForestClassifier()
        rf.fit(X, y)
        
        return rf.predict(pred_sample)[0]