-- database: product.sqlite3
DROP TABLE orders;

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    order_date DATE,
    total_amount REAL,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

ALTER TABLE orders ADD COLUMN price INTEGER;
ALTER TABLE orders DROP COLUMN total_amount;

INSERT INTO orders (order_id, order_date, customer_id, price) 
VALUES (1, '2023-07-15', 1, 50), (2, '2023-07-16', 2, 75), (3, '2023-07-17', 3, 30);

SELECT orders.order_id, customers.name,orders.order_date, orders.price
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id;