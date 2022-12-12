from PyQt5 import QtWidgets
from file_window import Ui_Dialog

from add_event_window import Ui_Dialog1
from add_menu_window import Ui_WindowNine
from add_place_window import Ui_WindowEight
from add_promotion_window import Ui_Dialog2
from add_review__window import Ui_WindowSeven
from choice_place_window import Ui_Dialog3
from main_window import Ui_MainWindow
from show_event_window import Ui_WindowFive
from show_menu_window import Ui_WindowFour
from show_place_window import Ui_WindowThree
from show_promotion_window import Ui_Dialog4
from show_comment_window import Ui_Dialog5
from update_event_window import Ui_update_event
from update_place_window import Ui_update_place
from update_menu_window import Ui_update_menu
from update_promotion_window import Ui_update_promotion

from db_file import add_user_in_table
from db_file import add_event_in_table
from db_file import add_menu_in_table
from db_file import add_promotion_in_table
from db_file import add_user_place_in_table
from db_file import add_place_in_table

from db_file import show_table
from db_file import get_place_title
from db_file import del_event_in_table
from db_file import del_promotion_in_table
from db_file import del_menu_in_table
from db_file import del_place_in_table
from db_file import del_user_place_in_table
from db_file import sql_procedure_menu
from db_file import sql_function_menu_price

from test1 import Ui_window_one
from test2 import Ui_Window_two
import sys

PLACE = ""
NAME_USER = ""
EVENT = ""
MENU = ""
PROMOTION = ""
DISCOUNT = False


def main_choice():
    global NAME_USER
    text = ui1.lineEdit.text()
    if text:
        result = add_user_in_table(text)
        print(result)
        # if result:
        #     pass
        # else:
        #     pass
        NAME_USER = text

        places = show_table("place")
        ui2.comboBox.clear()
        ui2.comboBox.addItem("")
        for elem in places:
            ui2.comboBox.addItem(elem["title"])

        main__window.close()
        choce_window.show()


def choce_add_place():
    choce_window.close()
    a_place_window.show()


def add_place_choce():
    new_title = ui3.lineEdit.text()
    new_type = ui3.lineEdit_2.text()
    new_description = ui3.textEdit.toPlainText()
    if new_title and new_type and new_description:
        result = add_place_in_table(new_type, new_title, new_description)
    ui2.comboBox.addItem(new_title)

    a_place_window.close()
    choce_window.show()


def choce_show_place():
    if not PLACE == "":
        good_places = ["bar", "Bar", "Ресторан", "Бар", "бар"]
        place_info = show_table("place")
        *place, = filter(lambda x: x["title"] == PLACE, place_info)
        place_id = place[0]["id"]
        place_type = place[0]["type"]
        ui4.label.setText(f"Название заведения: \n{PLACE}\n")
        ui4.textBrowser.setText(f"Тип заведения: {place_type}\nОписание:\n{place[0]['description']}")
        if place_type not in good_places:
            ui4.btn_3_1.close()
        else:
            ui4.btn_3_1.show()
        try:
            count_info = show_table("count_reviews")
            *count, = filter(lambda x: x["place_id"] == place_id, count_info)
            count_reviews = count[0]["count"]
        except Exception:
            count_reviews = 0
        ui4.label_3.setText(f"Отзывов: {count_reviews}")

        choce_window.close()
        s_place_window.show()


def show_place_show_menu():

    place_info = show_table("place")
    *place, = filter(lambda x: x["title"] == PLACE, place_info)
    place_id = place[0]["id"]
    #
    text = ""
    menu_info = show_table("menu")
    *menu, = filter(lambda x: x["place_id"] == place_id, menu_info)

    if DISCOUNT:
        for elem in menu:
            price = sql_function_menu_price(elem['price'])
            text += f"{elem['title']} -- \n{elem['description']}\nЦена: {price}\n\n"
    else:
        for elem in menu:

            text += f"{elem['title']} -- \n{elem['description']}\nЦена: {elem['price']}\n\n"

    menu_info = show_table("menu")
    ui5.comboBox.clear()
    ui5.comboBox.addItem("")
    for elem in menu_info:
        if elem["place_id"] == place_id:
            ui5.comboBox.addItem(str(elem["title"]))

    ui5.textBrowser.setText(text)

    s_place_window.close()
    s_menu_window.show()


