## Shopping website database

### Descroption

The goal for this project is to build a online shopping system. This is the database for our system.

This database is designed according to our [ER digram](https://github.com/derrl/CS425/blob/master/ER_Diagram.pdf)

It have 17 tables and more than 30 functions to make it robust.

### Tables
There are 17 tables to satified our system requirements.

You can see table creating detial in the file [cretab.sql](https://github.com/derrl/CS425/blob/master/sql_script/cretab.sql).

- ORDERDETAIL
- ADDRESS
- PAYMENTMETHOD
- VENDORS
- INVENTORY
- STORE
- BRANDBELONGTO
- BRAND
- PRODUCTBELONGTO
- CARTDETAIL
- CART
- PRODUCT_DESCRIPTION
- PRODUCT
- PRODUCT_TYPE
- ACCOUNT
- ORDERS
- CUSTOMERS

### Functions
I have created 19 User's functions and 13 Employee's functions using SQL queries. Here is the list.

You can see the queries detail in the file [functional_query.pdf](https://github.com/derrl/CS425/blob/master/sql_script/functional_query.pdf).

##### User's functions
- Sign in
- Sign up
- Edit information
- Add address
- Update address
- Delete address
- Add payment method
- Delete payment method
- Check order
- Check order detail
- Add to cart
- Add one in cart
- Minus one in cart
- Delete from cart
- Check cart
- Place order (checkout cart)
- Make payment order
- Cancel order
- Search product

##### Employee's functions
- Check product
- Add product
- Update product
- Delete product
- Check size from warehouse
- Check store
- Add store
- Update store information
- Delete store
- Add product type
- Delete product type
- Add brand
- Delete product brand
