#!/usr/bin/env python
# coding: utf-8

# In[4]:


#apply libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


#read csv file
ttc = pd.read_csv(r'C:\Users\bhave\OneDrive\Desktop\code\project\titanic.csv')


# In[6]:


ttc.shape


# In[7]:


# chake the first five rows
ttc.head(5)


# In[8]:


#chacking null values 
ttc.isnull().sum()


# In[9]:


ttc.describe()


# In[10]:


#removing Cabin column 
ttc = ttc.drop('Cabin', axis = 1)


# In[11]:


ttc.isnull().sum()


# In[12]:


#replacing null values in age column
ttc['Age'].fillna(np.mean(ttc['Age']),inplace=True)


# In[13]:


#replacing null values in embarked column with mode value
md= ttc.Embarked.mode
ttc['Embarked'].fillna(md, inplace=True)


# In[14]:


#Drop unwanted columns
ttc.drop(['PassengerId','Name'], axis = 1, inplace=True)


# In[15]:


ttc


# In[16]:


#Encoding for character columns (Sex, Embarked)
gender = pd.get_dummies(ttc['Sex'], drop_first=True)


# In[17]:


ttc


# In[18]:


ttc.drop(['Sex','Ticket','Embarked'], axis=1, inplace = True)


# In[19]:


ttc


# In[20]:


ttc = pd.concat([ttc,gender], axis=1)


# In[21]:


ttc


# Visual Analysis

# In[22]:


sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='male',data=ttc)


# in this chart we observed 0 is dead and 1 is survived
# and more female get survived coumpare to male

# In[23]:


sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Pclass',data=ttc)


# in this chart we observed the survived pepole by Class
# 1st class pepole servived more the 3rd class and 2nd class

# In[32]:


#Frequency distribution of ages of passengers on Titanic
ttc['Age'].hist(bins=20)


# we observed in this chart the pepole count by there age

# In[33]:


ttc['Pclass'].value_counts().plot.pie()


# in this pie chart vi observed the pepole count by class

# In[34]:


ttc


# In[35]:


X = ttc.iloc[:,1:]
y = ttc.Survived


# In[36]:


y.shape


# In[37]:


from sklearn.model_selection import train_test_split


# In[38]:


x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2)


# In[39]:


x_train.shape


# In[40]:


x_test.shape


# Applying Decision Tree

# In[41]:


from sklearn.tree import DecisionTreeClassifier


# In[43]:


model = DecisionTreeClassifier()
model.fit(x_train,y_train)


# In[46]:


y_pred = model.predict(x_test)


# In[45]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)


# In[ ]:




