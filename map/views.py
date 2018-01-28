# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Incident, PersonInvolved


#provides the webpage for the base map
def homepage(request):
    return HttpResponse("""
                <head>
                   <style>
                       #map {
                        height: 800px;
                        width: 70%;
                       }
                   </style>
                </head>
              <body>
                <h3>Mountain Rescue Map</h3>
                <div id="map">
                #map {
                float:right
                }
                </div>
                <script>
                  function initMap() {
                    var sheffield = {lat: 53.372966,lng:-1.470618};
                    var map = new google.maps.Map(document.getElementById('map'), {
                      zoom: 8,
                      center: sheffield
                    });
                    var marker = new google.maps.Marker({
                      position: sheffield,
                      map: map
                    });
                    var triangleCoords = [
                      {lat: 49.964607, lng: -5.887681},
                      {lat: 54.812678, lng: -5.310899},
                      {lat: 55.695508, lng:  1.824721},
                      {lat: 51.185500, lng:  2.176283}
                    ];
                    var shape = new google.maps.Polygon({
                    paths: triangleCoords,
                    strokeColor: '#000000',
                    strokeOpacity: 0.8,
                    strokeWeight: 2,
                    fillOpacity: 0
                    });
                    shape.setMap(map);

                  }
                </script>
                <script async defer
                src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBm6QBRvfUMvgQXxN9nz9T2wBL_Vx4-Ndw&callback=initMap">
                </script>
              </body>
              <div>
                <a class="twitter-timeline"  href="https://twitter.com/hashtag/savememountainrescue" data-widget-id="912341366470070272">#savememountainrescue Tweets</a>
                <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
              </div>""")

