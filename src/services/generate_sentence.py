from typing import List

from src.lib.file_adaptor import load_from_file
from src.lib.generate_sentence.markov import generate_text
from src.lib.generate_sentence.validator import validate_text


def generate_sentences(input_text: str) -> List[str]:
    text = validate_text(input_text)
    sentences = generate_text(text)

    return sentences


if __name__ == '__main__':
    text = load_from_file('*.txt')
    text = validate_text(text)
    markov_sentences = generate_sentences(text)

    print(markov_sentences)
