#-*- coding: utf-8 -*-

'''
Minimal interface to be implemented by recommenders.
'''
# Authors: Marcel Caraciolo <marcel@caraciolo.com.br>
# License: BSD Style.

from ..base import BaseEstimator

class BaseRecommender(BaseEstimator):
    """Base class for recommenders.
    Should not be used directly, use derived classes instead.
    """

    def recommend(self, uid, how_many,  **params):
        """
        Recommend new items for a set of id's. It assumes 
        that you've already called fit().

        Parameters
        ----------
        uid: int
        Id that will receive the recommendations. 

        how_many: int
        Maximum number of recommended items to return for a Id. 

        Returns
        ---------
        Return a list of recommended items, ordered from most strongly
        recommend to least.
        """
        pass 
