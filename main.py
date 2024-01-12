import heapq
from collections import defaultdict
import Two_test
import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3
import random
import string
import os
import sys




global question_number
question_numbers = 0

transition = '0'

#построения дерева Хаффмана
def build_huffman_tree(symbols_freq):
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


#Генерация кодов Хаффмана
def generate_huffman_codes(tree):
    huff_codes = {}
    for pair in tree[1:]:
        symbol, code = pair
        huff_codes[symbol] = code
    print(huff_codes)
    return huff_codes


#Сжатие данных с использованием кодов Хаффмана
def compress_data(text, huff_codes):
    compressed_data = ""
    for char in text:
        compressed_data += huff_codes[char]
    return compressed_data


#Восстановление данных
def decompress_data(decompress_data, huff_codes):
    huff_codes_reversed = {code: symbol for symbol, code in huff_codes.items()}
    decoded_data = ""
    temp_code = ""

    for bit in compressed_data:
        temp_code += bit
        if temp_code in huff_codes_reversed:
            decoded_data += huff_codes_reversed[temp_code]
            temp_code = ""

    return decoded_data





con = sqlite3.connect('users.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
    user_name TEXT,
    password TEXT 
) 
""")
con.commit()



def restart_program():
    print('Restarting script...')

    os.execv(sys.executable, ['python'] + sys.argv)



def new_test():
    global question_numbers
    global ID_test
    
    def correct_answer_1():
        global question_numbers
        question_numbers += 1

        correct_answer = 1

        ID_test = test_number
        rec_queschen = str()
        rec_answerre_1 = str()
        rec_answerre_2 = str()
        rec_answerre_3 = str()

        rec_queschen = queschen_entry.get()
        rec_answerre_1 = answer_entry_1.get()
        rec_answerre_2 = answer_entry_2.get()
        rec_answerre_3 = answer_entry_3.get()

        queschen_entry.delete(0, 'end')
        answer_entry_1.delete(0, 'end')
        answer_entry_2.delete(0, 'end')
        answer_entry_3.delete(0, 'end')

        print('correct_answer_1')

        Two_test.adding_new_question(ID_test, rec_queschen, rec_answerre_1, rec_answerre_2, rec_answerre_3, correct_answer, question_numbers)
        
    def correct_answer_2():
        global question_numbers
        question_numbers += 1

        correct_answer = 2

        ID_test = test_number
        rec_queschen = str()
        rec_answerre_1 = str()
        rec_answerre_2 = str()
        rec_answerre_3 = str()

        rec_queschen = queschen_entry.get()
        rec_answerre_1 = answer_entry_1.get()
        rec_answerre_2 = answer_entry_2.get()
        rec_answerre_3 = answer_entry_3.get()

        queschen_entry.delete(0, 'end')
        answer_entry_1.delete(0, 'end')
        answer_entry_2.delete(0, 'end')
        answer_entry_3.delete(0, 'end')

        print('correct_answer_2')

        Two_test.adding_new_question(ID_test, rec_queschen, rec_answerre_1, rec_answerre_2, rec_answerre_3, correct_answer, question_numbers)

    def correct_answer_3():

        global question_numbers
        question_numbers += 1

        

        correct_answer = 3

        ID_test = test_number
        rec_queschen = str()
        rec_answerre_1 = str()
        rec_answerre_2 = str()
        rec_answerre_3 = str()

        rec_queschen = queschen_entry.get()
        rec_answerre_1 = answer_entry_1.get()
        rec_answerre_2 = answer_entry_2.get()
        rec_answerre_3 = answer_entry_3.get()

        queschen_entry.delete(0, 'end')
        answer_entry_1.delete(0, 'end')
        answer_entry_2.delete(0, 'end')
        answer_entry_3.delete(0, 'end')

        print('correct_answer_3')

        Two_test.adding_new_question(ID_test, rec_queschen, rec_answerre_1, rec_answerre_2, rec_answerre_3, correct_answer, question_numbers)

    def exit_for_test():
        global contin
        contin.destroy()
        main_window()


    


    def continue_new_test(ID_test):
        global test_number
        test_number = ID_test
        global contin
        global queschen_entry, answer_entry_1, answer_entry_2, answer_entry_3
        
        win.destroy()
        contin = Tk()
        contin.title('Авторизация')
        # размер окна
        contin.geometry('900x600')
        # можно ли изменять размер окна - нет
        contin.resizable(False, False)

        # кортежи и словари, содержащие настройки шрифтов и отступов
        font_header = ('Arial', 15)
        font_entry = ('Arial', 12)
        label_font = ('Arial', 11)
        base_padding = {'padx': 10, 'pady': 8}
        header_padding = {'padx': 10, 'pady': 12}

        # заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
        # для всех остальных виджетов настройки делаются также
        main_label = Label(contin, text='Новый вопрос/ответ', font=font_header, justify=CENTER, **header_padding)
        # помещаем виджет в окно по принципу один виджет под другим
        main_label.pack()

        # метка для поля ввода имени
        queschen_label = Label(contin, text='Вопрос:', font=label_font, **base_padding)
        queschen_label.pack(ipady=10)

        queschen_entry = Entry(contin, bg='#fff', fg='#444', font=font_entry)
        queschen_entry.pack(fill=X, ipady=10)

        answer_label_1 = Label(contin, text='Ответ 1', font=label_font, **base_padding)
        answer_label_1.pack(ipady=10)


        answer_entry_1 = Entry(contin, bg='#fff', fg='#444', font=font_entry)
        answer_entry_1.pack(fill=X, ipady=10)

        answer_label_2 = Label(contin, text='Ответ 2', font=label_font, **base_padding)
        answer_label_2.pack(ipady=10)

        answer_entry_2 = Entry(contin, bg='#fff', fg='#444', font=font_entry)
        answer_entry_2.pack(fill=X, ipady=10)

        answer_label_3 = Label(contin, text='Ответ 3', font=label_font, **base_padding)
        answer_label_3.pack(ipady=10)

        answer_entry_3 = Entry(contin, bg='#fff', fg='#444', font=font_entry)
        answer_entry_3.pack(fill=X, ipady=10)

            # кнопка отправки формы
        send_btn = Button(contin, text='Выйти в главное меню', command=exit_for_test)
        send_btn.place(x=650, y=10, width=200)

        
        main_label = Label(contin, text='Правильный ответ:', font=font_header, justify=CENTER, **header_padding)
        main_label.place(x=300, y=450, width=300)

        place_for_x_button_correct_answere = 355

        send_btn = Button(contin, text='№1', command=correct_answer_1)
        send_btn.place(x=place_for_x_button_correct_answere, y=500, width=50)

        send_btn = Button(contin, text='№2', command=correct_answer_2)
        send_btn.place(x=place_for_x_button_correct_answere + 70, y=500, width=50)

        send_btn = Button(contin, text='№3', command=correct_answer_3)
        send_btn.place(x=place_for_x_button_correct_answere + 140, y=500, width=50)


        contin.mainloop()
        


    def continue_creating():
        global ID_test

        user = username_entry
        new_test_name = testName_entry.get()
        new_password_test = password_entry.get()
        print(user, new_test_name, new_password_test)
        ID_test = Two_test.new_tests(user, new_test_name, new_password_test)
        print(ID_test)
        continue_new_test(ID_test)


    global test_record
    global win
    #user = username_entry
    main_w.destroy()
    test_record = 1

    win = Tk()
    win.title('Авторизация')
    # размер окна
    win.geometry('600x320')
    # можно ли изменять размер окна - нет
    win.resizable(False, False)

    # кортежи и словари, содержащие настройки шрифтов и отступов
    font_header = ('Arial', 15)
    font_entry = ('Arial', 12)
    label_font = ('Arial', 11)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    # заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
    # для всех остальных виджетов настройки делаются также
    main_label = Label(win, text='НОВЫЙ ТЕСТ', font=font_header, justify=CENTER, **header_padding)
    # помещаем виджет в окно по принципу один виджет под другим
    main_label.pack()

    # метка для поля ввода имени
    testName_label = Label(win, text='Создание теста', font=label_font, **base_padding)
    testName_label.pack()

    # поле ввода имени
    testName_entry = Entry(win, bg='#fff', fg='#444', font=font_entry)
    testName_entry.pack()

    # метка для поля ввода пароля
    passwordTest_label = Label(win, text='Пароль', font=label_font, **base_padding)
    passwordTest_label.pack()

    # поле ввода пароля
    password_entry = Entry(win, bg='#fff', fg='#444', font=font_entry)
    password_entry.pack()

    # кнопка отправки формы
    send_btn = Button(win, text='Задать вопросы', command=continue_creating)
    send_btn.pack(padx=5, pady=5)

    send_btn = Button(win, text='Назад', command=main_window)
    send_btn.pack(padx=5, pady=5)
    win.mainloop()



    print("new test")
    '''Two_test.new_tests(user)'''


def back_menu_test_available():
    global available_w

    available_w.destroy()
    main_window()


def test_available():
    def go_test_aviable():
        global go_tests_entry
        go_tests = go_tests_entry.get()
        go_tests = str(go_tests)
        print(go_tests)
        print(go_tests.isdigit())
        if go_tests.isdigit() == True:
            take_test_ID = go_tests
            print('Строка состоит только из цифр')
            print(take_test_ID)
            result_check_ID = Two_test.take_test_aviable(take_test_ID)

            if result_check_ID == True:
                print('')
                print('существует')
                print('')

            else:
                print('')
                print('не существует')
                print('')


        else:
            print('строка содержит символы')



    global go_tests_entry
    global available_w
    global main_w

    main_w.destroy()

    transition = 'Пройти тест'
    font_header = ('Arial', 15)
    font_entry = ('Arial', 12)
    label_font = ('Arial', 11)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    available_w = Tk()
    available_w.title('Пройти тест')
    # размер окна
    available_w.geometry('680x400')
    # можно ли изменять размер окна - нет
    available_w.resizable(False, False)

    go_tests_label = Label(available_w, text='Введите ID теста', font=label_font, **base_padding)
    go_tests_label.place(x=200, y=120, width=250)

    go_tests_entry = Entry(available_w, bg='#fff', fg='#444', font=font_entry)
    go_tests_entry.place(x=50, y=170, width=600)
    
    send_btn = Button(available_w, text='Пройти тест', command=go_test_aviable)
    send_btn.place(x=470, y=320, width=200)

    send_btn2 = Button(available_w, text='В меню', command=back_menu_test_available)
    send_btn2.place(x=500, y=10, width=150)
    available_w.mainloop()
    


#основное окно
def main_window():
    global transition
    global main_w
    global question_numbers

    question_numbers = 0



    transition = 'main_window'
    font_header = ('Arial', 15)
    font_entry = ('Arial', 12)
    label_font = ('Arial', 11)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}
    main_w = Tk()
    main_w.title('main')
    # размер окна
    main_w.geometry('600x320')
    # можно ли изменять размер окна - нет
    main_w.resizable(False, False)
    send_btn = Button(main_w, text='Создать тест', command=new_test)
    send_btn.place(x=50, y=190, width=200)
    send_btn = Button(main_w, text='Пройти тест', command=test_available)
    send_btn.place(x=350, y=190, width=200)
    send_btn3 = Button(main_w, text='Вернуться к началу', command=restart_program)
    send_btn3.place(x=350, y=10, width=200)
    if test_record == 0:
        contin.quit()
        contin.destroy()
    elif test_record == 1:
        reg.destroy()
    else:
        print('иначе')
    '''elif test_record == 1:
        win.destroy()'''
    '''else:
        reg.destroy()'''

# обработчик нажатия на клавишу 'Войти'
def clicked():

    global username_entry
    global password_entry


    cliked = "entrance"

    # получаем имя пользователя и пароль
    username = username_entry.get()
    password = password_entry.get()
    username_entry = username

    checking_symbol_in_username = username.find('/')
    checking_symbol_in_password = password.find('/')



    if checking_symbol_in_username == -1 and checking_symbol_in_password == -1:

        # Подсчет частоты символов в тексте
        text = username + "/" + password
        print(text)
        symbols_freq = defaultdict(int)
        for symbol in text:
            symbols_freq[symbol] += 1

        # Построение дерева Хаффмана и генерация кодов
        huffman_tree = build_huffman_tree(symbols_freq)
        huffman_codes = generate_huffman_codes(huffman_tree)
        huff_codes = huffman_codes

        # Сжатие данных
        compressed_data = compress_data(text, huffman_codes)

        function = "username_checking"
        check_name = Two_test.decompress_data_in_server(compressed_data, huff_codes, cliked, function)
        print(check_name)

        '''# проверяем, совпадают ли имя пользователя и пароль в базе данных
        cur.execute("SELECT * FROM users WHERE user_name = ? AND password = ?", (username, password))
        result = cur.fetchone()
        print(result, "-1")'''
        if check_name == True:
            #global username_entry
            username_entry = username
            print(True)
            main_window()
            # messagebox.showinfo('Успешная авторизация', 'Вы успешно авторизованы!')
        else:
            print(False)
            messagebox.showinfo('Ошибка авторизации', 'Неверное имя пользователя или пароль.')

            contin.quit()
            contin.destroy()

            first_window()



    else:
        print(False)
        messagebox.showinfo('Ошибка, вы использовали запрещенные символы (такие как: /, ?, \, (, ), * ')

def registration():
    global random_password
    global password_user
    global username_entry

    def check_username_exists(username):
        cur.execute("SELECT * FROM users WHERE user_name = ?", (username,))
        result = cur.fetchone()
        return bool(result)

    def generate_unique_username():
        while True:
            username = ''.join(random.choice(string.ascii_lowercase) for _ in range(12))
            if not check_username_exists(username):
                username_entry_1.delete(0, END)
                username_entry_1.insert(0, username)
                break



    def new_password():
        length = random.randint(8, 20)
        password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

        password_user.delete(0, END)
        password_user.insert(0, password)

    def record_regist():
        global test_record
        global username_entry
        test_record = 1
        username = username_entry_1.get()
        password = password_user.get()

        checking_symbol_in_username = username.find('/')
        checking_symbol_in_password = password.find('/')

        if checking_symbol_in_username == -1 and checking_symbol_in_password == -1:

            # Подсчет частоты символов в тексте
            text = username + "/" + password
            print(text)
            symbols_freq = defaultdict(int)
            for symbol in text:
                symbols_freq[symbol] += 1

            # Построение дерева Хаффмана и генерация кодов
            huffman_tree = build_huffman_tree(symbols_freq)
            huffman_codes = generate_huffman_codes(huffman_tree)
            huff_codes = huffman_codes

            # Сжатие данных
            compressed_data = compress_data(text, huffman_codes)

            cliked = 'entrance'
            function = "new_users"
            check_name = Two_test.decompress_data_in_server(compressed_data, huff_codes, cliked, function)
            print(check_name)

            if check_name == True:
                print(True)
                username_entry = username
                main_window()
                # messagebox.showinfo('Успешная авторизация', 'Вы успешно авторизованы!')
            else:
                print(False)
                messagebox.showwarning(title='Ошибка', message="Ваш пароль слишком короткий или такой пользователь уже существует")

        else:
            print(False)
            messagebox.showwarning(title='Ошибка', message="Вы использовали запрещенные символы (такие как: /, \, *, ~)")

    global reg
    global test_record
    test_record = 1
    font_header = ('Arial', 15)
    font_entry = ('Arial', 12)
    label_font = ('Arial', 11)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}
    reg = Tk()
    reg.title('Регистрация')
    # размер окна
    reg.geometry('600x320')
    # можно ли изменять размер окна - нет
    reg.resizable(False, False)
    main_label = Label(reg, text='Регистрация', font=font_header, justify=CENTER, **header_padding)
    main_label.pack()
    username_label_1 = Label(reg, text='Имя пользователя', font=label_font, **base_padding)
    username_label_1.pack()
    username_entry_1 = Entry(reg, bg='#fff', fg='#444', font=font_entry)
    username_entry_1.pack()

    send_btn = Button(reg, text='Создай имя пользователя', command=generate_unique_username)
    send_btn.pack(padx=5, pady=5)

    password_label_1 = Label(reg, text='Пароль', font=label_font, **base_padding)
    password_label_1.pack()
    password_user = Entry(reg, bg='#fff', fg='#444', font=font_entry)
    password_user.pack()

    send_btn = Button(reg, text='Создай пароль', command=new_password)
    send_btn.pack(padx=5, pady=5)

    send_btn = Button(reg, text='Зарегестрироваться', command=record_regist)
    send_btn.pack(padx=5, pady=5)



    contin.quit()
    contin.destroy()


global username_entry
global password_entry
def first_window():
    global password_entry
    global username_entry
    global password_user
    global test_record
    global contin
    global question_numbers

    question_numbers = 0

    if transition == 'main_window':
        main_w.destroy()

    test_record = 0
    contin = Tk()
    contin.title('Авторизация')
    # размер окна
    contin.geometry('600x320')
    # можно ли изменять размер окна - нет
    contin.resizable(False, False)

    # кортежи и словари, содержащие настройки шрифтов и отступов
    font_header = ('Arial', 15)
    font_entry = ('Arial', 12)
    label_font = ('Arial', 11)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    username_entry = str()
    password_entry = str()  

    # заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
    # для всех остальных виджетов настройки делаются также
    main_label = Label(contin, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
    # помещаем виджет в окно по принципу один виджет под другим
    main_label.pack()

    # метка для поля ввода имени
    username_label = Label(contin, text='Имя пользователя', font=label_font, **base_padding)
    username_label.pack()

    # поле ввода имени
    username_entry = Entry(contin, bg='#fff', fg='#444', font=font_entry)
    username_entry.pack()

    # метка для поля ввода пароля
    password_label = Label(contin, text='Пароль', font=label_font, **base_padding)
    password_label.pack()

    # поле ввода пароля
    password_entry = Entry(contin, bg='#fff', fg='#444', font=font_entry, show='*')
    password_entry.pack()


    # кнопка отправки формы
    send_btn = Button(contin, text='Войти', command=clicked)
    send_btn.pack(padx=5, pady=5)

    send_btn = Button(contin, text='Зарегестрироваться', command=registration)
    send_btn.pack(padx=5, pady=5)
    contin.mainloop()




first_window()




# запускаем главный цикл окна
contin.mainloop()