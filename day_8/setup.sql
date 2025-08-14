DROP TABLE IF EXISTS Order_Details;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Shippers;
DROP TABLE IF EXISTS Products;


CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY,
    CustomerName TEXT
);

CREATE TABLE Shippers (
    ShipperID INTEGER PRIMARY KEY,
    ShipperName TEXT
);

CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    ShipperID INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ShipperID) REFERENCES Shippers(ShipperID)
);

CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY,
    ProductName TEXT,  
    Price REAL
);

CREATE TABLE Order_Details (
    OrderDetailID INTEGER PRIMARY KEY,
    OrderID INTEGER,
    ProductID INTEGER,
    Quantity INTEGER,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO Customers VALUES
(1, 'Paul Henriot'),
(2, 'Tom''s Spezialitäten'),
(3, 'Hanari Carnes');

INSERT INTO Shippers VALUES
(1, 'Speedy Express'),
(2, 'United Package'),
(3, 'Federal Shipping');

INSERT INTO Orders VALUES
(10248, 1, 1),
(10249, 2, 2),
(10250, 3, 3);

INSERT INTO Products VALUES
(1, 'Chai', 18.00),
(2, 'Chang', 19.00),
(3, 'Aniseed Syrup', 10.00);

INSERT INTO Order_Details VALUES
(1, 10248, 1, 12), 
(2, 10249, 2, 10),
(3, 10250, 3, 5); 

SELECT 
    Orders.OrderID, 
    Customers.CustomerName, 
    Shippers.ShipperName,
    Order_Details.Quantity,
    Products.ProductName
FROM Orders
INNER JOIN Customers 
    ON Orders.CustomerID = Customers.CustomerID
INNER JOIN Shippers 
    ON Orders.ShipperID = Shippers.ShipperID
INNER JOIN Order_Details 
    ON Orders.OrderID = Order_Details.OrderID
INNER JOIN Products 
    ON Order_Details.ProductID = Products.ProductID;

