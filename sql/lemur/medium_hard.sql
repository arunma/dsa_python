--https://datalemur.com/questions/sql-third-transaction
with ordered_tx_cte as (
    select
        user_id,
        spend,
        transaction_date,
        dense_rank() over (partition by user_id order by transaction_date asc) rnk
    from
        transactions
)
select
    user_id,
    spend,
    transaction_date
from
    ordered_tx_cte
where
    rnk=3


create index user_id_idx on activities (user_id)
create index age_break_id_idx on age_breakdown (user_id)
create index activity_type_idx on activities (activity_type)

--https://datalemur.com/questions/time-spent-snaps
explain with summ_cte as (
    select
        b.age_bucket,
        sum(case when activity_type='send' then time_spent else 0 end) as send_time,
        sum(case when activity_type='open' then time_spent else 0 end) as open_time,
        sum(time_spent) as total_time
    from
        activities a
    join
        age_breakdown b
    on a.user_id=b.user_id
    where a.activity_type in ('send', 'open')
    group by
        age_bucket
)
select
    age_bucket,
    round((send_time*100)::numeric/total_time::numeric,2) as send_perc,
    round((open_time*100)::numeric/total_time::numeric,2) as open_perc
from
    summ_cte
order by age_bucket


--https://datalemur.com/questions/rolling-average-tweets
select
    user_id,
    tweet_date,
    round(avg(tweet_count) over (partition by user_id rows between 2 preceding and current row), 2) rolling_avg_3d
from
    tweets
order by user_id


--https://datalemur.com/questions/sql-highest-grossing

with ranked_cte as (
  SELECT
    category,
    product,
    sum(spend) as total_spend,
    dense_rank() over (partition by category order by sum(spend) desc) rnk
  FROM
    product_spend
  where EXTRACT(YEAR from transaction_date)='2022'
  GROUP BY
    category, product
)
select
  category,
  product,
  total_spend
FROM
  ranked_cte
where rnk<=2


--https://datalemur.com/questions/top-fans-rank
with artist_rank_cte as (
    select
        a.artist_name,
        count(g.rank) rank_freq
    from
        artists a
    join
        songs s
    on
        a.artist_id=s.artist_id
    join
        global_song_rank g
    on
        g.song_id=s.song_id
    where
        g.rank<=10
    group by artist_name
),
artist_ranking_cte as (
    select
        artist_name,
        dense_rank() over (order by rank_freq desc) artist_rank
    from
        artist_rank_cte
)
select
    artist_name,
    artist_rank
from
    artist_ranking_cte
where
    artist_rank<=5


--https://datalemur.com/questions/signup-confirmation-rate


with calc_cte as (
    select
        sum(case when signup_action='Confirmed' then 1 else 0 end) num_confirmed,
        count(text_id) total_confirmations
    from
        emails e
    join
        texts t
    on
        e.email_id=t.email_id
)

select
    round(num_confirmed::numeric/total_confirmations, 2) as confirm_rate
from
    calc_cte



--https://datalemur.com/questions/supercloud-customer

with product_category_count_cte as(
    select
        count(distinct(product_category)) product_cat_count
    from
        products
),
customer_cat_count_cte as(
    select
        c.customer_id,
        count(distinct(p.product_category)) as total_categories
    from
        customer_contracts c
    left join
        products p
    on c.product_id=p.product_id
    group by
        c.customer_id

)
select
    customer_id
from
    customer_cat_count_cte
join
    product_category_count_cte p
on
    total_categories=p.product_cat_count




--https://datalemur.com/questions/odd-even-measurements

with ordered_cte as (
    select
        measurement_id,
        measurement_value,
        date(measurement_time) measurement_day,
        row_number() over (partition by date(measurement_time) order by measurement_time) rownum
    from
        measurements
)
select
    measurement_day,
    sum(case when mod(rownum, 2)!=0 then measurement_value else 0 end) odd_sum,
    sum(case when mod(rownum, 2)=0 then measurement_value else 0 end) even_sum
from
    ordered_cte
group by
    1


--https://datalemur.com/questions/histogram-users-purchases

with user_order_cte as (
    select
        user_id,
        transaction_date,
        product_id,
        dense_rank() over (partition by user_id order by transaction_date desc) txrank
    from
        user_transactions
)
select
   transaction_date,
   user_id,
   count(product_id) as product_count
from
    user_order_cte
where txrank=1
group by transaction_date, user_id
order by transaction_date




--https://datalemur.com/questions/alibaba-compressed-mode

with max_order_cte as (
    select
        max(order_occurrences) as max_occurrences
    from
        items_per_order
)
select
    item_count as mode
from
    items_per_order o
join
    max_order_cte
on
    o.order_occurrences=max_occurrences
order by 1



select
  item_count
from
  items_per_order
where
  order_occurrences = (select max(order_occurrences) from items_per_order)
order by item_count;



--https://datalemur.com/questions/card-launch-success


with ordered_cards_cte as (
    select
        card_name,
        issue_month,
        issue_year,
        issued_amount,
        rank() over (partition by card_name order by issue_year, issue_month) rnk
    from
        monthly_cards_issued
)
select
    card_name,
    issued_amount
