from pycantonese.corpus import Token
from pycantonese.tests.test_corpus import HKCANCOR


def test_find_verbs_in_hkcancor():
    all_verbs = HKCANCOR.search(pos="^V")
    assert len(all_verbs) == 29726
    assert all_verbs[:10] == [
        Token(word="去", pos="V", jyutping="heoi3", mor=None, gra=None),
        Token(word="去", pos="V", jyutping="heoi3", mor=None, gra=None),
        Token(word="旅行", pos="VN", jyutping="leoi5hang4", mor=None, gra=None),
        Token(word="有冇", pos="V1", jyutping="jau5mou5", mor=None, gra=None),
        Token(word="要", pos="VU", jyutping="jiu3", mor=None, gra=None),
        Token(word="有得", pos="VU", jyutping="jau5dak1", mor=None, gra=None),
        Token(word="冇得", pos="VU", jyutping="mou5dak1", mor=None, gra=None),
        Token(word="去", pos="V", jyutping="heoi3", mor=None, gra=None),
        Token(word="係", pos="V", jyutping="hai6", mor=None, gra=None),
        Token(word="係", pos="V", jyutping="hai6", mor=None, gra=None),
    ]


def test_by_tokens_false():
    all_verbs = HKCANCOR.search(pos="^V", by_tokens=False)
    assert len(all_verbs) == 29726
    expected = ["去", "去", "旅行", "有冇", "要", "有得", "冇得", "去", "係", "係"]
    assert all_verbs[:10] == expected


def test_by_utterances_true():
    all_verbs = HKCANCOR.search(pos="^V", by_utterances=True)
    assert len(all_verbs) == 29726
    print(all_verbs[:2])
    assert all_verbs[:2] == [
        [
            Token(word="喂", pos="E", jyutping="wai3", mor=None, gra=None),
            Token(word="遲", pos="A", jyutping="ci4", mor=None, gra=None),
            Token(word="啲", pos="U", jyutping="di1", mor=None, gra=None),
            Token(word="去", pos="V", jyutping="heoi3", mor=None, gra=None),
            Token(word="唔", pos="D", jyutping="m4", mor=None, gra=None),
            Token(word="去", pos="V", jyutping="heoi3", mor=None, gra=None),
            Token(word="旅行", pos="VN", jyutping="leoi5hang4", mor=None, gra=None),
            Token(word="啊", pos="Y", jyutping="aa3", mor=None, gra=None),
            Token(word="?", pos="?", jyutping=None, mor=None, gra=None),
        ],
        [
            Token(word="喂", pos="E", jyutping="wai3", mor=None, gra=None),
            Token(word="遲", pos="A", jyutping="ci4", mor=None, gra=None),
            Token(word="啲", pos="U", jyutping="di1", mor=None, gra=None),
            Token(word="去", pos="V", jyutping="heoi3", mor=None, gra=None),
            Token(word="唔", pos="D", jyutping="m4", mor=None, gra=None),
            Token(word="去", pos="V", jyutping="heoi3", mor=None, gra=None),
            Token(word="旅行", pos="VN", jyutping="leoi5hang4", mor=None, gra=None),
            Token(word="啊", pos="Y", jyutping="aa3", mor=None, gra=None),
            Token(word="?", pos="?", jyutping=None, mor=None, gra=None),
        ],
    ]


def test_word_range():
    all_verbs = HKCANCOR.search(pos="^V", word_range=(1, 2))
    assert len(all_verbs) == 29726
    assert all_verbs[:2] == [
        [
            Token(word="啲", pos="U", jyutping="di1", mor=None, gra=None),
            Token(word="去", pos="V", jyutping="heoi3", mor=None, gra=None),
            Token(word="唔", pos="D", jyutping="m4", mor=None, gra=None),
            Token(word="去", pos="V", jyutping="heoi3", mor=None, gra=None),
        ],
        [
            Token(word="唔", pos="D", jyutping="m4", mor=None, gra=None),
            Token(word="去", pos="V", jyutping="heoi3", mor=None, gra=None),
            Token(word="旅行", pos="VN", jyutping="leoi5hang4", mor=None, gra=None),
            Token(word="啊", pos="Y", jyutping="aa3", mor=None, gra=None),
        ],
    ]


def test_utterance_range():
    all_verbs = HKCANCOR.search(pos="^V", utterance_range=(0, 1))
    assert len(all_verbs) == 29726
    assert all_verbs[:2] == [
        [
            [
                Token(word="喂", pos="E", jyutping="wai3", mor=None, gra=None),
                Token(word="遲", pos="A", jyutping="ci4", mor=None, gra=None),
                Token(word="啲", pos="U", jyutping="di1", mor=None, gra=None),
                Token(word="去", pos="V", jyutping="heoi3", mor=None, gra=None),
                Token(word="唔", pos="D", jyutping="m4", mor=None, gra=None),
                Token(word="去", pos="V", jyutping="heoi3", mor=None, gra=None),
                Token(word="旅行", pos="VN", jyutping="leoi5hang4", mor=None, gra=None),
                Token(word="啊", pos="Y", jyutping="aa3", mor=None, gra=None),
                Token(word="?", pos="?", jyutping=None, mor=None, gra=None),
            ],
            [
                Token(word="你", pos="R", jyutping="nei5", mor=None, gra=None),
                Token(word="老公", pos="N", jyutping="lou5gung1", mor=None, gra=None),
                Token(word="有冇", pos="V1", jyutping="jau5mou5", mor=None, gra=None),
                Token(word="平", pos="A", jyutping="peng4", mor=None, gra=None),
                Token(word="機票", pos="N", jyutping="gei1piu3", mor=None, gra=None),
                Token(word="啊", pos="Y", jyutping="aa3", mor=None, gra=None),
                Token(word="?", pos="?", jyutping=None, mor=None, gra=None),
            ],
        ],
        [
            [
                Token(word="喂", pos="E", jyutping="wai3", mor=None, gra=None),
                Token(word="遲", pos="A", jyutping="ci4", mor=None, gra=None),
                Token(word="啲", pos="U", jyutping="di1", mor=None, gra=None),
                Token(word="去", pos="V", jyutping="heoi3", mor=None, gra=None),
                Token(word="唔", pos="D", jyutping="m4", mor=None, gra=None),
                Token(word="去", pos="V", jyutping="heoi3", mor=None, gra=None),
                Token(word="旅行", pos="VN", jyutping="leoi5hang4", mor=None, gra=None),
                Token(word="啊", pos="Y", jyutping="aa3", mor=None, gra=None),
                Token(word="?", pos="?", jyutping=None, mor=None, gra=None),
            ],
            [
                Token(word="你", pos="R", jyutping="nei5", mor=None, gra=None),
                Token(word="老公", pos="N", jyutping="lou5gung1", mor=None, gra=None),
                Token(word="有冇", pos="V1", jyutping="jau5mou5", mor=None, gra=None),
                Token(word="平", pos="A", jyutping="peng4", mor=None, gra=None),
                Token(word="機票", pos="N", jyutping="gei1piu3", mor=None, gra=None),
                Token(word="啊", pos="Y", jyutping="aa3", mor=None, gra=None),
                Token(word="?", pos="?", jyutping=None, mor=None, gra=None),
            ],
        ],
    ]
