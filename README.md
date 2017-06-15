# Logs Analysis Project

Analyzing the data of viewers on newspaper site.

## Getting Started

You will need VM and python 2.
[Virtual Machine](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)
You also need to download following library.

```
pip install psycopg2
```
You need to download [newsdata.psql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

When you download the newsdata.psql, then move the file into vagrant folder.
Using terminal go into vagrant folder and start vagrant.

```
cd ....../vagrant
vagrant up
vagrant ssh
cd /vagrant
```

Load the data and access the data.

```
psql -d news -f newsdata.sql
psql -d news
```

### View

In order to create view for how many views each articles have, you need following code:

```
create view popular_articles as
  select articles.title, count(*) as num
  from articles, log
  where concat('/article/',articles.slug) = log.path
  group by articles.title, articles.author
  order by num desc
  limit 3;
```

In order to create view for how many views each authors have, you need following code:

```
create view popular_authors as
  select authors.name, count(*) as num
  from articles, log, authors
  where articles.author = authors.id
  and concat('/article/',articles.slug) = log.path
  group by authors.name
  order by num desc;

```

In order to create view for how many requests lead to error, you need following code:

```
create view request_error as
  select total.time,
  round(error.error_num)/round(total.total_num)*100 as percent
  from
    (select date(time) as time,
    count(*) as total_num
    from log
    group by date(time)) total,
    (select date(time) as time,
    count(*) as error_num
    from log
    where status = '404 NOT FOUND'
    group by date(time)) error
  where total.time = error.time
  group by total.time, error.error_num, total.total_num
  having round(error.error_num)/round(total.total_num)*100  > 1
  order by percent desc;

```

### Run the code

After creating views, run the news.py in the terminal.

```
python news.py
```

## Answer

1. What are the most popular three articles of all time?

```
Candidate is jerk, alleges rival -- 338647
Bears love berries, alleges bear -- 253801
Bad things gone, say good people -- 170098
```

2. Who are the most popular article authors of all time?

```
Ursula La Multa -- 507594
Rudolf von Treppenwitz -- 423457
Anonymous Contributor -- 170098
Markoff Chaney -- 84557
```

3. On which days did more than 1% of requests lead to errors?

```
2016-07-17 -- 2.26
```