from
    ordered_cards_cte
where
    rnk=1
order by
    issued_amount desc



--https://datalemur.com/questions/international-call-percentage

with enriched_cte as (
    select
        p1.country_id as caller_country,
        p2.country_id as receiver_country
    from
        phone_calls c
    join
        phone_info p1
    on
        p1.caller_id=c.caller_id
    join
        phone_info p2
    on
        p2.caller_id=c.receiver_id
),
counts_cte as (
    select
        sum(case when caller_country!=receiver_country then 1 else 0 end) as international,
        count(caller_country) as all_calls
    from
        enriched_cte
)
select
    round((international*100)::numeric/all_calls, 1) as international_calls_pct
from
    counts_cte



SELECT
    ROUND(SUM(item_count * order_occurrences)::numeric / SUM(order_occurrences)::numeric, 1) AS mean
FROM items_per_order;


--https://datalemur.com/questions/non-profitable-drugs

select
    *,
    cogs-total_sales
from pharmacy_sales

SELECT
    manufacturer,
    COUNT(drug) AS drug_count,
    SUM(cogs - total_sales) AS total_loss
FROM pharmacy_sales
where cogs-total_sales>0
GROUP BY manufacturer
ORDER BY total_loss DESC


--https://datalemur.com/questions/user-retention

with action_counts_cte as (
    select
        user_id,
        extract(month from event_date) as "month",
        extract(year from event_date) as "year",
        sum(count(*)) over (partition by user_id, extract(month from event_date), extract(year from event_date)) action_count
    from
        user_actions
    group by 1,2,3
    order by 1,3,2
),
lag_cte as (
    select
        user_id,
        action_count,
        month,
        year,
        lag(action_count) over (partition by user_id order by year, month),
        lag(month) over (partition by user_id order by year, month) lag_month,
        lag(year) over (partition by user_id order by year, month) lag_year

    from
        action_counts_cte
)
select
      month,
      count(user_id) as monthly_active_users
from
    lag_cte
where
    lag!=0
and
    month-lag_month=1
and
    lag_year=year
group by month


with monthly_cte as (
    select
        user_id,
        sum(case when extract(month from event_date)=6 and extract(year from event_date)=2022 then 1 else 0 end) as june,
        sum(case when extract(month from event_date)=7 and extract(year from event_date)=2022 then 1 else 0 end) as july
    from
        user_actions
    group by
        user_id

)
select
    '7' as month,
    count(*) as monthly_active_users
from
    monthly_cte
where
    june>0 and july>0



--https://datalemur.com/questions/yoy-growth-rate
with yoy_cte as (
    select
        extract(year from transaction_date) as "year",
        product_id,
        sum(spend) curr_year_spend
    from
        user_transactions
    group by 1,2
),
yoy_spend as (
    select
        year,
        product_id,
        curr_year_spend,
        lag(curr_year_spend) over (partition by product_id order by year) as prev_year_spend
    from
        yoy_cte
)
select
    year,
    product_id,
    curr_year_spend,
    prev_year_spend,
    round((curr_year_spend-prev_year_spend)*100/prev_year_spend, 2) as yoy_rate
from
    yoy_spend


-- https://datalemur.com/questions/updated-status

with status_cte as (
    select
        coalesce(a.user_id, p.user_id) as user_id,
        status as old_status,
        p.paid,
        (case
            when paid is null then 'CHURN'
            when paid is not null and status='CHURN' then 'RESURRECT'
            when paid is not null and status is null then 'NEW'
            else 'EXISTING'
         end) as new_status
    from
        advertiser a
    full outer join
        daily_pay p
    on
        a.user_id=p.user_id
)
select
    user_id,
    new_status
from status_cte
order by user_id, new_status



--https://datalemur.com/questions/pizzas-topping-cost

select
    p1.topping_name,
    p2.topping_name,
    p3.topping_name,
    p1.ingredient_cost,
    p2.ingredient_cost,
    p3.ingredient_cost
from
    pizza_toppings p1
join
    pizza_toppings p2
on
    p1.topping_name<p2.topping_name
join
    pizza_toppings p3
on
    p2.topping_name<p3.topping_name


select
    concat(p1.topping_name,',',p2.topping_name,',', p3.topping_name) pizza,
    p1.ingredient_cost + p2.ingredient_cost + p3.ingredient_cost as total_cost
from
    pizza_toppings p1
join
    pizza_toppings p2
on
    p1.topping_name<p2.topping_name
join
    pizza_toppings p3
on
    p2.topping_name<p3.topping_name
order by total_cost desc, pizza asc


--https://datalemur.com/questions/repeated-payments

with transaction_cte as (
    select
        transaction_id,
        amount,
        transaction_timestamp,
        extract(epoch from transaction_timestamp - lag(transaction_timestamp) over (partition by amount order by transaction_timestamp))/60 as difference
    from
        transactions
)
select
    count(*) as payment_count
from
    transaction_cte
where
    difference<=10





