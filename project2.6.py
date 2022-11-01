from pymongo import *
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

def DBConnection():
        #Database connection and management
        client = MongoClient("mongodb+srv://e_albano11:soccerstatsbd2@cluster0-me1lc.mongodb.net/test?retryWrites=true&w=majority")
        database = client["SoccerStats"]
        global collection
        collection = database["Players"]
def FirstFrame():
        # ------------------------------------------------Search by name------------------------------------------------
        frame1 = LabelFrame(Window1, text="Ricerca Per Nome", padx=20, pady=20)
        frame1.grid(row=1, padx=20, pady=10)
        testo_frame1_1 = Label(frame1, text="Nome:")
        testo_frame1_1.grid(row=1, column=0)
        global input_frame1_1
        input_frame1_1 = Entry(frame1, width=30, borderwidth=5)
        input_frame1_1.insert(0, "Nome Calciatore")
        input_frame1_1.grid(row=1, column=1, padx=30)
        Button(frame1, text="Cerca", command=Search1).grid(row=1, column=2, sticky="N", padx=10,
                                                           pady=10)
def SecondFrame():
        # ------------------------------------------------Nationality ------------------------------------------------
        def callback(selezionato):
                global scelta_nazionalita
                scelta_nazionalita = selezionato

        global lista_nazionalita
        lista_nazionalita = ["Albania", "Algeria", "Argentina", "Australia", "Austria", "Belgium", "Bolivia", "Bosnia Herzegovina", "Brazil", "Bulgaria", "Cameroon", "Canada", "Chile", "China", "PR Colombia", "Costa Rica", "Croatia", "Czech Republic", "DR Congo", "Denmark", "Ecuador", "Egypt", "England", "Finland", "France", "Georgia", "Germany", "Ghana", "Greece", "Guinea", "Hungary", "Iceland", "India", "Italy", "Ivory Coast", "Jamaica", "Japan", "Korea Republic", "Kosovo", "Mali", "Mexico", "Morocco", "Netherlands", "New Zealand", "Nigeria", "Northern Ireland", "Norway", "Paraguay", "Peru", "Poland", "Portugal", "Republic of Ireland", "Romania", "Russia", "Saudi Arabia", "Scotland", "Senegal", "Serbia", "Slovakia", "Slovenia", "South Africa", "Spain", "Sweden", "Switzerland", "Tunisia", "Turkey", "Ukraine", "United States", "Uruguay", "Venezuela", "Wales"]

        clicked = StringVar()  # menu a tendina
        clicked.set("Seleziona")
        frame2 = LabelFrame(Window1, text="Ricerca Avanzata", padx=20, pady=10)
        frame2.grid(row=2, padx=20, pady=20)
        testo_frame2_1 = Label(frame2, text="Nazionalità :")
        testo_frame2_1.grid(row=2, column=0, padx=20, pady=5)
        global input_frame2_1
        input_frame2_1 = OptionMenu(frame2, clicked, *lista_nazionalita, command=callback)
        input_frame2_1.grid(row=2, column=1, padx=20, pady=5)

        # ------------------------------------------------Age ------------------------------------------------
        testo_frame2_2 = Label(frame2, text="Range di Età:")
        testo_frame2_2.grid(row=3, column=0, padx=20, pady=5)
        global input_frame2_2
        input_frame2_2 = Entry(frame2, width=8, borderwidth=5)
        input_frame2_2.insert(0, "Min")
        input_frame2_2.grid(row=3, column=1, padx=20, pady=5)
        global input_frame2_3
        input_frame2_3 = Entry(frame2, width=8, borderwidth=5)
        input_frame2_3.insert(0, "Max")
        input_frame2_3.grid(row=3, column=2, padx=20, pady=5)

        # ------------------------------------------------Overall Player ------------------------------------------------

        testo_frame2_3 = Label(frame2, text="Overall Calciatore:")
        testo_frame2_3.grid(row=4, column=0, padx=20, pady=5)
        global input_frame2_4
        input_frame2_4 = Entry(frame2, width=8, borderwidth=5)
        input_frame2_4.insert(0, 46)
        input_frame2_4.grid(row=4, column=1, padx=20, pady=5)
        global input_frame2_5
        input_frame2_5 = Entry(frame2, width=8, borderwidth=5)
        input_frame2_5.insert(0, 100)
        input_frame2_5.grid(row=4, column=2, padx=20, pady=5)

        # ------------------------------------------------Player's field ------------------------------------------------
        def callback2(selezionato2):
                global ruolo
                ruolo = selezionato2

        lista_ruoli = [
                "Portiere",
                "Difensore Centrale",
                "Terzino",
                "Centrocampista Centrale",
                "Esterno Destro",
                "Esterno Sinistro",
                "Attaccante"]

        clicked1 = StringVar()  # menu a tendina
        clicked1.set("Seleziona")
        testo_frame_2_4 = Label(frame2, text="Ruolo Calciatore :")
        testo_frame_2_4.grid(row=5, column=0, padx=20, pady=5)

        input_frame2_6 = OptionMenu(frame2, clicked1, *lista_ruoli, command=callback2)
        input_frame2_6.grid(row=5, column=1, padx=20, pady=5)
        Button(frame2, text="Cerca", command=Search2).grid(columnspan=3, sticky="N", padx=10, pady=5)
