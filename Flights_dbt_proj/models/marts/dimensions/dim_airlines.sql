with airlines as(

    select
     airline_code,
     airline_name,
     loaded_at
    from {{ ref('stg_flights') }}
    where airline_code is not null

),
dedup as(
    select
     airline_code,
     airline_name,
     row_number() over(partition by airline_code order by loaded_at) as rn
     from airlines
)

select 
    {{ dbt_utils.generate_surrogate_key(['airline_code']) }} as airline_key,
    airline_code,
    airline_name
from dedup
where rn = 1
