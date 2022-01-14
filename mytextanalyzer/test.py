import pytest
import analyzer

@pytest.mark.parametrize('text', [
    'Sentence one. Sentence two',
    'sentence one; still sentence one. Sentence two',
    'sentence one, sent one. Sentence two',
    'here is long sentence one here is long sentence one here is long sentence one here is long sentence one here is long sentence one . Sent two.',
    'one more example....of sent one. Sentence two'
])
def test_count_sentences_one(text):
    assert (len(analyzer.Analyzer.count_sentences(text)) == 2)


def test_count_sentences_two():
    assert (len(analyzer.Analyzer.count_sentences('Sentence one. Sentence two. Sentence three')) == 3)


def test_count_sentences_three():
    assert (len(analyzer.Analyzer.count_sentences('Sentence one. Sentence two. Sentence three. And one more')) == 4)


@pytest.mark.parametrize('text', [
    'grkghtroxf',
    'grkghtr xff',
    ' fedfrl lf?r',
    '&^##((((((',
    '1234567890'
])
def test_number_of_char(text):
    assert analyzer.Analyzer.count_number_of_characters(text) == 10

def test_number_of_char_two():
    assert analyzer.Analyzer.count_number_of_characters('Sentence one. Sentence two. Sentence three. And one more') == 48