def ThirdFrame():
        # frame 4 con label e entry ------------------------------------------------
        # ------------------------------------------------Nationality ------------------------------------------------
        frame3 = LabelFrame(Window1, text="Ricerca Distribuzione", padx=20, pady=10)
        frame3.grid(row=3, padx=10, pady=10)

        def callback_distribuzione1(selezionato):
                global nazionalita_distribuzione1
                nazionalita_distribuzione1 = selezionato

        clicked = StringVar()  # menu a tendina
        clicked.set("Seleziona")
        testo_frame3_1 = Label(frame3, text=" Nazionalità :")
        testo_frame3_1.grid(row=0, column=0, padx=20, pady=5)
        global input_frame3_1
        input_frame3_1 = OptionMenu(frame3, clicked, *lista_nazionalita, command=callback_distribuzione1)
        input_frame3_1.grid(row=0, column=1, padx=20, pady=5)

        def callback_distribuzione2(selezionato):
                global nazionalita_distribuzione2
                nazionalita_distribuzione2 = selezionato

        clicked2 = StringVar()  # menu a tendina
        clicked2.set("Seleziona")
        testo_frame3_2 = Label(frame3, text=" Seconda Nazionalità :")
        testo_frame3_2.grid(row=2, column=0, padx=20, pady=5)
        global input_frame3_2
        input_frame3_2 = OptionMenu(frame3, clicked2, *lista_nazionalita, command=callback_distribuzione2)
        input_frame3_2.grid(row=2, column=1, padx=20, pady=5)

        def callback_distribuzione3(selezionato):
                global nazionalita_distribuzione3
                nazionalita_distribuzione3 = selezionato

        clicked3 = StringVar()  # menu a tendina
        clicked3.set("Seleziona")
        testo_frame3_3 = Label(frame3, text=" Terza Nazionalità :")
        testo_frame3_3.grid(row=3, column=0, padx=20, pady=5)
        input_frame3_3 = OptionMenu(frame3, clicked3, *lista_nazionalita, command=callback_distribuzione3)
        input_frame3_3.grid(row=3, column=1, padx=20, pady=5)

        testo_frame3_4 = Label(frame3, text="Range di Età:")
        testo_frame3_4.grid(row=4, column=0, padx=20, pady=5)
        global input_frame3_4
        input_frame3_4 = Entry(frame3, width=8, borderwidth=5)
        input_frame3_4.insert(0, "Min")
        input_frame3_4.grid(row=4, column=1, padx=20, pady=5)
        global input_frame3_5
        input_frame3_5 = Entry(frame3, width=8, borderwidth=5)
        input_frame3_5.insert(0, "Max")
        input_frame3_5.grid(row=4, column=2, padx=20, pady=5)
        Button(frame3, text="Cerca", command=Search3).grid(columnspan=3, sticky="N", padx=10, pady=5)
