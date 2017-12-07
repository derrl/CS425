
## User's funciton

### Sign in

```sql
	--input username
	--input password

	select user_id from account
		where username = 'input_username' 
		and password = 'input_password';

--login use email
	select user_id from account
		where email = 'input_email' 
		and password = 'input_password';

```
	

### Sign up
```sql
	--auto generate auto_user_id;
	--input information;
	
	--examine the same username
	select username from account
		where username = 'input username';

	--if username is unique, then create a new account.
	insert into customers 
	values ('auto_user_id',
		'input_first_name',
		 'input_middle_name',
		'input_last_name',
		'phone_number' 
		);
```
	


### Edit information
```sql
	update table customers
	set first_name = 'input_first_name',
	    middle_name = 'input_middle_name',
	    last_name = 'input_last_name',
	    phone_number = 'input_phone_number',
	    date_of_birth = 'input_date_of_birth'
	where user_id = 'the current userid';
```
	

### Add address
```sql
	--auto generate auto_address_id;
	
	insert into address 
	values(	'auto_address_id',
		'address_line_1',
		'address_line_2',
		'city',
		'zipcode',
		'state',
		'current_user_id');
```
	
### Update address
```sql
	update address
	set address_line_1 = 'address_line_1',
	    address_line_2 = 'address_line_2',
		city = 'city',
		zipcode = 'zipcode',
		state = 'state'		 
	where address_id = 'current_address_id';
```

### Delete address

```sql
	delete from address
	where address_id = 'target_address_id';
```
	

### Set payment method
```sql
	--auto generate auto_payment_id;

	insert into paymentmethod
	values(	'method_id',
		'holdername',
		'card_number',
		'expiration_date',
		'svc',
		'user_id');
```

### Delete payment method 
```sql
	delete from paymentmethod
	where method_id = 'target_method_id';
```


### Check order
```sql
	select * from order 
	where user_id = 'the current userid';
```

### Check order detail
```sql
	select * form orderdetail
	where order_id = 'this order id';
```

### Add to cart
```sql
	insert into cartdetail 
	values ('the current userid',
		'target productid',
		'product_number');

	update cart
	set	shipping_price = 5,
		price = shipping_price + (select sum(product_price * product_number)
			from product natural join cartdetail
			where user_id = 'current_user_id'),
        tax = 0.05*(select sum(product_price * product_number)
            from product natural join cartdetail
            where user_id = 'current userid')
	where user_id = 'current_user_id';
```

### Add one in cart
```sql
	update cartdetail
	set product_number = product_number + 1
	where user_id = 'current_user_id' 
	and product_id = 'current_product_id';

	update cart
	set	shipping_price = 5,
		price = shipping_price + (select sum(product_price * product_number)
			from product natural join cartdetail
			where user_id = 'current_user_id'),
        tax = 0.05*(select sum(product_price * product_number)
            from product natural join cartdetail
            where user_id = 'current userid')
	where user_id = 'current_user_id';
```

### Minus one in cart
```sql
	update cartdetail
	set product_number = product_number - 1
	where user_id = 'current_user_id' 
	and product_id = 'current_product_id';

	update cart
	set	shipping_price = 5,
		price = shipping_price + (select sum(product_price * product_number)
			from product natural join cartdetail
			where user_id = 'current_user_id'),
        tax = 0.05*(select sum(product_price * product_number)
            from product natural join cartdetail
            where user_id = 'current userid')
	where user_id = 'current_user_id';
```

### Delete from cart
```sql
	delete from cartdetail
	where user_id = 'current_user_id'
	and product_id = 'product_id';

	update cart
	set	shipping_price = 5,
		price = shipping_price + (select sum(product_price * product_number)
			from product natural join cartdetail
			where user_id = 'current_user_id'),
        tax = 0.05*(select sum(product_price * product_number)
            from product natural join cartdetail
            where user_id = 'current userid')
	where user_id = 'current_user_id';
```

### Check cart
```sql
	--get current cartid
	select user_id from cart 
	where user_id = 'current userid';
	
	--get cart information
	select tax from cart 
	where user_id = 'current userid';
	
	select price from cart 
	where user_id = 'current userid';

	select shipping_price from cart 
	where user_id = 'current userid';

	--get product information
	select * from product natural join 
		(select product_id from cartdetail 
		where user_id = 'current userid');
```

### Place order (checkout cart)
```sql
	--auto generate auto_order_id;
    insert into orders
    values ('auto_order_id',
            current_date,
            (select price from cart
            where user_id = 'current userid'),
            'current userid',
            0);
  
    insert into orderdetail (order_id, product_id, product_number
    select 'auto_order_id', product_id, product_number
    from cartdetail
    where user_id = 'current_user_id';

    delete from cartdetail
    where user_id = 'current userid';

    update cart
    set shipping_price = 5,
        price = shipping_price + (select sum(product_price * product_number)
            from product natural join cartdetail
            where user_id = 'current userid'),
        tax = 0.05*(select sum(product_price * product_number)
            from product natural join cartdetail
            where user_id = 'current userid')
    where user_id = 'current userid';
```

### Make payment order
```sql
	update orders 
		set payment_status=1
		where order_id = 'current orderid';
```
	
### Cancel order
```sql
	delete from orderdetail
	where order_id = 'target_order_id';

	delete from orders
	where order_id = 'target_order_id';
```

### Search product
```sql
	select * from product
		where prodcut_name like '%key word%';
```


## Employee's function

### Check product
```sql
	select * from product;
```


### Add product
```sql
	insert into product
	values ('productid',
		'product_name',
		'product_price',
		'expiration_date',
		'upc_code');

	--set product store
	insert into inventory
	values ('store_id',
		'product_id',
		'number of product in this store');
	
	--set product description
	insert into product_description
	values ('product_id',
		'description')

	--set product type
	insert into productbelongto
	values ('product_id',
		'category_name');

	--set product brand 
	insert into brandbelongto
	values ('product_id',
		'barnd_name');
```

### Update product
```sql
	update product 
	set product_name = 'product name',
	    product_price = 'product price',
	    expiration_date = 'expiration date',
	    UPC_code = 'upc code'
	where product_id = 'target_product_id';
	
	update prodcut_description
	set description = 'product description'
	where product_id = 'target_product_id';
```
	
### Delete product
```sql
	delete from product 
	where product_id = 'productid';
```


### Check size from warehouse
```sql
	select product_name, product_number
	from inventory natural join product
	where store_id = 'target_store_id';
```
	
### Check store
```sql
	select * from store;
```

### Add store 
```sql
	--auto generate auto_store_id;
	insert into store 
	values ('auto_store_id',
		'store_name',
		'store_address',
		'phone_number',
		'open_time',
		'close_time',
		'description');

	--set vendors
	insert into vendors
	values ('store_id',
		'vendor_name');
```

### Update store information
```sql
	update store 
	set	store_name = 'store name',
		store_address = 'address',
		phone_number = 'phone number',
		open_time = 'open time',
		close_time = 'close time',
		description = 'store description'
	where store_id = 'current_storeid'
```

### Delete store
```sql
	delete from store
	where store_id = 'target_store_id';
```
	

### Add product type
```sql
	insert into product_type
	values ('category_name',
		'description');
```
	

### Delete product type
```sql
	delete from product_type
	where category_name = 'target_product_type';
```
	

### Add brand
```sql
	insert into brand
	values ('brand_name',
		'brand_descroption',
		'brand_company');
```
	

### Delete product brand
```sql
	delete from brand
	where brand_name = 'target_brand_name';
```
	
### Delete vendors
```sql
	delete from vendors
	where vendor_name = 'target_vendor_name';
```
	

