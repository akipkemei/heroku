

UPDATE polls_location * SET the_geom = ST_SetSRID(ST_MakePoint(longitude, latitude), 4326);

select * from polls_message  where user_id  = 30

select * from polls_message  where latitude = 0.58713392377831


ALTER TABLE polls_message ADD COLUMN Longitude double precision;

ALTER TABLE polls_message ADD COLUMN Latitude double precision;

ALTER TABLE polls_message ADD COLUMN Accuracy double precision;

SELECT AddGeometryColumn ('public','polls_message','the_geom',4326,'POINT',2);

select * from polls_location  where longitude = 12.43

--------------------------------------------------------------------------------------------------------------------------------------------------



UPDATE polls_message SET the_geom = GeomFromEWKT('SRID=4326;POINT(' || polls_message.longitude || ' ' || polls_message.latitude || ')');


update polls_message set the_geom = ST_GeogFromText('POINT(' || Latitude || ' ' ||Longitude || ')');


UPDATE polls_message * SET latitude = Latitude

UPDATE polls_message * SET the_geom = ST_SetSRID(ST_MakePoint(longitude, latitude), 4326);

--------------------------------------------------------------------------------------------------------------------------------------------------
SELECT AddGeometryColumn ('public','poll_message','the_geom',4326,'POINT',2);

CREATE OR REPLACE FUNCTION geom_insert_trigger()
RETURNS TRIGGER AS $$
 
 BEGIN
 
    UPDATE poll_message * SET the_geom = ST_SetSRID(ST_MakePoint(longitude, latitude), 4326);

    RETURN NULL;
END;
$$
LANGUAGE plpgsql;
 
 ----------CALL INTO THE  TRIGGER IN THE TABLE 
 
 CREATE TRIGGER  geom_insert_trigger
    AFTER INSERT ON poll_message
    FOR EACH ROW EXECUTE PROCEDURE geom_insert_trigger();


  -----------------------------
  CREATE TRIGGER geom_uodatecollumn_trigger
    AFTER UPDATE ON poll_message
    FOR EACH ROW
    WHEN (OLD.* IS DISTINCT FROM NEW.*)
    EXECUTE PROCEDURE geom_insert_trigger();

--------------------------------------------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------------------------------------------
