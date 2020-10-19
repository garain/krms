# krms
-----------

A simple python library for implementing the K-RMS Clustering algorithm on
unlabelled data using unsupervised learning. 


The code is Python 2 and 3 compatible.

# Installation
--------------

Fast install:
-------------

::

        pip install krms

For a manual install get this package:
--------------------------------------

.. code:: bash

        $wget https://github.com/garain/krms/archive/master.zip
        $unzip master.zip
        $rm master.zip
        $cd krms-master

Install the package:
--------------------

::

        python setup.py install    

# Example
---------

.. code:: python

        from krms import krms_clustering
        
        #For results related to Iris dataset no need to pass any argument.
        krms_clustering.run()
		
        #For getting results from custom dataset pass path of csv file as argument in function 'run'. 
        krms_clustering.run("data.csv")
		

N.B.: The csv file should have the labels in first column with header name 'type' followed by rest of feature columns.

# References
---------------

:: 
        
		@article{GARAIN2020113,
                title = "K-RMS Algorithm",
				journal = "Procedia Computer Science",
				volume = "167",
				pages = "113 - 120",
				year = "2020",
				note = "International Conference on Computational Intelligence and Data Science",
				issn = "1877-0509",
				doi = "https://doi.org/10.1016/j.procs.2020.03.188",
				url = "http://www.sciencedirect.com/science/article/pii/S1877050920306530",
				author = "Avishek Garain and Dipankar Das",
				keywords = "clustering, distortion-error, rms-value, multi-component analysis, unsupervised-learning"
				}