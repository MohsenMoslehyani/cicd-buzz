from buzz import generator


def test_sample_single_word():
    items = ("foo", "bar", "foobar")
    word = generator.sample(items)
    assert word in items


def test_sample_multiple_words():
    items = ("foo", "bar", "foobar")
    words = generator.sample(items, 2)
    assert len(words) == 2
    assert words[0] in items
    assert words[1] in items
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