def show_menu_show_place():

    s_menu_window.close()
    s_place_window.show()


def show_place_show_event():
    place_info = show_table("place")
    *place, = filter(lambda x: x["title"] == PLACE, place_info)
    place_id = place[0]["id"]
    #
    text = ""
    event_info = show_table("event")
    *event, = filter(lambda x: x["place_id"] == place_id, event_info)
    for elem in event:
        text += f"{elem['title']} -- \n{elem['description']}\n\n"

    ui7.comboBox.clear()
    ui7.comboBox.addItem("")
    for elem in event_info:
        if elem["place_id"] == place_id:
            ui7.comboBox.addItem(str(elem["title"]))

    ui7.textBrowser_2.setText(text)

    s_place_window.close()
    s_event_window.show()


def show_event_show_place():
    s_event_window.close()
    s_place_window.show()


def show_place_show_promotion():
    place_info = show_table("place")
    *place, = filter(lambda x: x["title"] == PLACE, place_info)
    place_id = place[0]["id"]
    #
    text = ""
    promotion_info = show_table("promotion")
    *promotion, = filter(lambda x: x["place_id"] == place_id, promotion_info)
    for elem in promotion:
        text += f"{elem['title']} -- \n{elem['description']}\n\n"

    promotion_info = show_table("promotion")
    ui19.comboBox.clear()
    ui19.comboBox.addItem("")
    for elem in promotion_info:
        if elem["place_id"] == place_id:
            ui19.comboBox.addItem(str(elem["title"]))

    ui19.textBrowser_2.setText(text)

    s_place_window.close()
    s_promotion_window.show()


def show_promotion_show_place():
    s_promotion_window.close()
    s_place_window.show()


def show_place_show_review():
    place_info = show_table("place")
    *place, = filter(lambda x: x["title"] == PLACE, place_info)
    place_id = place[0]["id"]

    reviews_info = show_table("user_place")
    *reviews, = filter(lambda x: x["place_id"] == place_id, reviews_info)
    user_id_list = list()
    reviews_list = list()
    for elem in reviews:
        user_id_list.append(elem["user_id"])
        reviews_list.append(elem["review"])

    user_info = show_table("users")
    names_dict = dict()
    for elem in user_info:
        names_dict[elem["id"]] = elem["name"]

    text = ""
    for ii in range(len(user_id_list)):
        text += f"{names_dict[user_id_list[ii]]}:\n{reviews_list[ii]}\n\n"

    ui13.textBrowser.setText(text)
    # pass
    s_place_window.close()
    s_comment_window.show()


def show_review_show_place():
    place_info = show_table("place")
    *place, = filter(lambda x: x["title"] == PLACE, place_info)
    place_id = place[0]["id"]
    try:
        count_info = show_table("count_reviews")
        *count, = filter(lambda x: x["place_id"] == place_id, count_info)
        count_reviews = count[0]["count"]
    except Exception:
        count_reviews = 0
    ui4.label_3.setText(f"Отзывов: {count_reviews}")
    s_comment_window.close()
    s_place_window.show()


def show_place_choice_place():
    s_place_window.close()
    choce_window.open()


def show_menu_add_menu():
    s_menu_window.close()
    a_menu_window.show()


def show_event_add_event():
    s_event_window.close()
    a_event_window.show()


def show_promotion_add_promotion():
    s_promotion_window.close()
    a_promotion_window.show()


def show_review_add_review():
    s_comment_window.close()
    a_review_window.show()
    pass


def add_menu_show_menu():
    try:
        title = ui6.lineEdit_2.text()
        description = ui6.textEdit.toPlainText()
        price = int(ui6.lineEdit.text())
        place_info = show_table("place")
        *place, = filter(lambda x: x["title"] == PLACE, place_info)
        place_id = place[0]["id"]
        result = add_menu_in_table(title, description, place_id, price)
        print(result)
        a_menu_window.close()
        s_menu_window.show()
    except Exception as ex:
        print(ex)


def add_menu_show_menu_cancel():
    a_menu_window.close()
    s_menu_window.show()


def add_event_show_event():
    title = ui8.lineEdit_3.text()
    description = ui8.textEdit_2.toPlainText()
    place_info = show_table("place")
    *place, = filter(lambda x: x["title"] == PLACE, place_info)
    place_id = place[0]["id"]
    result = add_event_in_table(place_id, title, description)
    print(result)
    a_event_window.close()
    s_event_window.show()