def Search1():
        toSearch = input_frame1_1.get()
        query_frame1 = {}
        query_frame1["Name"] = toSearch
        lista_risultati = []
        OutputQuery = list(
                collection.find(query_frame1, {"_id": 0, "Name": 1, "Nationality": 1, "Age": 1, "Overall": 1, "Position": 1}))
        if OutputQuery:
                lista_risultati.append(OutputQuery[0].get('Name'))
                lista_risultati.append(OutputQuery[0].get('Age'))
                lista_risultati.append(OutputQuery[0].get('Nationality'))
                lista_risultati.append(OutputQuery[0].get('Overall'))
                lista_risultati.append(OutputQuery[0].get('Position'))
        #       try:
        #               frame2.grid_forget()
        #               frame2.destroy()
        #       except NameError:
        #               pass


        # creazione frame
        frame4 = LabelFrame(Window1, width=800, height=700, text="Risultati Ricerca")
        frame4.grid(column=1, row=1, rowspan=2, padx=20, pady=20)

        # ------------------------------------------------Tabella -------------------------------------
        #titolo tabella
        if (OutputQuery):
                Label(frame4).grid(row=0, columnspan=3)
        else:
                Label(frame4, text="Nessun Calciatore Trovato", font=("Arial", 18)).grid(row=0, columnspan=3)

        cols = ('Nome', 'Età', 'Nazionalità', 'Overall', 'Ruolo')
        tabella = ttk.Treeview(frame4, show='headings')
        tabella["columns"] = cols
        tabella.column("Nome", width=200, minwidth=200)
        tabella.column("Età", width=50, minwidth=50)
        tabella.column("Nazionalità", width=150, minwidth=100)
        tabella.column("Overall", width=50, minwidth=50)
        tabella.column("Ruolo", width=150, minwidth=50)
        # intestazione colonne
        for col in cols:
                tabella.heading(col, text=col)
                tabella.column(col, anchor=N)
        tabella.grid(row=1, column=0, columnspan=2)
        tabella.insert("", "end", values=lista_risultati)
        lista_risultati = []
        def Delete():
                frame4.grid_forget()

        Button(frame4, text="Delete", command=Delete).grid(columnspan=3, sticky="N", padx=10, pady=5)
