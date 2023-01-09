

# <h1 align="center" id="heading">FastAPI for Machine Learning</h1>

This repository contains the files to build your very own AI image generation web application! Outlined are the core components of the FastAPI web framework.



![alt text](https://github.com/JasonSCFu/FastAPI-to-deploy-ML-model/blob/main/output.PNG)



## What is FastAPI?

It is a high-performance web framework to build APIs in Python. Traditionally, most of the developers used flask as the first option to build the API but due to some of the limitations but not limited to data validation, authentication, async, and many more, FastAPI gained a lot of popularity. FastAPI offers automatic docs generation functionality, authentication, data validation via pydantic models.

FastAPI helps in setting up the production-ready server but what if you want to share this with your team before deploying it in an actual cloud platform such as Heroku. The ngrok comes to the rescue by tunneling your localhost and exposing it to the internet. Anyone can access your API endpoint via the link provided.

 pydantic deals with data parts, starlette deals with web parts.

## Data and model
The problem statement I would be using in this repo is a decision tree classifier to classify between two music genres: Hip-Hop or Rock. I have already done the cleaning of the dataset and saved as data.csv in this repo. I have simply imported it into the notebook and trained a decision tree model without any preprocessing or EDA stuff as this article is more about deployment. Therefore, this model may return some wrong results!

The model is saved as model_tree.pkl which I have also uploaded in thie repo. Run the model_building.py will generate this pickle file.



## Steps to create the result

1: Run the model_building.py to create the model_tree.pkl.

2: main.py is the key FastAPI setting and config. You dont need to modify. In the terminal, type uvicorn main:app. Then go to http://127.0.0.1:8000/docs to test the API result.
