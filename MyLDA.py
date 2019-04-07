# Joseph Melton and Parakh Jaggi
# LDA Create
# 3/29/2019

import os
import gensim
from gensim import corpora
import MyCorpusReader


def LDACorpus(corpus, outputDir='lda_out', binary=False, num_topics=10, alpha=-1, eta=-1):
    # Convert the MyCorpusClass to a corpus that gensim can understand
    corpus = MyCorpusReader.MyCorpusReader('test_directory')

    texts = corpus.raw().split()
    texts = [d.split() for d in texts]

    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    r = dictionary
    #print(r)

    # checking if dir is already made
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    # if binary:
    if binary:
            texts = list(set(texts))
    # checking valid topics number have been request
    if num_topics < 0:
        print("Invalid number of topics requested")
        exit(1)

    # setting default alpha
    if alpha == -1:
        alpha = 'symmetric'
    # exiting now to prevent crashing if invalid alpha provided
    elif alpha != 'auto' or alpha != 'asymmetric':
        print("Invalid alpha value provided, please use 'auto' or 'asymmetric'")
        exit(1)

    # setting default eta
    if eta == -1:
        eta = None

    lda = gensim.models.ldamodel.LdaModel(corpus, num_topics, alpha=alpha, eta=eta, id2word=r)
    makeDtmatrix(lda, outputDir, corpus)
    make_topics(lda, outputDir)
    # displaying our 10 topics (demo purposes only)
    #outputMyLDA(lda)


# creates a file named dtmatrix that stores doc/topic matrix
def makeDtmatrix(lda, outputDir, corpus):
    # getting path to python script
    here = os.path.dirname(os.path.realpath(__file__))
    filename = 'dtmatrix'

    # getting path to subdir
    filepath = os.path.join(here, outputDir, filename)

    testdirpath = os.path.join(here, 'test_directory')
    os.listdir('test_directory')

    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(testdirpath)
    allFiles = list()

    try:
        file = open(filepath, 'w')
        # Iterate over all the entries
        for entry in listOfFile:
            # Create full path
            fullPath = os.path.join(testdirpath, entry)

            # get topic probability for each topic for doc
            file.write(fullPath[-13:])
            file.write(' ')
            file.write((str(lda.get_document_topics(corpus)[0][0])))
            file.write((str(lda.get_document_topics(corpus)[0][1])))
            file.write('\n')


        file.close()
    except IOError:
        print('Wrong path provided')


# creates files for each topic generated in the _topics subdir
def make_topics(lda, outputDir):
    # get path to python script
    here = os.path.dirname(os.path.realpath(__file__))

    filename = "topic_"
    # joining together path for _topics dir
    outputDir = os.path.join(here, outputDir, '_topics')

    # create _topics subdir
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    for i in range(0, lda.num_topics):
        # adding digit to end of filename
        filename += str(i)
        # getting correct path to _topics dir
        filepath = os.path.join(outputDir, filename)

        # need to loop over all topics and create files for each
        try:
            f = open(filepath, 'w')
            # need to write word, and corresponding probablity for topic to file
            for x in range(len(lda.show_topic(i, topn=10000))):
                f.write(str((lda.show_topic(i, topn=10000)[x])))
                f.write('\n')
            f.close()
        except IOError:
            print('Wrong path provided')
        # removing last char of our filename for next digit to replace
        filename = filename[:-1]


def outputMyLDA(lda):
    for i in range(0, lda.num_topics):
        print('topic #', i, lda.print_topic(i))


if __name__ == "__main__":
    LDACorpus(MyCorpusReader)
