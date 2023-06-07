import pandas as pd
import subprocess
import sqlite3
import streamlit as st
import time

def commit_to_git():
    subprocess.call(['git', 'add', '--all'])
    subprocess.call(['git', 'commit', '-m', 'Update data'])
    subprocess.call(['git', 'push', 'origin', 'main'])

if __name__ == '__main__' :
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # cursor.execute("""CREATE TABLE logs (
    #     cur_time text
    # );""")


    cursor.execute("insert into logs values (%s)"%str( round(time.time()) ) )

    conn.commit()


    st.write( cursor.execute("select * from logs").fetchall() )

    commit_to_git()
    st.write('Changes committed and pushed to GitHub.')


    conn.close()