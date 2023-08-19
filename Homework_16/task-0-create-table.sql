--
-- PostgreSQL database dump

-- Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--
CREATE TABLE guests (
    guest_id serial PRIMARY KEY,
    email character varying(30) NOT NULL,
    phone text NOT NULL,
    created_at date NOT NULL
);
--
-- Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--
CREATE TABLE rooms (
    room_id serial PRIMARY KEY,
    host_id int REFERENCES hosts(host_id) NOT NULL,
    address text NOT NULL,
    city_id int REFERENCES cities(city_id) NOT NULL,
    amount_of_residents int NOT NULL,
    room_type text NOT NULL,
    A_C bool NOT NULL,
    refrigerator bool NOT NULL,
    created_at date NOT NULL
);
--
-- Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--
CREATE TABLE booking (
    booking_id serial PRIMARY KEY,
    guest_id int REFERENCES guests(guest_id) NOT NULL,
    room_id int REFERENCES rooms(room_id) NOT NULL,
    start_day date NOT NULL,
    end_day date NOT NULL,
    price real NOT NULL,
    created_at date NOT NULL
);
--
-- Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--
CREATE TABLE hosts (
    host_id serial PRIMARY KEY,
    guest_id int REFERENCES guests(guest_id) NOT NULL
);
--
-- Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--
CREATE TABLE cities (
    city_id serial PRIMARY KEY,
    country_id int REFERENCES countries(country_id) NOT NULL,
    title text NOT NULL
);
--
-- Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--
CREATE TABLE countries (
    country_id serial PRIMARY KEY,
    title text NOT NULL
);
--
-- Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--
CREATE TABLE reviews (
    review_id serial PRIMARY KEY,
    guest_id int REFERENCES guests(guest_id) NOT NULL,
    body_review text NOT NULL
);