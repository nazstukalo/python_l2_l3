import argparse
from collections import Counter
import nltk
import re
import statistics
import time
import datetime
import concurrent.futures
from urllib.request import Request, urlopen
import validators


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
    def __init__(self, file):
        self.file = file

    def analyze(self):
        self.time_of_report = datetime.datetime.now()
        if validators.url(self.file):
            self.type_of_resource = 'resource'
        else:
            self.type_of_resource = 'file'

        try:
            if self.type_of_resource == 'resource':
                req = Request(self.file, headers={'User-Agent': 'Mozilla/5.0'})
                self.text = urlopen(req).read().decode('utf-8')
            elif self.type_of_resource == 'file':
                with open(self.file, 'r') as r:
                    self.text = r.read()
                    self.type_of_resource = 'file'
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
            self.top10_long_words = list(sorted(set(self.words), key=len, reverse=True))[:10]
            self.top10_short_words = list(sorted(set(self.words), key=len))[:10]
            self.top10_long_sentences = list(sorted(self.sentences, key=len, reverse=True))[:10]
            self.top10_short_sentences = list(sorted(self.sentences, key=len))[:10]
            self.palindromes = set([word for word in self.words if word==word[::-1]])
            self.number_of_palindromes = len(self.palindromes)
            self.top10_long_palindromes = list(sorted(self.palindromes, key=len, reverse=True))[:10]
            self.text_is_palindrome = re.sub(r'\W+', '', self.text) == re.sub(r'\W+', '', self.text)[::-1]
            self.reversed_text = self.text[::-1]
            self.reversed_text_char_order = ' '.join(self.text.split()[::-1])
        except Exception as e:
            self.result = f"{self.time_of_report}|{self.type_of_resource}|{self.file}|CRITICAL"
        else:
            self.result = f"{self.time_of_report}|{self.type_of_resource}|{self.file}|INFO"
            print(f"Report for file {self.file}:date and time: {self.time_of_report}")


def analyze_file(file):
    print(f'working with file {file}')
    report = Analyzer(file)
    with Timer() as timer:
        report.analyze()
    print(f"time to generate report for file {file}: {int(timer.elapsed * 1000)} ms")
    return report.result

if __name__ == '__main__':
    # analyze_file('https://filesamples.com/samples/document/txt/sample3.txt')
    parser = argparse.ArgumentParser(description = 'Text analyzer')
    parser.add_argument('-f', '--files', nargs='+', help='Input files')
    parser.add_argument('-r', '--resources', nargs='+', help='resource')
    args = parser.parse_args()
    files = vars(args)['files']
    resources = vars(args)['resources']
    total_files = []
    if files:
        total_files.extend(files)
    if resources:
        total_files.extend(resources)


    with concurrent.futures.ProcessPoolExecutor() as executor:
        reports = [executor.submit(analyze_file, file) for file in total_files]
        for f in concurrent.futures.as_completed(reports):
            with open ('textanalyzer.log', 'a') as log_file:
                log_file.write(f"\n{f.result()}")

    #
    # for file in files:
    #     analyze_file(file)

    # report = Analyzer(r"C:\work\python_mentor\python_l2_l3\advanced1\Sample-text-file-10kb.txt")

###################################################