### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?  
**python is more backend oriented such as working on servers, making requests and getting rsponses from a database and different syntax.**
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.  
  **1. get(key[, default]).  
 _Returns the value of the key if the key is in the dictionary otherwise sets default_**.  
 **2.  setdefault(key[, default]).  
 _Returns the value of the key if the key is in the dictionary otherwise sets default_**
- What is a unit test?
**A unit test is when you test functions inside of your code (piece by piece)**
- What is an integration test?
**an integration test, tests for functionality between functions and makes sure they are interacting the way you want**
- What is the role of web application framework, like Flask?
**Flask can help you build and deploy web applications on the World Wide Web.**
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?   
**You use dashes for main parts of the web app and use a query string to have more specific features**
- How do you collect data from a URL placeholder parameter using Flask?   

- How do you collect data from the query string using Flask?   
**You can use request.args which retrieves the arguements from the url**
- How do you collect data from the body of the request using Flask?   

	
- What is a cookie and what kinds of things are they commonly used for?   
**cookies are pieces of information saved about each users session.**
- What is the session object in Flask?   
**session object is the dictionary where all session variables and their associated values are stored.**
- What does Flask's `jsonify()` do?   
  **turns an iterable into JSON format**