# [MyAdviceApp](http://my-advice-app.herokuapp.com/)

Description of the project: </p>
 - This is Python project which was created to practice FastAPI
 - Also, I created a working website that provides three random advices from the open API [adviceslip API](https://api.adviceslip.com/advice)
 - To create the website I used [Grayscale template](https://startbootstrap.com/theme/grayscale) 
 - Finally, I uploaded my project on [Heroku](https://www.heroku.com/) to run the website


## Project:
    
- Python code is in [main.py](https://github.com/AigulTok/MyAdviceApp/blob/master/main.py)
  - It contains code for one-page website and separate pages' website which can be accessed by adding to the original website path separate page title:
    - [/#item](https://my-advice-app.herokuapp.com/#item)
    - [/#about](https://my-advice-app.herokuapp.com/#about)
    - [/#project](https://my-advice-app.herokuapp.com/#project)
    - [/#author](https://my-advice-app.herokuapp.com/#author)
  - The original adviceslip API provides only with one advice at once, therefore I used for loop to extract three random advices at once, because I liked website template's images, and I didn't want to use only one image out of it
- HTML codes from startbootstrap.com that I adapted to my project are in [templates](https://github.com/AigulTok/MyAdviceApp/tree/master/templates)
  - To make one-page website as in original Grayscale template I used [templates/index.html](https://github.com/AigulTok/MyAdviceApp/blob/master/templates/index.html)
  - Also, I divided website to several pages:
    - [templates/item.html](https://github.com/AigulTok/MyAdviceApp/blob/master/templates/item.html)
    - [templates/about.html](https://github.com/AigulTok/MyAdviceApp/blob/master/templates/about.html)
    - [templates/project.html](https://github.com/AigulTok/MyAdviceApp/blob/master/templates/project.html)
    - [templates/author.html](https://github.com/AigulTok/MyAdviceApp/blob/master/templates/author.html)
- CSS and JS codes from templates which remained almost untouched are in [static](https://github.com/AigulTok/MyAdviceApp/tree/master/static) folder