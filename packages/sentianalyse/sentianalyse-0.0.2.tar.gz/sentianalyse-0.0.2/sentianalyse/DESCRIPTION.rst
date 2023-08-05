# sentianalyse
-------------------

A simple python library that generates sentiment type(positive,negetive,neutral)
pie chart, percentage,number and ternary value for pandas dataframe text portion.

The code is Python 2 and 3 compatible.

# Installation
--------------

Fast install:
-------------

::
        pip install sentianalyse

For a manual install get this package:
--------------------------------------

.. code:: bash

        $wget https://github.com/garain/sentianalyse/archive/master.zip
        $unzip master.zip
        $rm master.zip
        $cd sentianalyse-master

Install the package:
--------------------

::

        python setup.py install    


# The library is pandas dataframe dependent.
--------------------------------------------
::
Have to get dataframe('text columns') and give to command.
Like df['text']


# Example
---------

.. code:: python

        import sentianalyse as sa
		# Features
		
        # - sentiment type pie chart :
        sa.pie()

        
        # sentiment type amount : 
        # - Get the sentiment type(postive,negetive,neutral numbers)
        sa.number()
               
        
        # sentiment percentage :
        # - Get the percentage of sentiment type
        sa.percentage() 
                
        
        # sa.ternary_analysis
        # - Get the type of all text, here -1:negetive, 0:neutral, 1:positive
        sa.ternary_analysis()
               
           
        import pandas as pd
        
        df=pd.read_csv("/home/samin/anaconda3/dataset_2.csv")
        
        percent=at.percentage(df['text'])
        
        print(percent)
        
        
        number = sa.number(df['text'])
        
        print(number)
        
        
        analysis = sa.analysis_ternary(df['text'])
        
        print(analysis)
        
        
        #sa.pie(df['text'])
		
        # Pass list of texts as input
		
		df=pd.DataFrame(["I love you very much."],columns=['text'])


Here is the output:
-------------------

::

    Positve : 33.31 %, Negetive 20.96 %, Neutral : 45.72 %
    {'positive  ': 1087, 'negetive': 684, 'neutral': 1492}
	[-1, 1, 0.0, 0.0, 0.0, 0.0,.......,1]

Please cite these publications if this library comes to any use:
----------------------------------------------------------------

- Ray, Biswarup, Avishek Garain, and Ram Sarkar. "An ensemble-based hotel recommender system using sentiment analysis and aspect categorization of hotel reviews." Applied Soft Computing 98 (2021): 106935.
- Garain, Avishek, and Sainik Kumar Mahata. "Sentiment Analysis at SEPLN (TASS)-2019: Sentiment Analysis at Tweet Level Using Deep Learning." (2019).
- Garain, Avishek, and Arpan Basu. "The titans at SemEval-2019 task 5: Detection of hate speech against immigrants and women in twitter." Proceedings of the 13th International Workshop on Semantic Evaluation. 2019.
- Garain, Avishek. "Humor Analysis based on Human Annotation (HAHA)-2019: Humor Analysis at Tweet Level using Deep Learning." (2019).
- Garain, Avishek, and Arpan Basu. "The titans at SemEval-2019 task 6: Offensive language identification, categorization and target identification." Proceedings of the 13th International Workshop on Semantic Evaluation. 2019.

