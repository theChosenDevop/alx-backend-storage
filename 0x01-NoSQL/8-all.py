#!/usr/bin/env python3
"""
    Defines 8-all module
"""


def list_all(mongo_collection):
    """
        Function list all documents in a collection
    """
    return mongo_collection.find()
