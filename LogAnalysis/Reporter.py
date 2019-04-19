#!/usr/bin/env python3
#
# Assignment 1 for Reporting tool for news Database.

import psycopg2
from datetime import datetime

DBNAME = "news"


def execute_query(query):
    """execute sql queries """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def get_top3():
    """Return top 3 articles from the 'database'."""
    query1 = """
             SELECT A.title,count(*)
             AS pop_cnt FROM log L ,articles A WHERE '/article/' || A.slug
             = L.path GROUP BY A.title
             ORDER BY pop_cnt DESC LIMIT 3;
             """
    return execute_query(query1)


def get_popauth():
    """Returns sorted list of authors based on total views on articles"""
    query2 = """
             SELECT AU.name,count(*)
             AS pop_cnt FROM log L ,articles AR, authors
             AU WHERE AR.slug = rtrim(substr(L.path,10,100))
             AND AU.id = AR.author GROUP BY AU.name
             ORDER BY pop_cnt DESC;
             """
    return execute_query(query2)


def get_err():
    """Return error percent crossing 1 percent mark from logs"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query3 = """
             SELECT CAST(time as DATE) as dt,
             ROUND(((COUNT(case when status =
             '404 NOT FOUND' then 1 end)::DECIMAL
             /count(*)) * 100),2)  FROM  log group
             by dt HAVING ((COUNT(case when
             status = '404 NOT FOUND'then 1 end)
             ::DECIMAL/count(*)) * 100) > 1.00;
             """

    return execute_query(query3)


def print_view(view, POST):
    print('\n')
    START = '\033[92m'
    END = '\033[0m'
    if view == 'TOP3':
        label = "Top 3 Most Popular Articles by View"
        print(START + "%s" % label + END)
        for output in POST:
            print("  %s -- %d views" % output)

    if view == 'POPAUTH':
        label = "Popular Authors by View"
        print(START + "%s" % label + END)
        for output in POST:
            print("  %s -- %d total views" % output)

    if view == 'ERRPCT':
        label = "Days with more than 1% of requests lead to errors"
        print(START + "%s" % label + END)
        for output in POST:
            datef = datetime.strftime(output[0], '%b %d, %Y')
            print("  %s" % datef + " --" + " %0.2f %% errors" % output[1])


def print_log():
    START = '\033[94m'
    END = '\033[0m'
    print(START + "            Log Analysis Report      " + END)
    print(START + "--------------------------------------------------" + END)
    print_view('TOP3', get_top3())
    print_view('POPAUTH', get_popauth())
    print_view('ERRPCT', get_err())
    print('\n')
    print(START + "----------------End of Report---------------------" + END)


if __name__ == '__main__':
    print_log()
