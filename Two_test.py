import heapq
from collections import defaultdict



def build_huffman_tree_in_server(symbols_freq):

    heap = [[weight, [symbol, ""]] for symbol, weight in symbols_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return heap[0]


def generate_huffman_codes_in_server(tree):

    huff_codes = {}
    for pair in tree[1:]:
        symbol, code = pair
        huff_codes[symbol] = code
    return huff_codes


def compress_data(text, huff_codes):

    compressed_data = ""
    for char in text:
        compressed_data += huff_codes[char]
    return compressed_data



#Восстановление данных
def decompress_data_in_server(compressed_data, huff_codes, cliked, function):
    import sqlite3
    import random
    import string

    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        userid INT PRIMARY KEY,
        user_name TEXT,
        password TEXT 
    ) 
    """)
    con.commit()

    huff_codes_reverse= {code: symbol for symbol, code in huff_codes.items()}
    decoded_date = ""
    temp_coding = ""

    for bit in compressed_data:
        temp_coding += bit
        if temp_coding in huff_codes_reverse:
            decoded_date += huff_codes_reverse[temp_coding]
            temp_coding = ""


    finder = decoded_date.find('/')
    number_of_characters = len(decoded_date)
    password = decoded_date[finder+1:number_of_characters]
    user_name = decoded_date[0:finder]
    print(password)

    if cliked == 'entrance':
        if function == "username_checking":
            cur.execute("SELECT * FROM users WHERE user_name = ? AND password = ?", (user_name, password))
            result = cur.fetchone()
            print(result)
            if result:
                date_server = True

            else:
                date_server = False


        elif function == "new_users":
            cur.execute("SELECT * FROM users WHERE user_name = ?", (user_name,))
            result = cur.fetchone()
            print(result)
            if result:
                date_server = False

            else:
                print("Новый пользователь")
                if len(str(password)) >= 8:
                    user_record_list = [user_name, password]
                    cur.execute("INSERT INTO users VALUES (?, ?);", user_record_list)
                    con.commit()
                    date_server = True

                else:
                    date_server = False

        else:
            date_server = False



    else:
        date_server = False



    return date_server



def new_tests(user, new_test_name, new_password_test):
    import sqlite3

    con = sqlite3.connect('tests.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS tests(
            IDtests INT PRIMARY KEY,
            name_test TEXT,
            password_test TEXT,
            user_name TEXT
        ) 
        """)
    con.commit()
    a = '0'
    cur.execute("SELECT * FROM tests WHERE IDtests = ?", (a,))
    result = cur.fetchone()
    print(result)
    if result:
        check = True
    else:
        check = False
    while check == True:
        a = str(a)
        cur.execute("SELECT * FROM tests WHERE IDtests = ?", (a,))
        result = cur.fetchone()
        if result:
            a = int(a)
            a += 1
        else:
            break
    username = user
    test_name = str(new_test_name)
    test_password = str(new_password_test)
    id = a
    a = (id, test_name, test_password, username)
    

    con.commit()
    cur.execute("INSERT INTO tests VALUES(?, ?, ?, ?);", a)
    con.commit()

    return id


def adding_new_question(ID_test, rec_queschen, rec_answerre_1, rec_answerre_2, rec_answerre_3, correct_answer, question_numbers):
    
    import sqlite3

    con = sqlite3.connect('all_tests.db')
    cur = con.cursor()
    ID = int(ID_test)
    cur.execute("""CREATE TABLE IF NOT EXISTS all_tests(
            IDtests INT,
            question_numbers TEXT, 
            rec_queschen TEXT,
            rec_answerre_1 TEXT,
            rec_answerre_2 TEXT,
            rec_answerre_3 TEXT,
            correct_answer TEXT
        ) 
        """)
    new_test_record_list = [ID_test, question_numbers, rec_queschen, rec_answerre_1, rec_answerre_2, rec_answerre_3, correct_answer]
    cur.execute("INSERT INTO all_tests VALUES (?, ?, ?, ?, ?, ?, ?);", new_test_record_list)
    con.commit()
    print('')
    print(new_test_record_list)
    print('')
    print('adding a new question', ID_test, rec_queschen, rec_answerre_1, rec_answerre_2, rec_answerre_3, correct_answer, question_numbers)
    print('')



def take_test_aviable(take_test_ID):
    import sqlite3

    con = sqlite3.connect('tests.db')
    cur = con.cursor()
    test_ID = int(take_test_ID)
    
    print(test_ID)
    
    cur.execute("SELECT * FROM tests WHERE IDtests = ?", (test_ID,))
    result = cur.fetchone()
    con.commit()

    if result:
        return True
    
    else:
        return False
    
def conclusion_questions(take_test_ID, check_question_numbers):
    import sqlite3
    
    con = sqlite3.connect('all_tests.db')
    cur = con.cursor()
    
    query = f"SELECT * FROM all_tests WHERE IDtests = ? AND question_numbers = ?"
    cur.execute(query, (take_test_ID, check_question_numbers))
    
    data = cur.fetchall()
    print('')
    print(type(data))
    print('')
    print(data)
    print('')

    if data:

        data_list = data[0]
        '''for row in data:
            data_list.append(row)'''
        print(data_list)
        con.close()

        return data_list
    
    else:
        return 0
    


def record_col_cor_answere(right_answer, ID_test, user_name, check_question_numbers):
    #добавить общее количество вопросов в тесте!

    check_question_numbers -= 1
    import sqlite3

    con = sqlite3.connect('r_answ.db')
    cur = con.cursor()
    ID = int(ID_test)
    cur.execute("""CREATE TABLE IF NOT EXISTS r_answ(
            IDtests INT,
            usser_name TEXT,                        
            right_answer TEXT,
            col_question TEXT
        ) 
        """)
    new_test_record_list = [ID_test, user_name, right_answer, check_question_numbers]
    print(new_test_record_list)
    cur.execute("INSERT INTO r_answ VALUES(?, ?, ?, ? );", new_test_record_list)
    con.commit()



def check_res_tests_us(IDtests):
    import sqlite3
    connection = sqlite3.connect('r_answ.db')  # Здесь нужно указать путь к базе данных SQLite3
    cursor = connection.cursor()
    cursor.execute("SELECT usser_name, right_answer, col_question FROM r_answ WHERE IDtests = ?", (IDtests,))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results
