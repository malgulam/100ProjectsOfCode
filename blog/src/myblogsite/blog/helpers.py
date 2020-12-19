#!/usr/bin/python3

#helpers.py

import sqlite3

def retrieve_blog_content():
    conn = None
    try:
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute(f'''SELECT * FROM blog''')
        blog_contents = list(c.fetchall())
        print('RETRIEVED LATEST BLOG POSTS!')
        conn.close()
        return blog_contents
    except sqlite3.OperationalError as e:
        print(e)