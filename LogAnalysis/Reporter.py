#!/usr/bin/env python3
#
# Assignment 1 for Reporting tool for news Database.

import psycopg2
from datetime import datetime

DBNAME = "news"


def get_top3():
    """Return top 3 articles from the 'database'."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query1 = ' '.join(["select distinct A.title,count(distinct L.id)",
                       "AS pop_cnt from log L ,articles A where A.slug",
                       "=rtrim(substr(L.path,10,100))",
                       "group by A.title order by pop_cnt desc limit 3"])

    c.execute(query1)
    return c.fetchall()
    db.close()


def get_popauth():
    """Returns sorted list of authors based on total views on articles"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query2 = ' '.join(["select distinct AU.name,count(distinct L.id)",
                       "AS pop_cnt from log L ,articles AR, authors ",
                       " AU where AR.slug=rtrim(substr(L.path,10,100))",
                       "and AU.id=AR.author group by AU.name",
                       "order by pop_cnt desc"])

    c.execute(query2)
    return c.fetchall()
    db.close()


def get_err():
    """Return error percent crossing 1 percent mark from logs"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query2 = ' '.join(["select CAST(time as DATE) as dt,",
                       "ROUND(((COUNT(case when status =",
                       "'404 NOT FOUND' then 1 end)::DECIMAL",
                       "/count(*)) * 100),2)  from  log group",
                       "by dt HAVING ((COUNT(case when",
                       "status = '404 NOT FOUND'then 1 end)",
                       "::DECIMAL/count(*)) * 100) > 1.00"])

    c.execute(query2)
    return c.fetchall()
    db.close()


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


print_log()
