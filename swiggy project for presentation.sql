use food_online;
show tables;

describe swiggy;

#set ID column as a primary key
alter table swiggy
add primary key(ID);

#find total rows in dataset;
select count(*) from swiggy;

# find total number of unique restaurants in dataset
select count(distinct(Restaurant))
from swiggy;
select count(distinct(City))
from swiggy;

#find total restaurant in each city
select city, count(restaurant) as total_hotels
from swiggy
group by city
order by total_hotels desc;

select city, count(restaurant) as total_hotels
from swiggy
group by city
having total_hotels >= 1000
order by total_hotels desc;

# find the restaurant from hyderabad which serves fast food or chinese or mughalai or indian food
select  restaurant, food_type
from swiggy
where city = "Hyderabad" and
Food_type in ('fast food','chinese','mughalai','indian');

# list top 3 restaurant having maximum number or orders
select restaurant, count(ID) as no_of_order
from swiggy
group by Restaurant
order by no_of_order desc limit 3;

select restaurant,count(ID) as orders,
dense_rank() over (order by count(ID) desc) as rankk
from swiggy
group by restaurant
limit 3;

#find avg dilevary time
select avg(Delivery_time) from swiggy;

# find the restauran from delhi who serves fast food or chinese or both whose rating is more than 3.5*
select  Restaurant , food_type
from swiggy
where city = "Delhi"
and Food_type in ("fast food" , "chinese")
and Total_ratings > 3.5;

# find restaurant in banglore and display them area wise
select restaurant from swiggy
where city = "Benlore"
group by Area;


# find the avg price of restaurant from powai area from mumbai
select avg(Price)from swiggy 
where city = "Mumbai" And  Area = "Powai";
 
select avg(Delivery_time) from swiggy
where city = "Mumbai" and Area = "Powai";





