
with airports as(
    select
        airport_code,
        city_name,
        country_name,
        loaded_at
    from {{ ref('stg_flights') }}
    where airport_code is not null
),

dedup as(
    select
     airport_code,
     city_name,
     country_name,
     row_number() over(partition by airport_code order by loaded_at) as rn
    from airports
)


select
    {{ dbt_utils.generate_surrogate_key(['airport_code']) }} as airport_key,
    airport_code,
    city_name,
    country_name
from dedup
where rn = 1