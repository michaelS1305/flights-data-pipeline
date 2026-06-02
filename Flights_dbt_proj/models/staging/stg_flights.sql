with source_data as (

    select *
    from {{source ('bronze', 'flights_current')}}

),

renamed as (

    select

        trim(operator_code) as airline_code,
        flight_number,
        trim(operator_name) as airline_name,

        scheduled_time::timestamp as scheduled_time,
        actual_time::timestamp as actual_time,

        arrival_departure,

        trim(destination_airport_code) as airport_code,

        trim(destination_city_en) as city_name,
        trim(destination_country_en) as country_name,

        terminal::varchar as terminal,

        trim(checkin_counter) as check_in_counter_range,
        trim(checkin_zone) as check_in_zone,

        trim(status_en) as status,

        loaded_at::timestamp as loaded_at

    from source_data

),

final as (

    select
        *,
        row_number() over (
            partition by
                airline_code,
                flight_number,
                scheduled_time,
                arrival_departure
            order by
                actual_time desc nulls last,
                loaded_at desc
        ) as rn

    from renamed

)

select *
from final
where rn = 1