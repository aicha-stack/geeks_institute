
CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    model VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    price NUMERIC(10,2) NOT NULL
);
INSERT INTO cars (model, year, price) VALUES
('Audi A4', 2022, 38000),
('Ford Mustang', 2021, 45000),
('Chevrolet Camaro', 2020, 42000),
('Nissan Altima', 2022, 25000),
('Kia Sportage', 2021, 27000),
('Hyundai Tucson', 2020, 26000),
('Volkswagen Golf', 2022, 30000),
('Mazda 3', 2021, 24000),
('Tesla Model 3', 2022, 50000),
('Porsche 911', 2021, 90000);

-- 
SELECT * FROM cars;
