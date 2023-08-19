-- Data for Name: guests; Type: TABLE DATA; Schema: public; Owner: -
INSERT INTO guests (email, phone, created_at) VALUES
    ('example1@example.com', '+1234567890', '2023-08-17'),
    ('example2@example.com', '+9876543210', '2023-08-18'),
    ('example3@example.com', '+5555555555', '2023-08-19');

-- Data for Name: hosts; Type: TABLE DATA; Schema: public; Owner: -
INSERT INTO hosts (guest_id) VALUES
    (1),
    (2),
    (3);

-- Data for Name: countries; Type: TABLE DATA; Schema: public; Owner: -
INSERT INTO countries (title) VALUES
    ('USA'),
    ('Canada'),
    ('UK');

-- Data for Name: cities; Type: TABLE DATA; Schema: public; Owner: -
INSERT INTO cities (country_id, title) VALUES
    (1, 'New York'),
    (2, 'Los Angeles'),
    (3, 'Chicago');

-- Data for Name: rooms; Type: TABLE DATA; Schema: public; Owner: -
INSERT INTO rooms VALUES
    (1, 1, '123 Main Street', 1, 2, 'Single', TRUE, TRUE, '2023-08-17'),
    (2, 2, '456 Elm Avenue', 2, 4, 'Double', TRUE, FALSE, '2023-08-18'),
    (3, 3, '789 Oak Road', 3, 3, 'Suite', TRUE, TRUE, '2023-08-19');

-- Data for Name: booking; Type: TABLE DATA; Schema: public; Owner: -
INSERT INTO booking (guest_id, room_id, start_day, end_day, price, created_at) VALUES
    (1, 2, '2023-08-20', '2023-08-25', 150.00, '2023-08-19'),
    (2, 3, '2023-09-01', '2023-09-10', 200.00, '2023-08-20'),
    (3, 1, '2023-08-22', '2023-08-29', 180.00, '2023-08-21');

-- Data for Name: reviews; Type: TABLE DATA; Schema: public; Owner: -
INSERT INTO reviews (guest_id, body_review) VALUES
    (1, 'Great experience!'),
    (2, 'Could be better.'),
    (3, 'Absolutely loved it.');



