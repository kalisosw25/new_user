import psycopg2
conn = psycopg2.connect(database="my_5ajx",
                        host="ccc.oregon-postgres.render.com",
                        user="my_5ajx_user",
                        password="VyKCoJgIgQtUKVWff8hb6RHOYUApNQYT",
                        port="5432")
mycursor = conn.cursor()

# -----------------------------------------------------CREATE TABLE google-------------------------------------------------
# ('google', ['first_name', 'last_name', 'phone', 'birthday_date', 'id', 'used_websites', 'username', 'password', 'created_date', 'status', 'shell_running', 'shell_status', 'next_quota_reset'])
# google id username password   created_date status shell_running shell_status next_quota_reset    first_name last_name phone birthday_date used_websites
#         0  maciso  aI*SMiX%J   15.11.2022  active 15.05 17:12   active        none                Aa         Bb       none   15.10.2000   beget,cc
#                                            blocked              end_limits    15.05 2023 17:12
#                                            pass_err
#                                            phone_need
# mycursor.execute("CREATE TABLE google (id  SERIAL PRIMARY KEY , username VARCHAR(255), password VARCHAR(255), created_date VARCHAR(255),status VARCHAR(255), shell_running VARCHAR(255) , shell_status VARCHAR(255) , next_quota_reset VARCHAR(255) , first_name  VARCHAR(255) , last_name  VARCHAR(255) ,phone  VARCHAR(255) ,birthday_date  VARCHAR(255) ,used_websites  VARCHAR(255))")

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

# ------------------------------------------INSERT DATA---------------------------------------------------------------------------
# without
# "boburbekbb1@gmail.com" , "boburbek098poi)",
# "boltayevboburbek1@gmail.com" , "boburbek098poi",

# gmail = [
# "boburbekdownload@gmail.com" , "boburbek098poi",
# "boburbektelegram@gmail.com" , "boburbek098poi",
# "boburbekspacial001@gmail.com" , "boburbek098poi",
# "boburbekspacial002@gmail.com" , "boburbek098poi",
# "ollohim.mendan.rozi.bol@gmail.com" , "boburbek777",
# "bombabobur@gmail.com" , "boburshoxx66S",
# "bombaakbar7@gmail.com" , "boburshoxx66S",
# "bombabobur4@gmail.com" , "boburshoxx66S",
# "boburbomba002@gmail.com" , "boburshoxx66S",
# "boburbomba001@gmail.com" , "boburshoxx66S",
# "boburbekbb2@gmail.com" , "boburbek098poi",
# "bbbother001@gmail.com" , "other123\\nb",
# "bbbother002@gmail.com" , "other123\\nb",
# "bbbother003@gmail.com" , "other123\\nb",
# "bbbother004@gmail.com" , "other123\\nb",
# "bbbother005@gmail.com" , "other123\\nb",
# "bbbother006@gmail.com" , "other123\\nb",
# "bbbother007@gmail.com" , "qsertg123@3e",
# "bbbother008@gmail.com" , "qsertg123@3e",
# "bbbother009@gmail.com" , "qsertg123@3e",
# "bbbother010@gmail.com" , "qsertg123@3e",
# "bbbother011@gmail.com" , "qsertg123@3e",
# "bbbother012@gmail.com" , "qsertg123@3e",
# "bbbother013@gmail.com" , "qsertg123@3e",
# "bbbother014@gmail.com" , "qsertg123@3e",
# "bbbother015@gmail.com" , "qsertg123@3e",
# "bbbother016@gmail.com" , "qsertg123@3e",
# "bbbother017@gmail.com" , "qsertg123@3e",
# "bbbother018@gmail.com" , "qsertg123@3e",
# "bbbother019@gmail.com" , "qsertg123@3e",
# "bbbother020@gmail.com" , "qsertg123@3e",
# "bbbother022@gmail.com" , "qsertg123@3e",
# "bbbother023@gmail.com" , "qsertg123@3e",
# "mira89c382@gmail.com"  , "KZuI!j[#N",
# "eira3045c3@gmail.com"  , "Obt[TT@&amp;5",
# "priya9bb9b@gmail.com"  , "ykn6xI3[!",
# "tomas62504@gmail.com"  , "tIctjQ77A",
# "vihaan6538@gmail.com"  , "6maN@A/dn",
# "jessie934b@gmail.com"  , "va&lt;@vmk}X",
# "brogana45c@gmail.com"  , "*kR(RQxQ/",
# ]
# sm = len(gmail)
# print(sm)
# for x in range(0,sm,2):
#   print(x) 
#   username=gmail[x]
#   password=gmail[x+1]
#   created_date="05.03.2023"
#   status="active"
#   shell_running=""
#   shell_status="active"
#   next_quota_reset="none"
#   first_name = ""
#   last_name = ""
#   phone = ""
#   birthday_date=""
#   used_websites=""
#   #   print(f"{username} , {password} , {created_date} , {status} , {shell_running} , {shell_status} , {next_quota_reset} , {first_name} , {last_name} , {phone} , {birthday_date} , {used_websites}")
#   mycursor.execute(f"INSERT INTO google (username , password , created_date , status , shell_running , shell_status , next_quota_reset , first_name , last_name , phone , birthday_date , used_websites) VALUES ( '{username}' , '{password}' , '{created_date}' , '{status}' , '{shell_running}' , '{shell_status}' , '{next_quota_reset}' , '{first_name}' , '{last_name}' , '{phone}' , '{birthday_date}' , '{used_websites}')")
#   # google id username password   created_date status shell_running shell_status next_quota_reset    first_name last_name phone birthday_date used_websites

# -----------------------------------------Show all data-----------------------------------------------------------------------------------------
mycursor.execute("SELECT * FROM google")
all = mycursor.fetchall()
print("-------------------------------------------------------------------------------")
print(all)

conn.commit()