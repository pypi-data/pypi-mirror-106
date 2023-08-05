# tweetprep
-----------

A simple python library for preprocessing tweets to make them training
ready. Use it to preprocess the tweets before feeding them to Machine
Learning or Deep Learning models.

The code is Python 2 and 3 compatible.

# Installation
--------------

Fast install:
-------------

::

        pip install tweetprep

For a manual install get this package:
--------------------------------------

.. code:: bash

        $wget https://github.com/garain/tweetprep/archive/master.zip
        $unzip master.zip
        $rm master.zip
        $cd tweetprep-master

Install the package:
--------------------

::

        python setup.py install    

# Example
---------

.. code:: python

        from tweetprep import preprocess
        #from tweetprep import lang_translator

        tweet = "#COVID-19 is the worst pandemic @2020!! :,("
        # get translated tweet
        lang="es"
        print(preprocess.lang_translator.translate(tweet,dest=lang).text)

        # Get processed version of tweet
        print(preprocess.clean(tweet))

Here is the output:
-------------------

::

    # COVID-19 es la peor pandemia @ 2020!! :,(
    covid19 is the worst pandemic crying smiley

Please cite these publications if this library comes to any use:
----------------------------------------------------------------

- Ray, Biswarup, Avishek Garain, and Ram Sarkar. "An ensemble-based hotel recommender system using sentiment analysis and aspect categorization of hotel reviews." Applied Soft Computing 98 (2021): 106935.
- Garain, Avishek, and Sainik Kumar Mahata. "Sentiment Analysis at SEPLN (TASS)-2019: Sentiment Analysis at Tweet Level Using Deep Learning." (2019).
- Garain, Avishek, and Arpan Basu. "The titans at SemEval-2019 task 5: Detection of hate speech against immigrants and women in twitter." Proceedings of the 13th International Workshop on Semantic Evaluation. 2019.
- Garain, Avishek. "Humor Analysis based on Human Annotation (HAHA)-2019: Humor Analysis at Tweet Level using Deep Learning." (2019).
- Garain, Avishek, and Arpan Basu. "The titans at SemEval-2019 task 6: Offensive language identification, categorization and target identification." Proceedings of the 13th International Workshop on Semantic Evaluation. 2019.

