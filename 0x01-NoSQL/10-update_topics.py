#!/usr/bin/env python3
"""
    10-update_topics module
"""


def update_topics(mongo_collection, name, topics):
    """
        The function changes all topics of a school document based on the name
    """
    query = {"name": name}
    update_doc = {"$set": {"topics": topics}}

    return mongo_collection.update_one(query, update_doc)
