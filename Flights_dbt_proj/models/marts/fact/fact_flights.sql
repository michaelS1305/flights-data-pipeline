with flights as (

    select *
    from {{ ref('stg_flights') }}

),

airlines as (

    select *
    from {{ ref('dim_airlines') }}

),

airports as (

    select *
    from {{ ref('dim_airports') }}

),

statuses as (

    select *
    from {{ ref('dim_status') }}

),

final as (

    select

        f.airline_code,
        f.flight_number,
        f.scheduled_time,
        f.arrival_departure,
        

        a.airline_key,
        ap.airport_key,
        s.status_key,

        f.actual_time,
        f.terminal,
        f.check_in_counter_range,
        f.check_in_zone,
        f.loaded_at

    from flights f

    left join airlines a
        on f.airline_code = a.airline_code

    left join airports ap
        on f.airport_code = ap.airport_code

    left join statuses s
        on f.status = s.status
       

)

select

    {{ dbt_utils.generate_surrogate_key([
        'airline_code',
        'flight_number',
        'scheduled_time',
        'arrival_departure'
    ]) }} as flight_key,

    *

from final