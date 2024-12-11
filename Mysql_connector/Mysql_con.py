import mysql.connector

# mysql -> Is an pack 
# .connector -> is an class
# .connect -> is an method of .connector

# mydb is an instance/object

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Jayv@#12',
        database='college_data'
    )

    if connection.is_connected():
        print("Connected to MySQL server")

    cursor = connection.cursor()


    create_table_query = """ 
    CREATE TABLE IF NOT EXISTS students(
        id INT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        address VARCHAR(100),
        mask INT NOT NULL
    );
    """

    cursor.execute(create_table_query)
    print("Table `student` Created successfully...")

    insert_into_student = '''
        INSERT INTO student 
        (id, name, address, mask)
        VALUES
        (101, "Bob", "California", 78),
        (102, "J. haimer", "New york", 99),
        (103, "Leslie burke", "New york", 95),
        (104, "adam", "China", 75);
    '''

    cursor.execute(insert_into_student, students)
    print("Values are inserted into student table")
except mysql.connector.Error as err:
    print("Error: ", err)

finally:
    # Step 4: Close the cursor and connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySql connection closed")


