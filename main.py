import pandas as pd
import subprocess
import sqlite3
import streamlit as st
import time

def commit_to_git():
    subprocess.call(['git' , 'config', '--global', 'user.email', ' shuhratabduqodirov5@gmail.com '])
    subprocess.call(['git', 'config', '--global', 'user.name', 'Shuhrat' ])

    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', 'Update data'])
    subprocess.call(['git', 'push'])

if __name__ == '__main__' :
#     conn = sqlite3.connect('data.db')
#     cursor = conn.cursor()

    # cursor.execute("""CREATE TABLE logs (
    #     cur_time text
    # );""") fdsafasdfsadfsdasdfsadfasfsfdsfsadf


    # cursor.execute("insert into logs values (%s)"%str( round(time.time()) ) )

    # conn.commit()


    # st.write( cursor.execute("select * from logs").fetchall() )

    
    if st.button('Update') == True :
        

        new = pd.DataFrame( data={
            'time':[time.time()]
            } )


        data = pd.read_csv('data.csv')


        data = pd.concat([data,new])

        data.to_csv('data.csv',index=False)


        st.write( data )


        commit_to_git()
        st.write('Changes committed and pushed to GitHub.')
