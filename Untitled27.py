#!/usr/bin/env python
# coding: utf-8

# In[3]:


#GET method: It is a type of HTTP request method used to request data from a specified resource. It sends data in the URL, and this data is visible in the URL parameters. It is primarily used for data retrieval and should have no other effect on the data.

#Example:
#GET /example?name=John&age=25 HTTP/1.1

#POST method: It is a type of HTTP request method used to submit data to be processed to a specified resource. Unlike GET, the data sent to the server is not visible in the URL. It is often used for submitting forms and can send larger amounts of data compared to GET.

#Example:
#POST /submit-form HTTP/1.1
#Content-Type: application/x-www-form-urlencoded

#name=John&age=25




# In[4]:


#In Flask, the request object is used to access incoming request data, which includes form data, query parameters, file uploads, and more. It provides an easy way to interact with the data sent by the client to the server. For example, you can use request.form to access form data in a POST request or request.args to access query parameters in a GET request.


# In[5]:


#The redirect() function in Flask is used to redirect the client to a different URL. This is commonly used after processing a form submission or handling some other request to guide the user to a new location. It helps in achieving a clean separation of concerns by allowing different routes to handle different aspects of the application logic.


# In[6]:


#Templates in Flask are used for generating dynamic HTML content by embedding variables, control structures, and other dynamic elements. The render_template() function is used to render templates in Flask. It takes the name of the template file and any variables to be passed to the template as arguments. This function allows you to create HTML pages with placeholders for dynamic content, making it easier to generate dynamic web pages.


# In[7]:


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello, World!')

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




