ALIC DANCE MINISTRY WEBSITE
    This is a website for a dance group that Serve in at our local church.
I thought it would be a good idea to use my final project to solve a real world problem
as we did not have a website prior to this.

    This is a website that allows users to get more information about the group and also
its individual members. I included the following features:
    1) Registration and log in(optional).
    2) Contact form that users can submit messages to our email adress.
    3) Bookings page that uses google forms for event booking.
    4) Media page that embeds all our youtube videos and images to the site.
    5) Mobile responsivity

FILES
A)STATIC
        -about.css: contains styling for the about page
        -posts.css: Contains styling for the media page
        -style.css: contains styling for the login and register pages
        -styles.css: contains styling for the index page
        -index.js: contains scripting for the index page
        -posts.js: contains scripting for the media page
        -MEDIA: Contails all uploaded images

B)TEMPLATES
        -layout.html: layout for the site
        -index.html: Landing page
        -login.html: login page
        -register.html: registration page
        -posts.html: Media page structure
        -about-us-details.html: Page that displays more information about us




DISTINCTIVENESS AND COMPLEXITY
First, this project is a fully fledged website that could be deployed for use in real world application.
It is fully mobile responve and utilizes 9 Django models to store users and all the media files.
File uploads are only done by the admin so you should create a superuser account.

It is different from all the other coursework projects as it allows for the Admin to be notified of user
communication from the site using Django email. To use this feature, make sure to go to the settings.py file
in the project directory and find #EMAIL SETTINGS. Update the HOST EMAIL ADDRESS and the HOST PASSWORD values.
The final step will be to navigate to the views.py file in the alic application folder, find the view called
mesage and update the send_to email address that specifies which email address will receive the message.
Additionally I have incorporated google forms to my site allowing the admin to receive email notifications for any bookings.

Also, the media route serves all  media files. The admin is responsible for uploading youtube
links to the appropriate playlist models i.e:
                                -Nuggets
                                -Reels
                                -Dancehall
                                -Afrobeat
                                -Hip-Hop
                                _Hangout
                                -Amapiano
Once this is done, the links are embeded in the site allowing users to view the videos just like on youtube. This makes use of the django-embed-video package.
Furthermore, I have used youtube's data api to make calls to youtube that provide us with statistical data about each individual video such as:
                                - Likes Count
                                - Comment Count
                                - Dislike Count
                                _ Views Count
When one hovers over a video, an api call is made asynchronously for that particular video and using javascript they are displayed to the user.
Finally, The application also has an image gallery for all Images uploaded by the admin.