def add_event_show_event_cancel():
    a_event_window.close()
    s_event_window.show()


def add_promotion_show_promotion():
    title = ui9.lineEdit_2.text()
    description = ui9.textEdit.toPlainText()
    place_info = show_table("place")
    *place, = filter(lambda x: x["title"] == PLACE, place_info)
    place_id = place[0]["id"]
    result = add_promotion_in_table(place_id, title, description)
    print(result)
    a_promotion_window.close()
    s_promotion_window.show()


def add_promotion_show_promotion_cancel():
    a_promotion_window.close()
    s_promotion_window.show()


def add_review_show_review():
    review = ui11.textEdit.toPlainText()
    place_info = show_table("place")
    *place, = filter(lambda x: x["title"] == PLACE, place_info)
    place_id = place[0]["id"]

    users_info = show_table("users")
    *users, = filter(lambda x: x["name"] == NAME_USER, users_info)
    user_id = users[0]["id"]
    result = add_user_place_in_table(place_id, user_id, review)
    print(result)

    a_review_window.close()
    s_comment_window.show()
    pass


def to_update_place():
    if PLACE:
        place_info = show_table("place")
        *place, = filter(lambda x: x["title"] == PLACE, place_info)
        description = place[0]["description"]
        title = PLACE
        type_place = place[0]["type"]

        u_place_w.lineEdit.setText(title)
        u_place_w.lineEdit_2.setText(type_place)
        u_place_w.textEdit.setText(description)

        choce_window.close()
        u_place_window.show()


def from_update_place():
    new_title = u_place_w.lineEdit.text()
    new_type = u_place_w.lineEdit_2.text()
    new_description = u_place_w.textEdit.toPlainText()
    if new_title and new_type and new_description:
        result = del_place_in_table(PLACE)
        print(result)
        result = add_place_in_table(new_type, new_title, new_description)
        print(result)

    places = show_table("place")
    ui2.comboBox.clear()
    ui2.comboBox.addItem("")
    for elem in places:
        ui2.comboBox.addItem(elem["title"])

    u_place_window.close()
    choce_window.show()


def from_update_place_cancel():

    u_place_window.close()
    choce_window.show()


def to_update_event():
    if EVENT:
        place_info = show_table("place")
        *place, = filter(lambda x: x["title"] == PLACE, place_info)
        place_id = place[0]["id"]

        event_info = show_table("event")
        *event_info, = filter(lambda x: x["title"] == EVENT and x["place_id"] == place_id, event_info)
        title = EVENT
        description = event_info[0]["description"]

        u_event_w.lineEdit_3.setText(title)
        u_event_w.textEdit_2.setText(description)

        s_event_window.close()
        u_event_window.show()


def from_update_event():
    title = u_event_w.lineEdit_3.text()
    description = u_event_w.textEdit_2.toPlainText()
    place_info = show_table("place")
    *place, = filter(lambda x: x["title"] == PLACE, place_info)
    place_id = place[0]["id"]

    del_event_in_table(place_id, EVENT)


    place_id = place[0]["id"]
    result = add_event_in_table(place_id, title, description)
    print(result)

    u_event_window.close()
    s_event_window.show()


def from_update_event_cancel():
    u_event_window.close()
    s_event_window.show()


def to_update_menu():
    if MENU:
        place_info = show_table("place")
        *place, = filter(lambda x: x["title"] == PLACE, place_info)
        place_id = place[0]["id"]
        menu_info = sql_procedure_menu(place_id, MENU)
        print(menu_info)
        description = menu_info["description"]
        price = menu_info["price"]
        title = MENU
        print(title)
        print(price)
        print(description)

        u_menu_w.lineEdit_2.setText(title)
        u_menu_w.lineEdit.setText(str(price))
        u_menu_w.textEdit.setText(description)

        s_menu_window.close()
        u_menu_window.show()


def from_update_menu():
    title = u_menu_w.lineEdit_2.text()
    description = u_menu_w.textEdit.toPlainText()
    price = float(u_menu_w.lineEdit.text())
    place_info = show_table("place")
    *place, = filter(lambda x: x["title"] == PLACE, place_info)
    place_id = place[0]["id"]
    del_menu_in_table(place_id, MENU)
    result = add_menu_in_table(title, description, place_id, price)
    print(result)

    u_menu_window.close()
    s_menu_window.show()


