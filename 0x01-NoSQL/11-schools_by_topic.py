#!/usr/bin/env python3
"""
    11-schools_by_topic module
"""


def schools_by_topic(mongo_collection, topic):
    """
        Function returns the list of school that have a specific topic
    """
    school = []
    return [school for school in mongo_collection.find({"topics": topic})]
