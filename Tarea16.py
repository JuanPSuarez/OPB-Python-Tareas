import sqlite3

db_connection = sqlite3.connect('Tarea16.db')
sqlCursor = db_connection.cursor()

sqlCursor.execute("CREATE TABLE Alumnos(Id INTEGER PRIMARY KEY AUTOINCREMENT, NombreAlumno TEXT, ApellidoAlumno TEXT)")

sqlCursor.execute("INSERT INTO Alumnos VALUES(1,'Fulano', 'Sanchez')")
sqlCursor.execute("INSERT INTO Alumnos VALUES(2,'Mengano', 'Suarez')")
sqlCursor.execute("INSERT INTO Alumnos VALUES(3,'Soledad', 'Rodriguez')")
sqlCursor.execute("INSERT INTO Alumnos VALUES(4,'Matias', 'Rossa')")
sqlCursor.execute("INSERT INTO Alumnos VALUES(5,'Leo', 'Dicaprio')")
sqlCursor.execute("INSERT INTO Alumnos VALUES(6,'Angelina', 'Jolie')")
sqlCursor.execute("INSERT INTO Alumnos VALUES(7,'Quentin', 'Tarantino')")
sqlCursor.execute("INSERT INTO Alumnos VALUES(8,'Esteban', 'Quito')")

db_connection.commit()

sqlCursor.execute("SELECT * FROM Alumnos WHERE NombreAlumno = 'Leo'")

filas = sqlCursor.fetchall()

print(filas)

db_connection.close()