def from_update_menu_cancel():
    u_menu_window.close()
    s_menu_window.show()


def to_update_promotion():
    if PROMOTION:
        place_info = show_table("place")
        *place, = filter(lambda x: x["title"] == PLACE, place_info)
        place_id = place[0]["id"]

        promotion_info = show_table("promotion")
        *promotion_info, = filter(lambda x: x["title"] == PROMOTION and x["place_id"] == place_id, promotion_info)
        title = PROMOTION
        description = promotion_info[0]["description"]

        u_event_w.lineEdit_3.setText(title)
        u_event_w.textEdit_2.setText(description)

        s_promotion_window.close()
        u_promotion_window.show()


def from_update_promotion():
    title = u_promotion_w.lineEdit_2.text()
    description = u_promotion_w.textEdit.toPlainText()
    place_info = show_table("place")
    *place, = filter(lambda x: x["title"] == PLACE, place_info)
    place_id = place[0]["id"]
    del_promotion_in_table(place_id, title)
    result = add_promotion_in_table(place_id, title, description)
    print(result)

    u_promotion_window.close()
    s_promotion_window.show()


def from_update_promotion_cancel():
    u_promotion_window.close()
    s_promotion_window.show()


app = QtWidgets.QApplication(sys.argv)


a_event_window = QtWidgets.QDialog()
ui8 = Ui_Dialog1()
ui8.setupUi(a_event_window)
ui8.btn_10_1.clicked.connect(add_event_show_event)
ui8.btn_11_2.clicked.connect(add_event_show_event_cancel)
# ui8.btn_10_2.clicked.connect(testing)


a_menu_window = QtWidgets.QDialog()
ui6 = Ui_WindowNine()
ui6.setupUi(a_menu_window)
ui6.btn_9_1.clicked.connect(add_menu_show_menu)
ui6.btn_11_2.clicked.connect(add_menu_show_menu_cancel)


a_place_window = QtWidgets.QDialog()
ui3 = Ui_WindowEight()
ui3.setupUi(a_place_window)
ui3.btn_8_1.clicked.connect(add_place_choce)


a_promotion_window = QtWidgets.QDialog()
ui9 = Ui_Dialog2()
ui9.setupUi(a_promotion_window)
ui9.btn_11_1.clicked.connect(add_promotion_show_promotion)
ui9.btn_11_2.clicked.connect(add_promotion_show_promotion_cancel)

a_review_window = QtWidgets.QDialog()
ui11 = Ui_WindowSeven()
ui11.setupUi(a_review_window)
ui11.btn_7_1.clicked.connect(add_review_show_review)
# ui11.btn_11_2.clicked.connect(addre)

# a_comment_window = QtWidgets.QDialog()
# ui15 = Ui_WindowSeven()
# ui15.setupUi(a_event_window)
# ui15.btn_7_1.clicked.connect(add_review_show_review)


def combobox_choice_place(text):
    global PLACE
    PLACE = text


def find_place():
    global PLACE
    PLACE = ""
    find_menu = ui2.lineEdit_3.text()
    find_event = ui2.lineEdit_4.text()

    def find_place_index_menu():
        menu = show_table("menu")
        place_id_menu = list()
        for elem_menu in menu:
            if find_menu in elem_menu["title"]:
                place_id_menu.append(elem_menu["place_id"])

        return place_id_menu

    def find_place_index_event():
        event = show_table("event")

        place_id_event = list()
        for elem_event in event:
            if find_event in elem_event["title"]:
                place_id_event.append(elem_event["place_id"])

        return place_id_event

    if find_menu and find_event:
        place_id_menu = find_place_index_menu()
        place_id_event = find_place_index_event()
        place_id = list(set(place_id_menu) & set(place_id_event))

    elif find_menu:
        place_id = find_place_index_menu()

    elif find_event:
        place_id = find_place_index_event()

    else:
        return

    places = show_table("place")
    ui2.comboBox.clear()
    ui2.comboBox.addItem("")
    for elem in places:
        if elem["id"] in place_id:
            ui2.comboBox.addItem(elem["title"])


