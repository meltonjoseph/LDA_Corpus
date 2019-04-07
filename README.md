# NLPUGProj19

CSI 5360/4V96 Natural Language Processing


Undergraduate Project/Presentation
Individual work for group 4


While NLTK does not have support for topic models, there has been a few other implementations. One
of them is the module gensim (https://radimrehurek.com/gensim/) . It provides implementation of LSA
and LDA.


Using the LDA API provided by gensim (specifically models.ldamodel), implement the following function:


LDACorpus(corpus, outputDir = “lda_out”, binary = false, num_topics=10, alpha=-1, eta=-1)

• corpus = A MyCorpusReader object (as defined in part 1)

• outputDir = string denoting directory where the output file is stored (directory relative to the
current directory). If the directory does not exist, create it.

• binary = if true, each document is represented by a binary vector (only denote whether a word
exists or not), otherwise, use the count() of each word
• num_topics = number of topics

• alpha = the alpha parameter for the lda class in gensim. If alpha is set to a negative number
(default), the default alpha for ldamodel class is used

• eta = the eta parameter for the lda class in. If it is set to a negative number, the default eta for
the ldamodel class is used.


The method should run LDA on the corpus specified. You will need to convert the corpus to the input
format of LDA (be mindful of the binary variable). You function should also do the following:


• Create the following file inside the directory

• “dtmatrix”: the function should create a file that store the document/topic matrix. Each
line should represent a document in the corpus. The first string for each line should
correspond to the filename of that document, after that, it should list the probability for
each topic for that document.

• Also create the following subdirectory inside the directory, and create the files list below

• “_topics”: the function should create a file for each topic that is generated. Each file
corresponds to a topic (you should label the file topic_1, topic_2, …, and so on). Each
line of the file should contain a word and its corresponding probability for that topic.
The topic number should match the ordering of the topic in the dtmarix file.
Your function should output the ldamodel object that is used to generate the LDA model. 