#provides the webpage for the report of incidents
def reportpage(request):
    all_incidents = Incident.objects.all()
    #for the Incident table
    
    #locations
    peak_district = 0
    lake_district = 0
    mid_pennine = 0
    ne_england = 0
    north_wales = 0
    south_wales = 0
    sw_england = 0
    yorks_dales = 0
    total_incidents = 0
    #extracts all records (but only the 'locations' column) from Incidents and stores it as a list
    incident_locations = Incident.objects.values_list('location', flat = True)

    #activities
    fell_running = 0
    hill_walking_summer = 0
    hill_walking_doe = 0
    hill_walking_winter = 0
    hang_gliding = 0
    mountain_biking = 0
    orienteering = 0
    parapenting = 0
    rescue_team_exercise = 0
    rock_climbing = 0
    rock_scrambling = 0
    search = 0
    #extracts all records (but only the 'activities' column) from Incidents and stores it as a list
    incident_activities = Incident.objects.values_list('activity', flat = True)
    



    #for the PersonInvolved table
    
    major_injuries = 0
    minor_injuries = 0
    fatal_injuries = 0
    no_injuries = 0
    total_people_involved = 0
    
    #extracts all records (but only the 'fatality' column) from PersonInvolved and stores it as a list
    person_involved_fatality = PersonInvolved.objects.values_list('fatality', flat = True)


    #counts every time a record contains each activity
    for i in range(0, len(incident_activities)):
        if incident_activities[i] == "Fell Running":
            fell_running = fell_running+ 1
        elif incident_activities[i] == "Hill Walking - Summer":
            hill_walking_summer = hill_walking_summer+ 1
        elif incident_activities[i] == "Hill Walking - DoE":
            hill_walking_doe = hill_walking_doe+ 1
        elif incident_activities[i] == "Hill Walking - Winter":
            hill_walking_winter = hill_walking_winter+ 1
        elif incident_activities[i] == "Hang Gliding":
            hang_gliding = hang_gliding+ 1
        elif incident_activities[i] == "Mountain Biking":
            mountain_biking = mountain_biking+ 1
        elif incident_activities[i] == "Orienteering":
            orienteering = orienteering+ 1
        elif incident_activities[i] == "Parapenting":
            parapenting = parapenting+ 1
        elif incident_activities[i] == "Rescue Team Exercise":
            rescue_team_exercise = rescue_team_exercise+ 1
        elif incident_activities[i] == "Rock Climbing":
            rock_climbing = rock_climbing+ 1
        elif incident_activities[i] == "Rock Scrambling":
            rock_scrambling = rock_scrambling+ 1
        elif incident_activities[i] == "Search":
            search = search+ 1
        total_incidents = total_incidents+1
        
    #counts each time a record contains a certain location
    for i in range(0, len(incident_locations)):
        if incident_locations[i] == "Peak District":
            peak_district = peak_district+ 1
        elif incident_locations[i] == "Lake District":
            lake_district = lake_district+ 1
        elif incident_locations[i] == "Mid Pennine":
            mid_pennine = mid_pennine+ 1
        elif incident_locations[i] == "North-East England":
            ne_england = ne_england+ 1
        elif incident_locations[i] == "North Wales":
            north_wales = north_wales+ 1
        elif incident_locations[i] == "South Wales":
            south_wales = south_wales+ 1
        elif incident_locations[i] == "South-West England":
            sw_england = sw_england+ 1
        elif incident_locations[i] == "Yorkshire Dales":
            yorks_dales = yorks_dales+ 1
        total_incidents = total_incidents+1

        
    #counts every time a record contains each tier of injury    
    for x in range(0, len(person_involved_fatality)):
        if person_involved_fatality[x] == "Major Injury":
            major_injuries = major_injuries+ 1
        elif person_involved_fatality[x] == "Minor Injury":
            minor_injuries = minor_injuries+ 1
        elif person_involved_fatality[x] == "Fatal Injury":
            fatal_injuries = fatal_injuries+ 1
        elif person_involved_fatality[x] == "No Injury":
            no_injuries = no_injuries+ 1
        total_people_involved = total_people_involved  + 1
        
        


    
    html = """<h1 align = "center"> Incident Report </h1>
<br>
<br>
<br>
       <head>
   
      <style type="text/css">
         table.empty{
            width:1750px;
            border-collapse:separate;
            empty-cells:hide;
         }
         td.empty{
            width:50px;
            padding:5px;
            border-style:solid;
            border-width:1px;
            border-color:#999999;
            
            
            
         }
         .left{
           float:left;


         }
         .right{
          float:right;
         }
         th.sidebyside{
           width:245px;
           padding:5px;
           border-style:solid;
           border-width:1px;
           border-color:#999999;

         }
         th.border{
           padding:5px;
           border-style:solid;
           border-width:1px;
           border-color:#999999;
         }
      </style>
      
   </head>
   <body>
   
      <table class="empty">
      <tr>
         <th></th>
         <div class = "border">
         <th>Peak District</th>
         <th>Lake District</th> 
         <th>Mid Penines</th>
         <th> Mid Penines </th>
         <th> Mid Penines </th>
         <th> North Wales </th>
         <th> South Wales </th>
         <th> South-West England </th>
         <th> Yorkshire Dales </th>
         <th> Total </th>
         </div>
      </tr>
      
      <tr>
         <th class = "sidebyside"><div class = "left">Fell Running </div> <div class = "right">Incidents:<br>Subjects: </div></th>
         <td class="empty" id = "test"></td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
      </tr>
      
      <tr>
         <th class = "sidebyside"><div class = "left">Hill Walking - Summer </div> <div class = "right">Incidents:<br>Subjects: </div></th>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
      </tr>
      
      <tr>
         <th class = "sidebyside"><div class = "left">Hill Walking - DoE </div> <div class = "right">Incidents:<br>Subjects: </div></th>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
      </tr>
      
      <tr>
         <th class = "sidebyside"><div class = "left">Hill Walking - Winter </div> <div class = "right">Incidents:<br>Subjects: </div></th>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
      </tr>
      
      <tr>
         <th class = "sidebyside"><div class = "left">Hang Gliding </div> <div class = "right">Incidents:<br>Subjects: </div></th>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
      </tr>
      
      <tr>
         <th class = "sidebyside"><div class = "left">Mountain Biking </div> <div class = "right">Incidents:<br>Subjects: </div></th>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
      </tr>
      
      <tr>
         <th class = "sidebyside"><div class = "left">Orienteering </div> <div class = "right">Incidents:<br>Subjects: </div></th>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
      </tr>
      
      <tr>
         <th class = "sidebyside"><div class = "left">Parapenting </div> <div class = "right">Incidents:<br>Subjects: </div></th>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
      </tr>
      
      <tr>
         <th class = "sidebyside"><div class = "left">Rescue Team Exercise </div> <div class = "right">Incidents:<br>Subjects: </div></th>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
      </tr>
      
      <tr>
         <th class = "sidebyside"><div class = "left">Rock Climbing </div> <div class = "right">Incidents:<br>Subjects: </div></th>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
      </tr>
      
      <tr>
         <th class = "sidebyside"><div class = "left">Rock Scrambling </div> <div class = "right">Incidents:<br>Subjects: </div></th>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
      </tr>
      
      <tr>
         <th class = "sidebyside"><div class = "left">Search </div> <div class = "right">Incidents:<br>Subjects: </div></th>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
      </tr>
      
      <tr>
         <th class = "sidebyside"><div class = "left">Total </div> <div class = "right">Incidents:<br>Subjects: </div></th>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
         <td class="empty">value</td>
      </tr>
      </table>
      <script type = "text/javascript">
      var fell = "{{fell_running}}";
      document.getElementById("test").innerHTML = fell
      




      </script
      
   </body>
    """
    return HttpResponse(html)






