#pip install sklearn
#pip install pydot
#pip install sqlalchemy
#pip install snowflake

#

import os
import base64
from io import BytesIO
import pickle
from textwrap import dedent
import xml

import joblib
from sqlalchemy import create_engine
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder
import plotly.express as px
import pydot
import plotly.graph_objects as go

