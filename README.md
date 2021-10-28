## Machine Learning Project-- The iris dataset example 

#### Software Environment
1. Python 3.8.8
2. Django 3.2.7
3. Pycharm Professional 
4. JDK 11
5. Spark 3.1.2
6. Firebase Realtime 
7. Firebase Storage 

#### The Functions this project realized: 
***1. Load raw data into the system***

***2. Extract metadata (e.g., # of attributes, rows, file size, or meta data from images/videos)
from the raw data (including text files such as CSV)***

***3.Clean and/or transform the data if needed.***

**4.extract features from the raw data By Spark.**

**5. Store extracted features in the database.**


***6. Select prediction/inference problems intuitively.***

***7. Store the inference results in the database.***


#### The explanation of the data:

The dataset is from Kaggle https://www.kaggle.com/uciml/iris. This dataset is a very popular and useful dataset to 
learn about maachine learning. The Main goal of this project is not only the classification of Iris species, but also 
***learn how to utilize various tools from back-end to front-end to actually build a simple website for a beginner.***

**Metadata:**

SepalLengthCm : the Length of Sepal (cm)

SepalAreacm2 : the area of sepal (cm^2)

SepalWidthCm : the width of sepal (cm)

PetalWidthCm : the width of Petal (cm)

PetalAreacm2 : the area of Petal (cm^2)

PetalLengthCm : the length of Petal (cm)

Species : the species of this data

#### The Django Framework Explanation:

Django is a very powerful and simple Web Framework. The core functions I learned from this project are the following:

1. Templete Folder: the HTML script, JS script

2. Views.py: Interact with the back-end machine learning Algorithm and with the urls.py 

3. urls.py: Connect the Front-end with the back-end (views). Navigate the direction of HTTP  request 

Since I used the Cloud database, I did not explore the use of Sqlite3 in Django. Except the Data Store, the Django 

Framework actually is about these three files.


#### The Spark :
In this Project, I utilize the Spark for feature selection by Chi-square selection method and store the result into the realtime database. 

I did not just use the above original features. I added their cross products as new feature candidates. Thus, there are totally 56 features available. 



#### The machine learning algorithm:
 
This project used the Quadratic Discriminant Analysis as the machine learning Algorithm method. The reason that I choosed QDA but not Logistic Regression Algorithm is:

QDA is better than Logistic regression:

**1. when we have a small dataset.**

**2. when it is a multiclass problem.**

