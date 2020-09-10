#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib as s
from email.mime.text import MIMEText


# In[2]:


ob = s.SMTP("smtp.gmail.com",587)


# In[3]:


ob.starttls()


# In[4]:


ob.login("gmail","password")


# In[5]:


subject = "sending eamil"


# In[6]:


body = "this email i s sending email for you"


# In[7]:


message = "Subject:{}\n\n{}".format(subject,body)


# In[8]:


message


# In[9]:


listofaddress = ['anantbansal643@gmail.com','anantbansal643091@gmail.com','amankmrbansal0490454@gmail.com']


# In[11]:


ob.sendmail("ravizc109",listofaddress,message)


# In[ ]:


ob.quit()


# In[ ]:





# In[ ]:




