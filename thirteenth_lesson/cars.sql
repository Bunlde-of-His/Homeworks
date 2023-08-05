--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: car_owners; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.car_owners (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    age integer NOT NULL,
    contact_number character varying(20) NOT NULL
);


ALTER TABLE public.car_owners OWNER TO postgres;

--
-- Name: car_owners_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.car_owners_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.car_owners_id_seq OWNER TO postgres;

--
-- Name: car_owners_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.car_owners_id_seq OWNED BY public.car_owners.id;


--
-- Name: cars; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cars (
    car_id integer NOT NULL,
    manufacturer character varying(100),
    model character varying(100),
    color character varying(50),
    owner_id integer
);


ALTER TABLE public.cars OWNER TO postgres;

--
-- Name: cars_car_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cars_car_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cars_car_id_seq OWNER TO postgres;

--
-- Name: cars_car_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cars_car_id_seq OWNED BY public.cars.car_id;


--
-- Name: car_owners id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.car_owners ALTER COLUMN id SET DEFAULT nextval('public.car_owners_id_seq'::regclass);


--
-- Name: cars car_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cars ALTER COLUMN car_id SET DEFAULT nextval('public.cars_car_id_seq'::regclass);


--
-- Data for Name: car_owners; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.car_owners (id, name, age, contact_number) FROM stdin;
1	Jhon Doe	35	1234567890
2	Jane Smith	28	9876543210
3	Mike Jhonson	42	5555555555
4	Jack Black	39	346373465
5	Suzen Q	33	453536347
\.


--
-- Data for Name: cars; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cars (car_id, manufacturer, model, color, owner_id) FROM stdin;
1	Toyota	Camry	Red	1
2	Honda	Civic	Blue	2
3	Ford	Mustang	Yellow	3
4	Chevrolet	Cruze	Silver	4
5	Nissan	\N	Purple	5
6	\N	Logan	\N	6
\.


--
-- Name: car_owners_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.car_owners_id_seq', 9, true);


--
-- Name: cars_car_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cars_car_id_seq', 6, true);


--
-- Name: car_owners car_owners_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.car_owners
    ADD CONSTRAINT car_owners_pkey PRIMARY KEY (id);


--
-- Name: cars cars_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cars
    ADD CONSTRAINT cars_pkey PRIMARY KEY (car_id);


--
-- PostgreSQL database dump complete
--

