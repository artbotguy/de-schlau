--
-- PostgreSQL database dump
--

-- Dumped from database version 13.20 (Debian 13.20-1.pgdg120+1)
-- Dumped by pg_dump version 13.20 (Debian 13.20-1.pgdg120+1)

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
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: myuser
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO myuser;

--
-- Name: word_pair; Type: TABLE; Schema: public; Owner: myuser
--

CREATE TABLE public.word_pair (
    id integer NOT NULL,
    word character varying(100) NOT NULL,
    translation character varying(100),
    created_at timestamp without time zone DEFAULT now(),
    examples text,
    cognitive_status character varying(100)
);


ALTER TABLE public.word_pair OWNER TO myuser;

--
-- Name: word_pair_id_seq; Type: SEQUENCE; Schema: public; Owner: myuser
--

CREATE SEQUENCE public.word_pair_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.word_pair_id_seq OWNER TO myuser;

--
-- Name: word_pair_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: myuser
--

ALTER SEQUENCE public.word_pair_id_seq OWNED BY public.word_pair.id;


--
-- Name: word_pair id; Type: DEFAULT; Schema: public; Owner: myuser
--

ALTER TABLE ONLY public.word_pair ALTER COLUMN id SET DEFAULT nextval('public.word_pair_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.alembic_version (version_num) FROM stdin;
bc3fbcdade95
\.


--
-- Data for Name: word_pair; Type: TABLE DATA; Schema: public; Owner: myuser
--

COPY public.word_pair (id, word, translation, created_at, examples, cognitive_status) FROM stdin;
1	das Auto	машина	2025-05-12 02:37:08.177374	\N	\N
2	das Wasser	вода	2025-05-29 23:07:24.995177	\N	\N
3	der Saft	сок	2025-05-29 23:28:03.003867	\N	new
4	die Wohnung	квартира	2025-05-29 23:28:26.07212	\N	new
5	das Zimmer	комната	2025-05-29 23:53:22.725002	\N	new
6	der Mann	мужчина	2025-05-30 00:17:21.212621	\N	new
7	die Banane	банан	2025-05-30 00:52:01.945518	\N	new
8	die Frage	вопрос	2025-05-30 00:53:59.951426		new
9	das Autoo	машина	2025-05-30 00:54:20.069253		new
\.


--
-- Name: word_pair_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myuser
--

SELECT pg_catalog.setval('public.word_pair_id_seq', 9, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: myuser
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: word_pair word_pair_pkey; Type: CONSTRAINT; Schema: public; Owner: myuser
--

ALTER TABLE ONLY public.word_pair
    ADD CONSTRAINT word_pair_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

