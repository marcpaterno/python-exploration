#!/usr/bin/env python

# This is a demo program to see of a context manager works inside
# of a generator.
# Thanks to "Programing and Mathematical Thinking" by Allan M. Stavely
# (page 97) for the generator, but without the use of the context
# manager.


def words(aFilename):
    """words is a function that constructs a generator.
    Calling words does not begin executing the generator;
    that is done by using it in an iteration context, or
    by calling next(x) on the returned object 'x'.
    """
    punctuation = ".,:;'\""
    with open(aFilename) as my_file:
        for line in my_file:
            words = line.strip().split()
            for word in words:
                yield word.strip(punctuation)


if __name__ == "__main__":
    num_words = 0
    for word in words("README.md"):
        num_words += 1
        print(word)
    print(f"That was {num_words} words")
