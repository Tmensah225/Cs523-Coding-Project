import psycopg2


print('Beginning')
con = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Mindgames123')

print(con)

con.set_isolation_level(3)
con.autocommit = False

try:
    cur = con.cursor()
    cur.execute("ALTER table stock DROP CONSTRAINT stock_depid_fkey")
    cur.execute("UPDATE depot SET addr='dd1' WHERE depid='d1'")
    cur.execute("UPDATE Stock SET depid = 'dd1' WHERE depid ='d1'")

except (Exception, psycopg2.DatabaseError) as err:
    print(err)
    print("Transaction could not be completed so database will be rolled back")
    con.rollback()

finally:
    if con:
        con.commit()
        cur.close
        con.close