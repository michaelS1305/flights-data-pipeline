{% docs dimensions_overview %}

# Dimensions Layer

The Dimensions layer contains descriptive business entities used by the analytical data model.

These dimension tables provide contextual information that enriches the flight fact table and support analytical reporting through a star schema design.

## Included Dimensions

### dim_airlines
Contains unique airlines and their descriptive information.

**Grain:** One row per airline.

**Business Key:** airline_code

**Primary Key:** airline_key

---

### dim_airports
Contains unique destination airports and location details.

**Grain:** One row per airport.

**Business Key:** airport_code

**Primary Key:** airport_key

---

### dim_status
Contains unique flight statuses used to describe the operational state of a flight.

**Grain:** One row per status.

**Business Key:** status

**Primary Key:** status_key

---

## Purpose

The dimension tables are joined to the fact_flights table through surrogate keys to support scalable analytical queries and reporting.

This design follows a star schema architecture and serves as the Gold layer of the Medallion Architecture.

{% enddocs %}