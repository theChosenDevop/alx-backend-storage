#!/usr/bin/env python3
"""
    9-insert_school module
"""


def insert_school(mongo_collection, **kwargs):
    """
        The function inserts a new document in a collection based on kwargs

        Returns: new _id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