def Search2():
        # ------------------------------------------------Check sulle entry -------------------------------------
        # ---------------Nazionalità -------------------
        try:
                tryAssign0 = scelta_nazionalita
                flag_nazionalita = 1
        except NameError:
                flag_nazionalita = 0

        # ---------------età -------------------
        if input_frame2_2.get() == "Min":
                flag_eta_min = 0
        else:
                flag_eta_min = 1
                try:
                        float(input_frame2_2.get())
                except ValueError:
                        input_frame2_2.delete(0, 'end')
                        input_frame2_2.insert(0, 16)
                if int(input_frame2_2.get()) < 16:
                        input_frame2_2.delete(0, 'end')
                        input_frame2_2.insert(0, 16)

        if input_frame2_3.get() == "Max":
                flag_eta_max = 0
        else:
                flag_eta_max = 1
                try:
                        float(input_frame2_3.get())
                except ValueError:
                        input_frame2_3.delete(0, 'end')
                        input_frame2_3.insert(0, 45)
                if int(input_frame2_3.get()) > 45:
                        input_frame2_3.delete(0, 'end')
                        input_frame2_3.insert(0, 45)

        # ---------------Overall -------------------

        if input_frame2_4.get() == "46":
                flag_overall_min = 0
        else:
                flag_overall_min = 1
                try:
                        float(input_frame2_4.get())
                except ValueError:
                        input_frame2_4.delete(0, 'end')
                        input_frame2_4.insert(0, 46)
                if int(input_frame2_4.get()) < 46:
                        input_frame2_4.delete(0, 'end')
                        input_frame2_4.insert(0, 46)

        if input_frame2_5.get() == "100":
                flag_overall_max = 0
        else:
                flag_overall_max = 1
                try:
                        float(input_frame2_5.get())
                except ValueError:
                        input_frame2_5.delete(0, 'end')
                        input_frame2_5.insert(0, 99)
                if int(input_frame2_5.get()) > 100:
                        input_frame2_5.delete(0, 'end')
                        input_frame2_5.insert(0, 99)

        # ---------------Ruolo -------------------

        try:
                tryAssign1 = ruolo
                flag_ruolo = 1
        except NameError:
                flag_ruolo = 0

        # ------------------------------------------------Query -------------------------------------
        if flag_nazionalita == 0 and flag_eta_min == 0 and flag_eta_max == 0 and flag_overall_min == 0 and flag_overall_max == 0 and flag_ruolo == 0:
                pass
        else:
                query1 = {}

                if flag_nazionalita == 1:
                        query1["Nationality"] = tryAssign0
                if flag_eta_min == 1 and flag_eta_max == 0:
                        age = {}
                        age["$gte"] = input_frame2_2.get()
                        query1["Age"] = age
                if flag_eta_max == 1 and flag_eta_min == 0:
                        age = {}
                        age["$lte"] = input_frame2_3.get()
                        query1["Age"] = age
                if flag_eta_min == 1 and flag_eta_max == 1:
                        age = {}
                        age["$gte"] = input_frame2_2.get()
                        age["$lte"] = input_frame2_3.get()
                        query1["Age"] = age
                if flag_overall_min == 1 and flag_overall_max == 0:
                        overall = {}
                        overall["$gte"] = input_frame2_4.get()
                        query1["Overall"] = overall
                if flag_overall_max == 1 and flag_overall_min == 0:
                        overall = {}
                        overall["$lte"] = input_frame2_5.get()
                        query1["Overall"] = overall
                if flag_overall_max == 1 and flag_overall_min == 1:
                        overall = {}
                        overall["$gte"] = input_frame2_4.get()
                        overall["$lte"] = input_frame2_5.get()
                        query1["Overall"] = overall
                if flag_ruolo == 1:
                        query1["Position"] = tryAssign1

                lista_master = []
                lista_risultati = []
                # risultati3 = [{'Name': 'Thiago Silva', 'Age': '33', 'Nationality': 'Brazil', 'Overall': '88', 'Position': 'Difensore Centrale'}, {'Name': 'Ederson', 'Age': '24', 'Nationality': 'Brazil', 'Overall': '86', 'Position': 'Portiere'}]
                OutputQuery = list(collection.find(query1,
                                                  {"_id": 0, "Name": 1, "Nationality": 1, "Age": 1, "Overall": 1,
                                                   "Position": 1}))
                '''listaNazionalita = []
                listaNazionalita = collection.distinct("Nationality")
                nazionalita=""
                for nazionalita in listaNazionalita:
                        if collection.count_documents({"Nationality":nazionalita}) > 25:
                                print(nazionalita)'''


                numero_elementi = len(OutputQuery)

                for i in range(numero_elementi):
                        lista_risultati.append(OutputQuery[i].get('Name'))
                        lista_risultati.append(OutputQuery[i].get('Age'))
                        lista_risultati.append(OutputQuery[i].get('Nationality'))
                        lista_risultati.append(OutputQuery[i].get('Overall'))
                        lista_risultati.append(OutputQuery[i].get('Position'))
                        lista_master.append(lista_risultati)
                        lista_risultati = []

                frame4 = LabelFrame(Window1, width=800, height=700, text="Risultati Ricerca")
                frame4.grid(column=1, row=1, rowspan=2, padx=20, pady=20)
                if (lista_master):
                        Label(frame4).grid(row=0, columnspan=3)
                else:
                        Label(frame4, text="Nessun Calciatore Trovato", font=("Arial", 18)).grid(row=0,columnspan=3)

                cols = ('Nome', 'Età', 'Nazionalità', 'Overall', 'Ruolo')
                tabella = ttk.Treeview(frame4, show='headings')
                tabella["columns"] = ('Nome', 'Età', 'Nazionalità', 'Overall', 'Ruolo')
                tabella.column("Nome", width=200, minwidth=200)
                tabella.column("Età", width=50, minwidth=50)
                tabella.column("Nazionalità", width=150, minwidth=100)
                tabella.column("Overall", width=50, minwidth=50)
                tabella.column("Ruolo", width=150, minwidth=50)

                for col in cols:
                        tabella.heading(col, text=col)
                        tabella.column(col, anchor=N)
                tabella.grid(row=1, column=0, columnspan=2)

                ListaOrdinata = lista_master

                ListaOrdinata.sort(key=lambda e: e[3], reverse=True)
                # il sort mette in ordine secondo la e, in questo caso età

                for i, (Nome, Età, Nazionalità, Overall, Ruolo) in enumerate(ListaOrdinata, start=1):
                        tabella.insert("", "end", values=(Nome, Età, Nazionalità, Overall, Ruolo))
                def Delete():
                        frame4.grid_forget()
                Button(frame4, text="Delete", command=Delete).grid(columnspan=3, sticky="N", padx=10, pady=5)
