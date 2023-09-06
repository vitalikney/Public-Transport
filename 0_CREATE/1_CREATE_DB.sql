BEGIN;

DROP TABLE IF EXISTS public.types CASCADE;
CREATE TABLE IF NOT EXISTS public.types
(
  type_id serial NOT NULL,
  type_name text NOT NULL,
  PRIMARY KEY (type_id)
);

DROP TABLE IF EXISTS public.transports CASCADE;
CREATE TABLE IF NOT EXISTS public.transports
(
 transport_id serial NOT NULL,
 transport_type_id serial NOT NULL,
 transport_number text NOT NULL,
 PRIMARY KEY (transport_id)
);

DROP TABLE IF EXISTS public.stops CASCADE;
CREATE TABLE IF NOT EXISTS public.stops
(
 stop_id serial NOT NULL,
 stop_type_id serial NOT NULL,
 stop_name text NOT NULL,
 PRIMARY KEY (stop_id)
);

DROP TABLE IF EXISTS public.stop_transports CASCADE;
CREATE TABLE IF NOT EXISTS public.stop_transports
(
 stop_transport_id serial NOT NULL,
 stop_id serial NOT NULL,
 transport_id serial NOT NULL,
 PRIMARY KEY (stop_transport_id)
);

DROP TABLE IF EXISTS public.communications CASCADE;
CREATE TABLE IF NOT EXISTS public.communications
(
 communication_id serial NOT NULL,
 first_stop_id serial NOT NULL,
 second_stop_id serial NOT NULL,
 tyme_interval serial NOT NULL,
 PRIMARY KEY (communication_id)
);

DROP TABLE IF EXISTS public.routes CASCADE;
CREATE TABLE IF NOT EXISTS public.routes
(
 route_id serial NOT NULL,
 communication_id serial NOT NULL,
 route_part serial NOT NULL,
 start_stop text NOT NULL,
 next_stop text NOT NULL,
 finish_stop text NOT NULL,
 PRIMARY KEY (route_id)
);

DROP TABLE IF EXISTS public.timetables CASCADE;
CREATE TABLE IF NOT EXISTS public.timetables
(
 timetable_id serial NOT NULL,
 stop_transport_id serial NOT NULL,
 times text NOT NULL,
 PRIMARY KEY (timetable_id)
);

ALTER TABLE IF EXISTS public.transports
  ADD CONSTRAINT transport_type_id FOREIGN KEY (transport_type_id)
  REFERENCES public.types (type_id) MATCH SIMPLE
  ON UPDATE NO ACTION
  ON DELETE NO ACTION
  NOT VALID;  
  
ALTER TABLE IF EXISTS public.stops
  ADD CONSTRAINT stop_type_id FOREIGN KEY (stop_type_id)
  REFERENCES public.types (type_id) MATCH SIMPLE
  ON UPDATE NO ACTION
  ON DELETE NO ACTION
  NOT VALID; 

ALTER TABLE IF EXISTS public.stop_transports
  ADD CONSTRAINT stop_id FOREIGN KEY (stop_id)
  REFERENCES public.stops (stop_id) MATCH SIMPLE
  ON UPDATE NO ACTION
  ON DELETE NO ACTION
  NOT VALID;
  
ALTER TABLE IF EXISTS public.stop_transports
  ADD CONSTRAINT transport_id FOREIGN KEY (transport_id)
  REFERENCES public.transports (transport_id) MATCH SIMPLE
  ON UPDATE NO ACTION
  ON DELETE NO ACTION
  NOT VALID; 

ALTER TABLE IF EXISTS public.communications
  ADD CONSTRAINT first_stop_id FOREIGN KEY (first_stop_id)
  REFERENCES public.stops (stop_id) MATCH SIMPLE
  ON UPDATE NO ACTION
  ON DELETE NO ACTION
  NOT VALID; 

ALTER TABLE IF EXISTS public.communications
  ADD CONSTRAINT second_stop_id FOREIGN KEY (second_stop_id)
  REFERENCES public.stops (stop_id) MATCH SIMPLE
  ON UPDATE NO ACTION
  ON DELETE NO ACTION
  NOT VALID;

ALTER TABLE IF EXISTS public.routes
  ADD CONSTRAINT communication_id FOREIGN KEY (communication_id)
  REFERENCES public.communications (communication_id) MATCH SIMPLE
  ON UPDATE NO ACTION
  ON DELETE NO ACTION
  NOT VALID;

ALTER TABLE IF EXISTS public.timetables
  ADD CONSTRAINT stop_transport_id FOREIGN KEY (stop_transport_id)
  REFERENCES public.stop_transports (stop_transport_id) MATCH SIMPLE
  ON UPDATE NO ACTION
  ON DELETE NO ACTION
  NOT VALID;

END;