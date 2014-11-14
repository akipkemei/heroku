
SELECT AddGeometryColumn ('public','polls_location','the_geom',4326,'POINT',2);



UPDATE polls_message SET the_geom = GeomFromEWKT('SRID=4326;POINT(' || polls_message.longitude || ' ' || polls_message.latitude || ')');


update polls_message set the_geom = ST_GeogFromText('POINT(' || Latitude || ' ' ||Longitude || ')');

