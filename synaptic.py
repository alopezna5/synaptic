#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import random


_text_colors = {
    "NORMAL": "\033[0m",
    "BLUE": "\033[;36m",
    "UNDERLINED_BLUE": "\033[4;35;36m",
    "RED": "\033[91mm",
    "YELLOW": "\033[93m",
    "GREEN": "\033[92m"
}


class synaptic():


    def __init__(self, path_to_topics):
        self.path_to_topics = path_to_topics
        self.topics = os.listdir(self.path_to_topics)


    def _colored_print(self, text, color_code):
        print("{init_color} {text} {restore_color}".format(init_color=color_code, text=text, restore_color=_text_colors["NORMAL"]))


    def get_topics(self):
        i = 1
        for topic in self.topics:
            print(str(i) + " " + topic)
            i += 1

    def get_topic_from_user(self):
        while True:
            try:
                topic_to_read = int(input("Choose the topic you want to try with \n")) - 1
                assert topic_to_read >= 0
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

        random_choice = random.choice(list(question_and_answer_json.items())) # Choosing a random element from the dictionary

        print("[!] Choosing a random concept about", end="")
        self._colored_print(self.topics[index_of_topic_to_read], _text_colors["BLUE"])

        print("[?] The concept is: ", end="")
        self._colored_print(random_choice[0], _text_colors["UNDERLINED_BLUE"])
        input("\t Press enter to see the result ...\n\t")
        print("\t" + random_choice[1])

        while True:
            try:
                self._colored_print("Were you right? S/N", _text_colors["YELLOW"])
                user_result = str(input())
                assert user_result.upper() == "S" or user_result.upper() == "N"
                break
            except:
                self._colored_print("Not valid option!", _text_colors["RED"])

        return user_result


    def main(self):
        while True:
            self.get_topics()
            self.get_topic_from_user()



if __name__ == "__main__":
    test = synaptic("test/resources/")
    test.main()