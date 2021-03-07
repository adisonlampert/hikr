#hikr
### An all-in-one hike planner website.
 
## :sunrise_over_mountains: What Inspired Us
We got into hiking during the pandemic because it is a safe way to explore the outdoors, get exercise, and have fun! However, finding new hiking trails can be difficult for new hikers. Visiting multiple websites to check the weather, open hours, and location is tedious and takes the spontaneity away from trekking through the wilderness. So, we built hikr, an all-in-one hiking planner, to connect people to hiking trails in their area and give them all of the information they need to OWN their hike.


## :sunrise_over_mountains: What It Does

A hike-enthusiast can search any location whether that’s their home address, city, or their favorite donut shop (for a “post-hike” snack) to get information on nearby trails. The closest trails are displayed Pinterest-style on our nifty search result page and users can click on locations to find out the essential information for planning their next hike. Clicking on a trail will take them to a page that displays valuable information such as open hours, the upcoming weather, and photos of the trails so that the hiker can plan their next adventure with ease.


## :sunrise_over_mountains: What We Learned

###Python Flask
This was our first project using Python Flask so it was an opportunity to improve upon our Flask knowledge. We learned how to use Flask throughout the entire web page such as for loops with Jinja to create content.

###APIs
It was also our first major project using APIs so we were able to learn more about json format and about sending requests via APIs. We had the opportunity to explore the various API options and learn about choosing the right API. We nearly died reading all of the documentation, but the result was worth it!

###Web Development
We improved our CSS, HTML, and Javascript knowledge and learned how to implement various features. We explored the Bootstrap framework and the possibilities of Bootstrap such as a photo carousel.

###Google Cloud Platform
This was the first time we ever used Google Cloud Platform and it ended up being an integral part of our project. Google Cloud Platform provided us with the Google Places API and Google Geocode API that allowed us to find nearby hiking locations from a given location. Additionally, we used Google App Engine to deploy our website.

## :sunrise_over_mountains: How We Built It

###Python Flask
Flask handled the back-end of the project. We used Flask to communicate with APIs, organize data, and dynamically generate content.

###Bootstrap
Most of our front-end was designed with Bootstrap.

###Google Places API and Google Geocode API
Google Geocode determines the latitude and longitude of the address entered in the search bar. Google Places uses the latitude and longitude to find hiking trails within a 10km radius of the location. We also used Google Places to collect data about the trails.

###OpenWeather API
The open weather API allowed us to gather weather information based on the latitude and longitude of the trail.

###Google App Engine
We used Google Cloud’s Google App Engine to host our Flask application.


##:sunrise_over_mountains: Challenges

Our first challenge was finding the correct APIs to use for the project. After finding several dead-ends in the quest for an API that could find hiking trails, we stumbled upon Google Places API. We then realized we would need the latitude and longitude of the user in order to search nearby trails. Google Geocode API was the answer to this since it takes an address and returns the coordinates. We had to get a little creative with our request, but in the end we were able to get the data we needed.

Our next challenge was getting Flask to work. We had a lot of particular ideas about how we wanted information displayed, especially information in the url. We ultimately discovered that we could use the Flask routing to redirect features along with a post request to specify the URL query. Additionally, it was confusing getting Flask to properly work in the HTML templates. This required a lot of google searching to find the proper syntax, but by the end we had learned so much more about Flask.

Google App Engine taught us patience. We struggled to figure out why our website was getting a 502 Bad Gateway error for a long time and had to read *many* Medium articles on deploying Flask applications in GAE before realizing how to set up the files so that GAE knew what we wanted to do. Ultimately, we were successful in deploying!!

## :sunrise_over_mountains: What We’re Proud Of

We are in love with this project. It’s absolutely our baby and we’re so thrilled with how it turned out. The entire project was very seamless except for a few challenges. Triumphing over the errors and completing our project feels amazing and we are so excited to present hikr to the world!

## :sunrise_over_mountains: What’s Next for hikr
- Ability for users to create accounts and save users favorite trails
- More specific search categories based on user preferences for weather, time of day, etc.
- An algorithm to determine the best time and day for the perfect hike.
