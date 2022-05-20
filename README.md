# Personal-Blog

## Built By [Kipkemoi Elvis](https://github.com/DynastyElvis)


You can view the site at: [ My Blogpost Live Link](https://pitches-posts.herokuapp.com/ytidcdytic)


## Screenshots


## Description
This is a personal blogging website where you can create and share your opinions and other users can read and comment on them. Additionally it has a feature that displays random quotes to inspire your users.

[Go Back to the top](#Personal-Blog)


## My Blogs
The user would like to.... :
*  View the blog posts on the site
*  Comment on blog posts
*  View the most recent posts
*  An email alert when a new post is made by joining a        subscription.
* See random quotes on the site

The writer would like to... :

* see random quotes on the site
* sign in to the blog.
* create a blog from the application.
* delete comments that I find insulting or degrading.
* update or delete blogs I have created.



[Go Back to the top](#Personal-Blog)

## Behaviour Driven Development
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| View blog | Click on comment | Taken to the clicked post | Click on `Comment` | Taken to where you can comment | Signs In/ Signs Up |
| Click on `Click Add a blog` | If logged in, display form to add a blog| Redirected to the home page |
| Click on profile | Redirects to the profile page | User adds bio and profile picture |
| Click on Sign Out | Redirects to the home page | Signs user out |

[Go Back to the top](#Personal-Blog)

## Getting started

### Prerequisites
* python3.8
* virtual environment
* pip
* Markfile


[Go Back to the top](#Personal-Blog)

### Cloning
* In your terminal:
        
        git clone https://github.com/DynastyElvis/Personal-Blog

        cd Personal-Blog

[Go Back to the top](#Personal-Blog)

## Running the Application
* Install virtual environment using `$ python3.8 -m venv --without-pip virtual`

* Activate virtual environment using `$ source virtual/bin/activate`

* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`

* Creating the virtual environment

        $ python3.8 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.8 -m pip install Flask
        $ python3.8 -m pip install Flask-Bootstrap
        $ python3.8 -m pip install Flask-Script

* Install all the dependencies from the requirements.txt file by running `python3.8 pip install -r requirements.txt`

* Create a `start.sh` file in the root of the folder and add the following code:

        export MAIL_USERNAME=<your-email-address>
        export MAIL_PASSWORD=<your-email-password>
        export SECRET_KEY=<your-secret-key>

* Edit the configuration instance in `manage.py` from `development` to `production`
* To run the application, in your terminal:

        chmod a+x start.sh
        ./start.sh

[Go Back to the top](#Personal-Blog)

## Testing the Application
* To run the tests for the class file:

        python3.8 manage.py server

 [Go Back to the top](#Personal-Blog)
       
## Built With

* [Python3.6](https://docs.python.org/3/)
* Flask
* Boostrap
* HTML
* CSS

[Go Back to the top](#Personal-Blog)


## License

[MIT LICENCE](https://github.com/DynastyElvis/Personal-Blog/blob/main/LICENSE)


Copyright (c) 2022 K. E. Rono


[Go Back to the top](#Personal-Blog)

## Known Bugs

No Known Bugs.

## Support and contact details
 Incase you come across errors, have questions, ideas ,concerns, or want to contribute to the application, feel free to reach me at :kipkemoilvs@gmail.com

## Authors Info
LinkedIn - [KIPKEMOI ELVIS RONO](https://www.linkedin.com/in/elvis-rono-aa3548209/)

[Go Back to the top](#Personal-Blog)