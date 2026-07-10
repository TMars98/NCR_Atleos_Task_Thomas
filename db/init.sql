CREATE TABLE service_requests (
    id INTEGER PRIMARY KEY,
    description TEXT NOT NULL,
    customer_name TEXT NOT NULL,
    customer_email TEXT NOT NULL,
    customer_phone TEXT
);

INSERT INTO service_requests (description, customer_name, customer_email, customer_phone) VALUES
('Replace failed compressor on production line 3', 'Acme Manufacturing', 'ops@acme.example', '+44 20 7946 0001'),
('Lift stuck between floors 2 and 3', 'Brightwell Estates', 'facilities@brightwell.example', '+44 161 496 0002'),
('Recalibrate loading bay weighbridge', 'Corvid Logistics', 'depot@corvid.example', '+44 141 496 0003');