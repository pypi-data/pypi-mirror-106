# ggwp: Prepare Fast, Analyze Faster  
[![PyPI Latest Release](https://img.shields.io/pypi/v/ggwp)](https://pypi.org/project/ggwp/) 
[![Downloads](https://img.shields.io/pypi/dm/ggwp)](https://pypi.org/project/ggwp/)
[![Repo Size](https://img.shields.io/github/repo-size/datanooblol/ggwp)](https://pypi.org/project/ggwp/)
[![License](https://img.shields.io/pypi/l/ggwp)](https://pypi.org/project/ggwp/)
[![Release Date](https://img.shields.io/github/release-date/datanooblol/ggwp)](https://pypi.org/project/ggwp/)

## What is ggwp?

**ggwp** is a Python package for fast and easy data analytics.  
It aims to make a data model that can be applied for some use cases  
such as customer analytics. The data model created by ggwp is designed  
directly from my personal experiences, which will be more and more data models  
in the future. In addition, **ggwp** now has some new features for  
logging, modeling and evaluating your models, which of these can speed up your workflow  
FOR REAL!!

## Main Features  
Here are current features available in **ggwp**  

For Data Modeling: check out -> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1BcbHZjwNHsxtypOhu9KgddPOY28N5Xtt?usp=sharing)  
-  DataModel: prepare your raw data for a general data model
-  EzCheck: check your data quality
-  EzRFM: create RFMT dataset
-  EzCohort: create Cohort dataset
-  EzCustomerMovement: create Customer Movement dataset
-  EzBasketEvolving: create Basket Evolving dataset

For Logging, Modeling, Evaluation: check out -> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1uMNnpK-4x8wAq5pVsahWePnKzQNZdClK?usp=sharing)  
-  EzLog: log your data status and your remark, so you know what you've done for each stage
-  EzEvaluation: evaluate your model using traditional (R2, RMSE, F-1, ACC, ROC) and practical metrics (Cost&Benefit, Lift)
-  EzBenchMark: benchmark your models' performances giving you some intuition
-  EzPipeline: integrate pandas with sklearn

## Where to get **ggwp**  
The source code is currently hosted at GitHub:  
https://github.com/datanooblol/ggwp  

The latest version is available at  
[Python Package Index (PyPI)](https://pypi.org/project/ggwp/)  

```sh  
# pip  
pip install ggwp  
```  

## Dependencies  

-  numpy  
-  pandas  
-  sklearn
-  xgboost

## Disclaimer  
**ggwp** is now in devoping phase. Hence, if you experience any inconveniences, please be patient...