import psycopg2


def access_database(table_name):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    query="select * from " + table_name
    c.execute(query)
    data = c.fetchall()
    db.close()
    return data

def three_most_popular(table):
    num = 0
    for list in table:
        if num < 3:
            print "%s -- %i" %(list[0], list[1])
            num += 1
        else:
            break

def find_request(table):
    for list in table:
        if list[3]> 1:
            print "%s -- %d" %(list[0], list[3])
        else:
            pass



print "1. What are the most popular three articles of all time?"
view_articles = access_database("popular_articles")
three_most_popular(view_articles)
print "2. Who are the most popular article authors of all time?"
view_authors = access_database("popular_authors")
three_most_popular(view_authors)
print "3. On which days did more than 1% of requests lead to errors?"
request_error_rate = access_database("request_error")
find_request(request_error_rate)
