from typing import List

import MeCab
import markovify


def generate_text(text: str, exec_times: int = 10) -> List[str]:
    text = _split_for_markovify(text)

    # learn model from text.
    text_model = markovify.NewlineText(text, state_size=2)

    markov_sentences = [text_model.make_short_sentence(200, min_chars=100, tries=1000).replace(" ", "") for i in
                        range(exec_times)]

    markov_sentences.sort(reverse=True, key=len)

    [print(sentence) for sentence in markov_sentences]

    print('generate_sentence ending…')

    return markov_sentences


def _split_for_markovify(text: str) -> str:
    mecab = MeCab.Tagger()
    splitted_text = ""

    breaking_chars = [
        '(',
        ')',
        '[',
        ']',
        '"',
        "'",
    ]

    for line in text.split():
        mp = mecab.parseToNode(line)
        while mp:
            try:
                if mp.surface not in breaking_chars:
                    splitted_text += mp.surface
                if mp.surface != '。' and mp.surface != '、':
                    splitted_text += ' '
                if mp.surface == '。':
                    splitted_text += '\n'
            except UnicodeDecodeError as e:
                print(line)
            finally:
                mp = mp.next

    return splitted_text
