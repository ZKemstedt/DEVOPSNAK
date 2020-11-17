# Liten övning i grupp

### Finns det några uppenbara funktioner eller egeneskaper vi bör ta hänsyn till i uppbyggnaden av ett stort system ?

### Lite of företaget (år 2015)
* Deras huvudkontor finns i Sverige
* Första butiken öppnade i Västerås 1947
* Har nu över 4.500 butiker
* Finns i 62 länder
* De är nr 2 i värlen, bakom spanska Inditex


# Aspekter att ta hänsyn till

Region 
- Språk
  - Produktnamn
- Tidson

- Skatt
  - När ?
  - Hur mycket ?
- Valutor
- lokala skillnader i pris
- lokala skillnader i utbud

Tillgänglighet
  - latency

# Vår påbörjade skiss

## DB Global

- # Places
    - 

- # Customers
    (kund)
  - id 		        PRIMARY incr
  - firstname
  - middle name
  - surname
  - adress row 1
  - adress row 2
  - zip code        int
  - state*
  - country
  - region

- # Products
    (product)
  - product_id 			    PRIMARY incr
  - name 					"IKEA style"
  - cost 					production cost (= min price for profit)

- # Orders
    (order_head)
  - order_id 		PRIMARY incr
  - customer_id 			-> customer.id
  - order_date	    datetime[utc]

    (order_part)
  - part_id 		PRIMARY incr
  - order_id 				-> orders.order_id
  - product_id 			    -> products.product_id
  - product_count
  - transport_id			-> transports.transport_id

- # Transport
    (transport)

## DB Lokal
- Settings {
    languages   	[]		# i=0 is default
    time_format
    time_zone
    currencies  	[]		# i=0 is default
	
	tax_categories  {} 		# category(int):amount(float)
	tax_inclusive  	bool
}

- # Products
    (product)
  - global_id 	    PRIMARY -> Global.products.product_id
  - name 					-?> global.products.name
  - price           float
  - available		bool
  - stock 		    int

- # Employees
  - 

