SELECT Sale.SaleDate, SalesPerson.SalesPersonName, Customer.CustomerName, Sale.Amount
FROM Sale
LEFT JOIN SalesPerson ON Sale.SalesPersonID = SalesPerson.SalesPersonID
LEFT JOIN ON Customer on Sale.CustomerID = Customer.CustomerID
WHERE SalePerson.OfficeID = 1;