#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json

class synaptic():


    def __init__(self, path_to_topics):
        self.path_to_topics = path_to_topics
        self.topics = os.listdir(self.path_to_topics)


    def get_topics(self):
        i = 1
        for topic in self.topics:
            print(str(i) + " " + topic)
            i += 1

    def get_topic_from_user(self):
        while True:
            try:
                topic_to_read = int(input("Choose the topic you want to try with \n"))
                break
            except:
                print("Not valid option! Please, add the number of the topic you want to try with")

        self.make_question_from_topic(topic_to_read)


    def make_question_from_topic(self, index_of_topic_to_read):
        question_and_answer_json = {}

        topic_path = self.path_to_topics + self.topics[index_of_topic_to_read]
        topic_directory = os.listdir(topic_path)

        for file_in_path in topic_directory:
            if file_in_path.endswith(".json"):
                path = topic_path + "/" + file_in_path
                f = open(path, "r")
                file_into_json = json.loads(f.read())
                question_and_answer_json.update(file_into_json)


if __name__ == "__main__":
    test = synaptic("test/resources/")
    test.get_topics()
    test.get_topic_from_user()


