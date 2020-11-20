
## Övning - vad skulle ni välja för datatyp


* om ni ska lagra ett telefonnummer
  - varchar

* förnamn
  - varchar

* ålder
  - int av något slag
  - datum är bättre

* vikt
  - float

* postnummer
  - varchar(10)


# Objectives of good design, part 1

* supports required and ad hoc information retrieval
* contains efficiently constructed 
  * each table describes only one subject
  * has relatively distinct fields
  * contains an absolute minimum amount of redundant data
  * identified by a field with unique values
* Imposes ...


# Objectives of good design, part 2

* Supports appropriate business rules
  * The data provides valid and accuraate information that is always meaningful to the business
* Lends itself to future growth
  * The database structure will be easy to modify or expand as the information requirements of the business change and grow


# Advantages of good design, part 1
* It is easy to modify and maintain the structure
  * Modifications made to a column or table will not adversely affect other columns or tables in the database
* It is easy to modify data
  * ...


# Normalisering
break up things to their core parts
  * First normal form (1NF)
  * Second normal form (2NF)
  * Third normal form (3NF)
  

# Normalisteringsregler
* Använd teori med förnuft
* ibland är det bra att inte normalisera.
* Men om du väljer en lägre normaliseringsgrad bör du ha goda skäl till det, och du bör vara medveten om vilka problem som kan uppstå. När du dokumenterar bör du sedan ange att du valt en lägre normaliseringsgrad, varför du gjorde det, och vilka problem du förutsett.



entitet + attribut

relationer
- entitet <-> entitet
- entity set <-> entity set
  
  cardinal relations
- one-to-one
- one-to-many
- many-to-many