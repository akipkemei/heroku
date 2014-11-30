/* Define base layers */
var cycleURL='http://{s}.tile.thunderforest.com/cycle/{z}/{x}/{y}.png';
var cycleAttrib='Map data © OpenStreetMap contributors';
var opencyclemap = new L.TileLayer(cycleURL, {attribution: cycleAttrib}); 

var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib='Map data © openstreetmap contributors';
var osm = new L.TileLayer(osmUrl, {attribution: osmAttrib}); 

/* create new layer group */
var layer_apartments = new L.LayerGroup();
var array_markers = new Array();

/* create custom marker which will represent apartments in layer 'layer_apartments' */
customMarker = L.Marker.extend({
   options: { 
      title: 'Name of the apartment',
   }
});

/* define function which adds markers from array to layer group */
function AddPointsToLayer() {
    for (var i=0; i<array_markers.length; i++) {
        array_markers[i].addTo(layer_apartments);
    }
} 

/* Get all apartments from DB and add them to layer:_apartments */
$.ajax({
    url: '/map/get-apartments/',
    type: 'GET',
    success: function(response) {
        $.each(eval(response), function(key, val) {      
            //fields in JSON that was returned          
            var fields = val.fields; 

            // parse point field to get values of latitude and longitued
            var regExp = /\(([^)]+)\)/;
            var matches = regExp.exec(fields.geom);
            var point = matches[1];
            var lon=point.split(' ')[0];
            var lat=point.split(' ')[1];

            //function which creates and adds new markers based on filtered values
            marker = new customMarker([lat, lon], {
                title: fields.name,
                opacity: 1.0  
            }); 
            marker.bindPopup("<strong>Name: </strong>" + fields.name + "<br><strong>City: </strong>"
                + fields.city + "<br><strong>Price: </strong>"+ fields.price);
            marker.addTo(map);
            array_markers.push(marker);
        });

        // add markers to layer and add it to map
        AddPointsToLayer();
    }
});

/* create map object */
var map = L.map('map', {
    center: [41.75, -74.98],
    zoom: 7,
    fullscreenControl: true,
    fullscreenControlOptions: {
        position: 'topleft'
    },
    layers: [osm, layer_apartments]
});

var baseLayers = {
    "OpenCycleMap": opencyclemap,
    "OpenStreetMap": osm
};

var overlays = {
    "Apartments in NYC": layer_apartments
};

L.control.layers(baseLayers, overlays).addTo(map);