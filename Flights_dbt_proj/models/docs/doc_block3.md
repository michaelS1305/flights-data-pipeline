{% docs fact_flights %}

# Fact Flights

The fact_flights table contains one record per unique flight and serves as the central fact table in the Gold layer star schema.

## Grain

One row per unique flight identified by:

- airline_code
- flight_number
- scheduled_time
- arrival_departure

## Relationships

The table is linked to:

- dim_airlines
- dim_airports
- dim_status

through surrogate keys.

## Purpose

Supports analytical reporting and dashboarding on flight operations, airline activity, airport traffic, and flight status trends.

{% enddocs %}