def return_choice_user():
    choce_window.close()
    main__window.show()


def delete_place():
    result = del_place_in_table(PLACE)
    print(result)


choce_window = QtWidgets.QDialog()
ui2 = Ui_Dialog3()
ui2.setupUi(choce_window)
ui2.comboBox.activated[str].connect(combobox_choice_place)
ui2.btn_2_1.clicked.connect(choce_add_place)
ui2.btn_2_2.clicked.connect(choce_show_place)
ui2.button.clicked.connect(find_place)
ui2.btn.clicked.connect(return_choice_user)
ui2.pushButton_3.clicked.connect(to_update_place)

main__window = QtWidgets.QMainWindow()
ui1 = Ui_MainWindow()
ui1.setupUi(main__window)
ui1.btn.clicked.connect(main_choice)
main__window.show()


def delete_event():
    place_info = show_table("place")
    *place, = filter(lambda x: x["title"] == PLACE, place_info)
    place_id = place[0]["id"]

    result = del_event_in_table(place_id, EVENT)
    print(result)

    event_info = show_table("event")
    ui7.comboBox.clear()
    ui7.comboBox.addItem("")
    for elem in event_info:
        ui7.comboBox.addItem(str(elem["title"]))


def event_delete_box(text):
    global EVENT
    EVENT = text


s_event_window = QtWidgets.QDialog()
ui7 = Ui_WindowFive()
ui7.setupUi(s_event_window)
ui7.btn_5_1.clicked.connect(show_event_add_event)
ui7.pushButton.clicked.connect(show_event_show_place)
ui7.pushButton_2.clicked.connect(delete_event)
ui7.pushButton_3.clicked.connect(to_update_event)
ui7.comboBox.activated[str].connect(event_delete_box)


def delete_menu():
    place_info = show_table("place")
    *place, = filter(lambda x: x["title"] == PLACE, place_info)
    place_id = place[0]["id"]

    result = del_menu_in_table(place_id, MENU)
    print(result)

    menu_info = show_table("menu")
    ui7.comboBox.clear()
    ui7.comboBox.addItem("")
    for elem in menu_info:
        ui7.comboBox.addItem(str(elem["title"]))


def menu_delete_box(text):
    global MENU
    MENU = text


def change_discount_flag():
    global DISCOUNT
    DISCOUNT = not DISCOUNT

    place_info = show_table("place")
    *place, = filter(lambda x: x["title"] == PLACE, place_info)
    place_id = place[0]["id"]
    #
    text = ""
    menu_info = show_table("menu")
    *menu, = filter(lambda x: x["place_id"] == place_id, menu_info)

    if DISCOUNT:
        ui5.label_7.setText("Скидка активирована")
        for elem in menu:
            price = sql_function_menu_price(elem['price'])
            text += f"{elem['title']} -- \n{elem['description']}\nЦена: {float(price)}\n\n"
    else:
        ui5.label_7.setText("Скидка не активирована")
        for elem in menu:
            text += f"{elem['title']} -- \n{elem['description']}\nЦена: {float(elem['price'])}\n\n"

    menu_info = show_table("menu")
    ui5.comboBox.clear()
    ui5.comboBox.addItem("")
    for elem in menu_info:
        if elem["place_id"] == place_id:
            ui5.comboBox.addItem(str(elem["title"]))

    ui5.textBrowser.setText(text)


s_menu_window = QtWidgets.QDialog()
ui5 = Ui_WindowFour()
ui5.setupUi(s_menu_window)
ui5.btn_4_1.clicked.connect(show_menu_add_menu)
ui5.btn_4_2.clicked.connect(show_menu_show_place)
ui5.btn_5.clicked.connect(change_discount_flag)
ui5.pushButton_2.clicked.connect(delete_menu)
ui5.pushButton_3.clicked.connect(to_update_menu)
ui5.comboBox.activated[str].connect(menu_delete_box)

s_place_window = QtWidgets.QDialog()
ui4 = Ui_WindowThree()
ui4.setupUi(s_place_window)
ui4.btn_3_1.clicked.connect(show_place_show_menu)
ui4.btn_3_2.clicked.connect(show_place_show_event)
ui4.btn_3_3.clicked.connect(show_place_show_promotion)
# ui4.btn_3_4.clicked.connect(show_place_show_review)
ui4.pushButton.clicked.connect(show_place_show_review)
ui4.pushButton_2.clicked.connect(show_place_choice_place)