def Search3():
        lista_temp = []
        lista1 = []
        lista2 = []
        lista3 = []

        # ---------------Nazionalità -------------------
        try:
                tryAssign0 = nazionalita_distribuzione1
                flag_nazionalita = 1
        except NameError:
                flag_nazionalita = 0
        # ---------------età -------------------
        if input_frame3_4.get() != "Min":
                try:
                        float(input_frame3_4.get())
                except ValueError:
                        input_frame3_4.delete(0, 'end')
                        input_frame3_4.insert(0, 16)
                if int(input_frame3_4.get()) < 16:
                        input_frame3_4.delete(0, 'end')
                        input_frame3_4.insert(0, 16)
        if input_frame3_5.get() != "Max":
                try:
                        float(input_frame3_5.get())
                except ValueError:
                        input_frame3_5.delete(0, 'end')
                        input_frame3_5.insert(0, 45)
                if int(input_frame3_5.get()) > 45:
                        input_frame3_5.delete(0, 'end')
                        input_frame3_5.insert(0, 45)

        if flag_nazionalita == 0 or (input_frame3_4.get() == "Min" and input_frame3_5.get() == "Max"):
                pass
        else:
                if input_frame3_5.get() == "Max":
                        input_frame3_5.delete(0, 'end')
                        input_frame3_5.insert(0, 45)
                if input_frame3_4.get() == "Min":
                        input_frame3_4.delete(0, 'end')
                        input_frame3_4.insert(0, 16)
                lista_eta = []
                range_eta = int(input_frame3_5.get()) - int(input_frame3_4.get()) + 1

                for i in range(range_eta):
                        lista_eta.append(int(input_frame3_4.get()) + i)



                '''pipeline1 = [{"$match": {"Nationality": nazionalita_distribuzione1,
                                        "Age": {"$gte": input_frame3_4.get(), "$lte": input_frame3_5.get()}}},
                            {"$group": {"_id": "$Age", "count": {"$sum":{"$ifNull":["$Age", 0]}}}}, {"$sort": {"_id": 1}}]'''
                pipeline1 = [{"$match": {"Nationality": nazionalita_distribuzione1,
                                         "Age": {"$gte": input_frame3_4.get(), "$lte": input_frame3_5.get()}}},
                             {"$group": {"_id": "$Age", "count": {"$sum": 1}}}, {"$sort": {"_id": 1}}]
                pipeline2 = [{"$match": {"Nationality": nazionalita_distribuzione2,
                                         "Age": {"$gte": input_frame3_4.get(), "$lte": input_frame3_5.get()}}},
                             {"$group": {"_id": "$Age", "count": {"$sum": 1}}}, {"$sort": {"_id": 1}}]
                pipeline3 = [{"$match": {"Nationality": nazionalita_distribuzione3,
                                         "Age": {"$gte": input_frame3_4.get(), "$lte": input_frame3_5.get()}}},
                             {"$group": {"_id": "$Age", "count": {"$sum": 1}}}, {"$sort": {"_id": 1}}]
                risultatiAggregate1 = list(collection.aggregate(pipeline1))
                risultatiAggregate2 = list(collection.aggregate(pipeline2))
                risultatiAggregate3 = list(collection.aggregate(pipeline3))
                '''print(risultatiAggregate1)
                print(risultatiAggregate2)
                print(risultatiAggregate3)
                print(lista_eta)'''
                dizionariobase = {'_id': '0', 'count': 0}
                for i in range(0,range_eta):
                        '''print(i)'''
                        if int(risultatiAggregate1[i].get('_id')) == lista_eta[i]:  # se l'età è uguale all'indice ok va avanti
                                pass
                        else:
                                dizionariobase['_id'] = str(lista_eta[i])
                                risultatiAggregate1.insert(i, dizionariobase)
                                '''print(risultatiAggregate1[i].get('_id'))'''
                                i -= 1
                array1 = []
                array2 = []
                array3 = []




                for i in lista_eta:
                        #print(risultatiAggregate1[0])
                        if risultatiAggregate1[0] != i:
                                risultatiAggregate1

                for i in range(len(risultatiAggregate1)):
                        lista_temp.append(risultatiAggregate1[i].get('_id'))
                        lista_temp.append(risultatiAggregate1[i].get('count'))
                        array1.append(risultatiAggregate1[i].get('count'))
                        lista1.append(lista_temp)
                        lista_temp = []

                for i in range(len(risultatiAggregate2)):
                        lista_temp.append(risultatiAggregate2[i].get('_id'))
                        lista_temp.append(risultatiAggregate2[i].get('count'))
                        array2.append(risultatiAggregate2[i].get('count'))
                        lista2.append(lista_temp)
                        lista_temp = []

                for i in range(len(risultatiAggregate3)):
                        lista_temp.append(risultatiAggregate3[i].get('_id'))
                        lista_temp.append(risultatiAggregate3[i].get('count'))
                        lista3.append(lista_temp)
                        array3.append(risultatiAggregate3[i].get('count'))
                        lista_temp = []


                frame4 = LabelFrame(Window1, width=300, height=300, text="Risultati Ricerca")
                frame4.grid(column=1, row=1, rowspan=4, padx=20, pady=20)

                figure1 = plt.Figure(figsize=(6, 5), dpi=100)
                ax1 = figure1.add_subplot(111)
                bar1 = FigureCanvasTkAgg(figure1, frame4)
                bar1.get_tk_widget().grid(columnspan=3, sticky="N", padx=10, pady=5)

                # creare dizionario con  nazionalita : [ occorrenze]
                plotdata = pd.DataFrame({
                        nazionalita_distribuzione1: array1,
                        nazionalita_distribuzione2: array2,
                        nazionalita_distribuzione3: array3

                },
                        index=lista_eta
                )

                plotdata.plot(kind='bar', legend=True, ax=ax1)
                ax1.set_title('Età Vs Occorrenze per Nazione')
                def Delete():
                        frame4.grid_forget()
                Button(frame4, text="Delete", command=Delete).grid(columnspan=3, sticky="N", padx=10, pady=5)




Window1 = Tk()
Window1.title("Soccer Stats")
Window1.attributes("-fullscreen", False)
image = Image.open("logo.jpg")
image = image.resize((200, 200), Image.ANTIALIAS)
Logo = ImageTk.PhotoImage(image)
logo = Label(image=Logo).grid( sticky = NSEW)

DBConnection()
FirstFrame()
SecondFrame()
ThirdFrame()
Window1.mainloop()

