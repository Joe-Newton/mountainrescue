Welcome to my Project:

The main goal of this project (the combination of both the django website and the twitter stream) will be to take tweets that appear on the
hashtag #savememountainrescue and will strip data from the tweets using twitter API. The coordinates attached to each tweet are to be 
extracted and used to put markers on a google map (which is on my website) depending on how much time I have I may try to add a text box 
that appears on each marker giving the text of the tweet that was sent. Additionally, using the database that I have setup in Django, I
am trying to create an incident report which gives statistics on the incidents that occur for that year (this report is displayed on 
another webpage).

Django:
I have currently got the google map to work on a webpage under the directory "http://127.0.0.1:8000/map" which is the first webpage and I 
have set the centre to near enough the centre of the UK, and I have created a CSS layout on the second webpage under the directory 
"http://127.0.0.1:8000/map/report" but each of the boxes on this webpage has only filler values. I have done some basic logic in the 
"views.py" file in the "map" file that keeps track of how many times certain activities/locations/fatality of incidents occur in the 
database and these values are stored in variables for each activity on the database (same with locations+ whether the injury is minor/m
ajor etc.). My main problem lies here: I cannot put these variables on my webpage "http://127.0.0.1:8000/map/report" as they would need to 
be converted to javascript variables for this to be done (I am struggling to do this). I believe that if this done, the webpage statistics 
will update automatically if the database is updated and the webpage refreshed.Ipredict I will have to convert more python variables to
javascript variables when the coordinates have been extracted from the "twitterdata.txt" file. 

Twitter Stream:
I have written a program that (spearate to the django files) returns all the data about any recent tweet and dumps it in a file. This is 
"twitter-streaming.py" and it runs continually unless terminated. My problem is how the data is dumped in the file - I intend to extract
the "coordinates" section from each of the tweets (only data regarding one tweet is currently in the "twitterdata.txt" file) however I 
have found it difficult to do using basic file extraction methods as each line in the file seems to be different to how I expected due to
indentation. Once the coordinates have been obtained they will somehow have to end up on the webpage as javascript variables to appear as
a marker. Additionally, I think I may look into how to make the "twitter-streaming.py" file to gather tweets and update the map if new 
tweets have been found. Somehow I need to find a way to link these two components together to complete the project. 

Notes:
-I have not included the supporting files that cause "twitter-streaming.py" to work because I couldn't get them to work on Github (I am 
new to GitHub), they are instead on a google drive: https://drive.google.com/drive/folders/12VOfOVsHLGegGZ5qxtSGaRFdvNOqDT3i?usp=sharing

With regard to the "records" folder in Django, ignore it as it was an experiment and I found out It was easier just to add to the views.py file in the "map" folder because the database was already linked to the "map" folder. Also, the fact I don not have a homepage is okay because in the user manual I will provide the correct urls to use.

To run the server to launch the Django website, navigate to where the files are stored locally and type "python manage.py runserver" - I will hopefully put commands like these in a .bat file to make it easier for users to understand.
