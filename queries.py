"""24 de Octubre del 2023/Base de Datos"""
import sqlite3

DB_NAME = "chinook.db"

con = sqlite3.connect(DB_NAME)
cursor = con.cursor()

# cursor.execute("INSERT INTO Locations(LocationName) VALUES ('7303')")
# cursor.execute("INSERT INTO Locations(LocationName) VALUES ('4302')")

cursor.execute(
    "SELECT Employeeid, Address, Email FROM employees WHERE HireDate BETWEEN '1992-06-01' AND '2008-12-15'")

cursor.execute(
    "SELECT LastName, Company FROM customers"
)

cursor.execute(
    "SELECT * FROM albums"
)

cursor.execute(
    """SELECT tracks.Composer, tracks.Name FROM tracks 
    INNER JOIN genres ON tracks.GenreId = genres.GenreId"""
)

cursor.execute("""
    SELECT playlists.Name, invoices.BillingAddress
    FROM playlists
    LEFT JOIN invoices ON 1=1

    UNION

    SELECT playlists.Name, invoices.BillingAddress
    FROM playlists
    RIGHT JOIN invoices ON 1=1
""")

cursor.execute("""
    SELECT playlists.*, invoices.*
    FROM playlists
    LEFT JOIN invoices ON 1=1

    UNION

    SELECT playlists.*, invoices.*
    FROM playlists
    RIGHT JOIN invoices ON 1=1
""")


rows = cursor.fetchall()

for r in rows:
    print(r)

cursor.close()
con.close()
