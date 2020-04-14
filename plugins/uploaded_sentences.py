import json

import nltk
import pymorphy2
import requests
from pymystem3 import Mystem


class UploadedSentences:

    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()
        self.mystem = Mystem()
        self.score = 0.9
        self.results = list()
        self.start = -1
        self.end = -1
        self.api_key = "93e13cef1c3834722983c61eeb9b9ba5f8ec9f4f"
        self.target_type = "syntax-relation"
        self.url = 'http://api.ispras.ru/texterra/v1/nlp?targetType={}&apikey={}'.format(self.target_type, self.api_key)
        self.processing = 0

    def get_processing(self):
        return self.processing

    def text_analysis(self, text):
        '''
        JSON, text: str; options: содержит настройки
        '''
        try:
            self.results = []
            self.start = -1
            self.end = -1
            # tmp_text = text["text"]
            count_sentence = nltk.sent_tokenize(text["text"], 'russian')
            procent = int(100 / len(count_sentence))
            sentences_gen = self.generator_sentence(text["text"])
            for sentence in sentences_gen:
                words_gen = self.generator_worlds_of_sentence(sentence)

                # Статистика для текущего предложения
                sentence_stats = {key: 0 for key in text["options"].keys()}

                for word in words_gen:
                    word_parse = self.morph.parse(word)
                    # Если score подходит, то обрабатываем слово
                    sentence_stats["word_count"] += 1
                    if word_parse[0].score >= self.score:
                        # Пунктуация
                        if "PNCT" in word_parse[0].tag:
                            if ',' in word_parse[0].word and text["options"]["number of commas"] is not None:
                                sentence_stats["number of commas"] += 1
                            elif ',' not in word_parse[0].word \
                                    and text["options"]["number of punctuation marks"] is not None:
                                sentence_stats["number of punctuation marks"] += 1

                            sentence_stats["word_count"] -= 1
                        # Сущ, гл, прил, мест, нареч, компаративы
                        elif "NOUN" in word_parse[0].tag and text["options"]["number of nouns"] is not None:
                            sentence_stats["number of nouns"] += 1

                        elif ("VERB" in word_parse[0].tag or "INFN" in word_parse[0].tag) \
                                and text["options"]["number of verbs"] is not None:
                            sentence_stats["number of verbs"] += 1

                        elif ("ADJF" in word_parse[0].tag or "ADJS" in word_parse[0].tag) \
                                and text["options"]["number of adjectives"] is not None:
                            sentence_stats["number of adjectives"] += 1

                        elif "NPRO" in word_parse[0].tag and text["options"]["number of pronouns"] is not None:
                            sentence_stats["number of pronouns"] += 1

                        elif "ADVB" in word_parse[0].tag and text["options"]["number of adverbs"] is not None:
                            sentence_stats["number of adverbs"] += 1

                        elif "COMP" in word_parse[0].tag and text["options"]["number of comparatives"] is not None:
                            sentence_stats["number of comparatives"] += 1

                        # Причастия, деепричасти
                        elif ("PRTF" in word_parse[0].tag or "PRTS" in word_parse[0].tag) \
                                and text["options"]["number of participles"] is not None:
                            sentence_stats["number of participles"] += 1

                        elif "GRND" in word_parse[0].tag and text["options"]["quantity of participles"] is not None:
                            sentence_stats["quantity of participles"] += 1

                        # Союзы и частицы, предлоги и междометия
                        elif "CONJ" in word_parse[0].tag and text["options"]["number of unions"] is not None:
                            sentence_stats["number of unions"] += 1

                        elif "PRCL" in word_parse[0].tag and text["options"]["number of particles"] is not None:
                            sentence_stats["number of particles"] += 1

                        elif "PREP" in word_parse[0].tag and text["options"]["number of prepositions"] is not None:
                            sentence_stats["number of prepositions"] += 1

                        elif "INTJ" in word_parse[0].tag and text["options"]["number of interjections"] is not None:
                            sentence_stats["number of interjections"] += 1

                        # Числительные и числа
                        elif "NUMR" in word_parse[0].tag and text["options"]["number of numerals"] is not None:
                            sentence_stats["number of numerals"] += 1

                        elif "NUMB" in word_parse[0].tag and text["options"]["amount of numbers"] is not None:
                            sentence_stats["amount of numbers"] += 1
                    else:
                        sentence_stats = self.text_analysis_mystem(word, text, sentence_stats)
                # Ищем основы
                if text["options"]["number of grammatical bases"] is not None:
                    res = requests.post(self.url, json=[{"text": sentence}])
                    count_podl = 0
                    count_skaz = 0
                    iter = res.json()[0]["annotations"]["syntax-relation"]
                    if len(iter) > 1:
                        for item in iter:
                            if item['value'] == {}:
                                count_skaz += 1
                            elif "предик" in item['value']["type"]:
                                count_podl += 1

                    sentence_stats["number of grammatical bases"] = count_podl
                    if count_podl == 0:
                        sentence_stats["number of grammatical bases"] = count_skaz

                index = 100
                keys = text["options"].keys()
                key_ = ""
                for key in keys:
                    if text["options"][key] is not None:
                        if int(text["options"][key]["priority"]) < index \
                                and text["options"][key]["count"] <= sentence_stats[key]:
                            index = int(text["options"][key]["priority"])
                            key_ = key

                # Закончили обрабатывать предложение, сохранить текущий результат
                start_index = text["text"].find(sentence)
                end_index = start_index + len(sentence)
                if start_index > self.start:
                    self.start = start_index
                    self.end = end_index
                else:
                    start_index = self.end + 1
                    end_index = start_index + len(sentence)

                # start_index = tmp_text.find(sentence)
                # end_index = start + len(sentence)
                # tmp_text = tmp_text[end_index:]
                if start_index != -1:
                    if key_ != "":
                        self.results.append({
                            # "sentence_stats": sentence_stats,
                            "indexes": {
                                "start": start_index,
                                "end": end_index
                            },
                            "color": text["options"][key_]["color"]
                        })

                self.processing += procent

            self.processing = 100

            if not self.results:
                self.results = None

            return self.results
        except Exception as e:
            return self.results.append({"error": "error"})

    def word_parse_mystem(self, word):
        word_parse = self.mystem.analyze(word)[0]
        if "analysis" in word_parse.keys():
            word_parse = word_parse["analysis"][0]
            # if word_parse['wt'] >= self.score:
            return word_parse
            # else:
            #     return {"skip": "skip"}

        else:
            return {"error": "error"}

    def text_analysis_mystem(self, word, text, sentence_stats):
        # Сущ, гл (+причасти и деепричастия), прил(+компаратив), мест, нареч, компаративы
        if text["options"]["number of nouns"] is not None:
            word_parse = self.word_parse_mystem(word)
            if "S" in word_parse['gr']:
                sentence_stats["number of nouns"] += 1

        elif text["options"]["number of verbs"] is not None \
                or text["options"]["number of participles"] is not None \
                or text["options"]["quantity of participles"] is not None:
            word_parse = self.word_parse_mystem(word)
            if "V" in word_parse['gr']:
                if "деепр" in word_parse['gr']:
                    sentence_stats["quantity of participles"] += 1
                elif "прич" in word_parse['gr']:
                    sentence_stats["number of participles"] += 1
                else:
                    sentence_stats["number of verbs"] += 1

        elif text["options"]["number of adjectives"] is not None \
            or text["options"]["number of comparatives"] is not None:
            word_parse = self.word_parse_mystem(word)
            if "A" in word_parse['gr']:
                if "срав" in word_parse['gr']:
                    sentence_stats["number of comparatives"] += 1
                else:
                    sentence_stats["number of adjectives"] += 1

        elif text["options"]["number of pronouns"] is not None:
            word_parse = self.word_parse_mystem(word)
            if "SPRO" in word_parse['gr'] or "APRO" in word_parse['gr']:
                sentence_stats["number of pronouns"] += 1

        elif text["options"]["number of adverbs"] is not None:
            word_parse = self.word_parse_mystem(word)
            if "ADV" in word_parse['gr'] or "ADVPRO" in word_parse['gr']:
                sentence_stats["number of adverbs"] += 1

        # Союзы и частицы, предлоги и междометия
        elif text["options"]["number of unions"] is not None:
            word_parse = self.word_parse_mystem(word)
            if "CONJ" in word_parse['gr']:
                sentence_stats["number of unions"] += 1

        elif text["options"]["number of particles"] is not None:
            word_parse = self.word_parse_mystem(word)
            if "PART" in word_parse['gr']:
                sentence_stats["number of particles"] += 1

        elif text["options"]["number of prepositions"] is not None:
            word_parse = self.word_parse_mystem(word)
            if "PR" in word_parse['gr']:
                sentence_stats["number of prepositions"] += 1

        elif text["options"]["number of interjections"] is not None:
            word_parse = self.word_parse_mystem(word)
            if "INTJ" in word_parse['gr']:
                sentence_stats["number of interjections"] += 1

        # Числительные
        elif text["options"]["number of numerals"] is not None:
            word_parse = self.word_parse_mystem(word)
            if "NUM" in word_parse['gr'] or "ANUM" in word_parse['gr']:
                sentence_stats["number of numerals"] += 1

        return sentence_stats

    @staticmethod
    def generator_sentence(text):
        for sentence in nltk.sent_tokenize(text, 'russian'):
            yield sentence

    @staticmethod
    def generator_worlds_of_sentence(sentence):
        for world in nltk.word_tokenize(sentence, 'russian'):
            yield world