def delete_promotion():
    place_info = show_table("place")
    *place, = filter(lambda x: x["title"] == PLACE, place_info)
    place_id = place[0]["id"]

    result = del_promotion_in_table(place_id, PROMOTION)
    print(result)

    promotion_info = show_table("promotion")
    ui7.comboBox.clear()
    ui7.comboBox.addItem("")
    for elem in promotion_info:
        ui7.comboBox.addItem(str(elem["title"]))


def promotion_delete_box(text):
    global PROMOTION
    PROMOTION = text


s_promotion_window = QtWidgets.QDialog()
ui19 = Ui_Dialog4()
ui19.setupUi(s_promotion_window)
ui19.btn_5_1.clicked.connect(show_promotion_add_promotion)
ui19.pushButton.clicked.connect(show_promotion_show_place)
ui19.pushButton_2.clicked.connect(delete_promotion)
ui19.pushButton_3.clicked.connect(to_update_promotion)
ui19.comboBox.activated[str].connect(promotion_delete_box)


def delete_review():
    place_info = show_table("place")
    *place, = filter(lambda x: x["title"] == PLACE, place_info)
    place_id = place[0]["id"]

    user_info = show_table("users")
    *user_info, = filter(lambda x: x["name"] == NAME_USER, user_info)
    user_id = user_info[0]["id"]

    result = del_user_place_in_table(place_id, user_id)
    print(result)


s_comment_window = QtWidgets.QDialog()
ui13 = Ui_Dialog5()
ui13.setupUi(s_comment_window)
ui13.pushButton.clicked.connect(show_review_add_review)
ui13.pushButton_2.clicked.connect(show_review_show_place)
ui13.pushButton_3.clicked.connect(delete_review)


u_place_window = QtWidgets.QDialog()
u_place_w = Ui_update_place()
u_place_w.setupUi(u_place_window)
u_place_w.btn_8_1.clicked.connect(from_update_place)
u_place_w.btn_11_2.clicked.connect(from_update_place_cancel)

u_event_window = QtWidgets.QDialog()
u_event_w = Ui_update_event()
u_event_w.setupUi(u_event_window)
u_event_w.btn_10_1.clicked.connect(from_update_event)
u_event_w.btn_11_2.clicked.connect(from_update_event_cancel)

u_menu_window = QtWidgets.QDialog()
u_menu_w = Ui_update_menu()
u_menu_w.setupUi(u_menu_window)
u_menu_w.btn_9_1.clicked.connect(from_update_menu)
u_menu_w.btn_11_2.clicked.connect(from_update_menu_cancel)

u_promotion_window = QtWidgets.QDialog()
u_promotion_w = Ui_update_promotion()
u_promotion_w.setupUi(u_promotion_window)
u_promotion_w.btn_11_1.clicked.connect(from_update_promotion)
u_promotion_w.btn_11_2.clicked.connect(from_update_place_cancel)



# second_window = QtWidgets.QDialog()
# ui = Ui_Window_two()
# ui.setupUi(second_window)
# ui.pushButton.clicked.connect(open_first_window)
#
# WINDOW = QtWidgets.QDialog()
# ui = Ui_WindowSeven()
# ui.setupUi(WINDOW)
# # ui.pushButton.clicked.connect(open_second_window)
# WINDOW.show()


sys.exit(app.exec_())


#
# class mywindow(QtWidgets.QMainWindow):
#
#     def __init__(self):
#         super(mywindow, self).__init__()
#         self.ui = Ui_window_one()
#         self.ui.setupUi(self)
#         self.show()
#
#         self.ui.pushButton.clicked.connect(self.func_1)
#
#     def func_1(self):
#         self.close()
#         self.ui = Ui_Window_two()
#         self.ui.setupUi(self)
#         self.show()
#
#         self.ui.pushButton.clicked.connect(self.func_2)
#
#     def func_2(self):
#
#         self.ui = Ui_window_one()
#
#         self.ui.setupUi(self)
#         self.close()
#         self.show()
#
#         self.ui.pushButton.clicked.connect(self.func_1)
#
#
# app = QtWidgets.QApplication([])
# application = mywindow()
#
# sys.exit(app.exec())