import argparse
from collections import Counter
import nltk
import re
import statistics
import time
import datetime

class Timer:
    """
    Starts and stops timer automatically
    """
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start

class Analyzer:
    """
    generates detailed report about input text
    """
    def __init__(self, text):
        self.text = text

    def analyze(self):
        nltk.download('punkt')
        self.sentences = nltk.tokenize.sent_tokenize(self.text)
        self.words = [re.sub(r'\W+', '', word) for sentence in [words.split() for words in self.sentences] for word in sentence]
        self.number_of_characters = len([char for char in self.text if not char.isspace()])
        self.number_of_words = len(self.words)
        self.number_of_sentences = len(self.sentences)
        self.frequency_of_chars = Counter(self.text)
        self.distr_of_chars = {char: dist/self.number_of_characters*100 for char, dist in self.frequency_of_chars.items()}
        self.avrg_word_length = statistics.mean([len(word) for word in self.words])
        self.avrg_words_in_sentence = statistics.mean([len(sentence.split()) for sentence in self.sentences])
        self.top10_words = Counter([word.lower() for word in self.words]).most_common(10)
        self.top10_long_words = list(sorted(self.words, key=len, reverse=True))[:10]
        self.top10_short_words = list(sorted(self.words, key=len))[:10]
        self.top10_long_sentences = list(sorted(self.sentences, key=len, reverse=True))[:10]
        self.top10_short_sentences = list(sorted(self.sentences, key=len))[:10]
        self.palindromes = [word for word in self.words if word==word[::-1]]
        self.number_of_palindromes = len(self.palindromes)
        self.top10_long_palindromes = list(sorted(self.palindromes, key=len, reverse=True))[:10]
        self.text_is_palindrome = re.sub(r'\W+', '', self.text) == re.sub(r'\W+', '', self.text)[::-1]
        self.time_of_report = datetime.datetime.now()
        self.reversed_text = self.text[::-1]
        self.reversed_text_char_order = ' '.join(self.text.split()[::-1])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Text analyzer')
    parser.add_argument('-i', '--input', help='Input text', required=True)
    args = parser.parse_args()
    report = Analyzer(args.input)
    with Timer() as timer:
        report.analyze()
    print(f"Report date and time: {report.time_of_report}")
    print(f"time to generate report: {int(timer.elapsed * 1000)} ms")
