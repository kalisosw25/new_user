import psycopg2
conn = psycopg2.connect(database="my_5ajx",
                        host="ccc.oregon-postgres.render.com",
                        user="my_5ajx_user",
                        password="VyKCoJgIgQtUKVWff8hb6RHOYUApNQYT",
                        port="5432")
mycursor = conn.cursor()

# -----------------------------------------------------CREATE TABLE beget_account-------------------------------------------------
# beget_account id username password gmail created_date service last_running_time phone_number
#                0  mac      mdalk    a@gm   05.11.2023  active  09.08 19:20       +7 9934043

# mycursor.execute("CREATE TABLE beget_account (id  SERIAL PRIMARY KEY , username VARCHAR(255), password VARCHAR(255), gmail VARCHAR(255),created_date VARCHAR(255), service VARCHAR(255) , last_running_time VARCHAR(255) , phone_number VARCHAR(255))")

# ----------------------------------------------------- see all table and columns-------------------------------------------------
# mycursor.execute("""select
#     t.table_name,
#     array_agg(c.column_name::text) as columns
# from
#     information_schema.tables t
# inner join information_schema.columns c on
#     t.table_name = c.table_name
# where
#     t.table_schema = 'public'
#     and t.table_type= 'BASE TABLE'
#     and c.table_schema = 'public'
# group by t.table_name""")
# for table in mycursor.fetchall():
#     print(table)

# -----------------------------------------Show all data-----------------------------------------------------------------------------------------
# mycursor.execute("SELECT * FROM beget_account")
# all = mycursor.fetchall()
# print(all)

# ------------------------------------------INSERT DATA---------------------------------------------------------------------------
# username=""
# password=""
# gmail=""
# created_date=""
# service=""
# last_running_time=""
# phone_number=""
# mycursor.execute(f"INSERT INTO beget_account (username,password,gmail,created_date,service,last_running_time,phone_number) VALUES ( '{username}', '{password}', '{gmail}', '{created_date}' , '{service}', '{last_running_time}', '{phone_number}')")

# ------------------------------------------UPDATE DATA---------------------------------------------------------------------------
# last_running_time = ""
# username = ""
# mycursor.execute(f"UPDATE beget_account SET  last_running_time = '{last_running_time}'  WHERE username ='{username}' ")


conn.commit()