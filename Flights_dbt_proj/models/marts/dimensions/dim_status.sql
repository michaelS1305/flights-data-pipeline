with statuses as(
    select
        status,
        arrival_departure,
        loaded_at
    from {{ ref('stg_flights') }}
    where status is not null
),

dedup as(
    select
     status,
     arrival_departure,
     row_number() over(partition by status order by loaded_at) as rn
    from statuses
)

select 
    {{ dbt_utils.generate_surrogate_key(['status']) }} as status_key,
    status,
    arrival_departure
from dedup
where rn =1