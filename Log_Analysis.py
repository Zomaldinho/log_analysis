#!/usr/bin/env python3

import psycopg2


def pop_art():
    conn = psycopg2.connect(database="news")
    c = conn.cursor()
    c.execute("select title, views from articles, hits \
              where articles.slug=hits.slug order by views desc limit 3; ")
    results = c.fetchall()
    print("** The Most Popular Three Articles of All Time:")
    for item in results:
        print ('- '+item[0]+" -- "+str(item[1])+" Views")
    conn.close()


def pop_aut():
    conn = psycopg2.connect(database="news")
    c = conn.cursor()
    c.execute("select auth_name.name, sum(hits.views) as views from auth_name,\
              hits where auth_name.slug=hits.slug group by auth_name.name \
              order by views desc; ")
    results = c.fetchall()
    print("** The Most Popular Article Authors of All Time:")
    for item in results:
        print('- '+item[0]+" -- "+str(item[1]))+" Views"
    conn.close()


def errors():
    conn = psycopg2.connect(database="news")
    c = conn.cursor()
    c.execute("select TO_CHAR(day, 'Mon DD, YYYY'), percentage from error_pcnt \
              where percentage>1; ")
    results = c.fetchall()
    print("** Days When More Than 1% of Requests Led to Errors:")
    for item in results:
        print("- "+str(item[0])+" -- "+str(item[1])+"% errors")
    conn.close()

pop_art()
pop_aut()
errors()
