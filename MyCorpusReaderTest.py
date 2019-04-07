from MyCorpusReader import MyCorpusReader
from nltk.corpus import PlaintextCorpusReader
import os
import nltk
import unittest


class MyCorpusReaderTester(unittest.TestCase):

    mcr = None
    nltk_reader = None

    def setUp(self):
        self.mcr = MyCorpusReader('test_directory', 'stop_word', None)
        self.nltk_reader = PlaintextCorpusReader(os.path.abspath('test_directory'), 'text1.txt')

    def test_constructor(self):
        # check root
        self.assertEqual(self.mcr.root, os.path.abspath('test_directory'))
        # check default stemmer
        self.assertIsNone(self.mcr.stemmer)

    def test_with_directory_name(self):
        with self.assertRaises(FileExistsError):
            MyCorpusReader('not a directory', 'stop_word', None)

    def test_with_sfile(self):
        # stop word file as empty set
        a = MyCorpusReader('test_directory', '', None)
        self.assertEqual(a.stop_words, ())
        # stop word file as default from nltk
        b = MyCorpusReader('test_directory', stemmer=None)
        self.assertEqual(b.stop_words, set(nltk.corpus.stopwords.words("english")))
        # failed to open specified stop word file
        with self.assertRaises(FileExistsError):
            MyCorpusReader('test_directory', 'not a stop word', None)
        c = MyCorpusReader('test_directory', 'stop_word', None)
        # successful load the stop words
        reader = PlaintextCorpusReader(str(os.getcwd()), 'stop_word')
        self.assertEqual(c.stop_words, set(reader.words(['stop_word', ])))

    def test_raw(self):
        # default
        # self.assertEqual(self.mcr.raw(), self.nltk_reader.raw())
        # one file in list format
        self.assertEqual(self.mcr.raw(['text1.txt', ]), self.nltk_reader.raw(['text1.txt', ]))
        # one file in string format
        self.assertEqual(self.mcr.raw('text1.txt'), self.nltk_reader.raw('text1.txt'))
        # two files
        self.assertEqual(self.mcr.raw(['text1.txt', 'text2.txt', ]), self.nltk_reader.raw(['text1.txt', 'text2.txt', ]))

    def test_words(self):
        # one file in list format
        self.assertEqual(self.mcr.words(['text1.txt', ]), list(self.nltk_reader.words(['text1.txt', ])))
        # one file in string format
        self.assertEqual(self.mcr.words('text1.txt'), list(self.nltk_reader.words('text1.txt')))
        # two files
        self.assertEqual(self.mcr.words(['text1.txt', 'text2.txt', ]), list(self.nltk_reader.words(['text1.txt', 'text2.txt', ])))

    def test_sents(self):
        # one file in list format
        self.assertEqual(self.mcr.sents(['text1.txt', ]), list(self.nltk_reader.sents(['text1.txt', ])))
        # one file in string format
        self.assertEqual(self.mcr.sents('text1.txt'), list(self.nltk_reader.sents('text1.txt')))
        # two files
        self.assertEqual(self.mcr.sents(['text1.txt', 'text2.txt', ]), list(self.nltk_reader.sents(['text1.txt', 'text2.txt', ])))

    def test_abspath(self):
        # valid path
        self.assertEqual(self.mcr.abspath('text1.txt'), os.path.join(os.path.abspath('test_directory'), 'text1.txt'))
        # invalid path
        with self.assertRaises(FileExistsError):
            self.mcr.abspath("???")


if __name__ == "__main__":
    unittest.main()

