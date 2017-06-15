#!/usr/bin/env python

import psycopg2


def access_database(table_name):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    query="select * from " + table_name
    c.execute(query)
    data = c.fetchall()
    db.close()
    return data

def result(views):
    num = 0
    for view in views:
        if view[1] == int(view[1]):
            print "%s -- %d" %(view[0], view[1])
        else:
            print "%s -- %0.2f" %(view[0], view[1])



print "1. What are the most popular three articles of all time?"
view_articles = access_database("popular_articles")
result(view_articles)
print "2. Who are the most popular article authors of all time?"
view_authors = access_database("popular_authors")
result(view_authors)
print "3. On which days did more than 1% of requests lead to errors?"
request_error_rate = access_database("request_error")
result(request_error_rate)
