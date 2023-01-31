import tkinter
import tkinter.messagebox
import customtkinter
import sqlite3
# main (root) GUI menu
customtkinter.set_default_color_theme("blue")



        


class DatabaseGUI:      # drives the main GUI elements
    def __init__(self):
        self.main_window = customtkinter.CTk()
        
        
        self.main_window.title('DataBase Checker')
        self.main_window.geometry("500x400")


        self.top_frame = customtkinter.CTkFrame(self.main_window)
        self.bottom_frame = customtkinter.CTkFrame(self.main_window)

        self.data_frame = customtkinter.CTkFrame(self.main_window)
        
        

       #CTk

        # create the search bar and search button
        self.tkinterText = "Enter the name of the database file you wish to search for"
        self.search_title = customtkinter.CTkLabel(self.top_frame, text=self.tkinterText, font=("Arial", 13))
        self.db_search_entry = customtkinter.CTkEntry(self.top_frame)

        # pack the radio buttons
        self.search_title.pack()
        self.db_search_entry.pack(anchor="s")
        
        #self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons
        self.search_button = customtkinter.CTkButton(self.bottom_frame, text='Search', command=lambda:self.connectToDataBase(self.db_search_entry.get()))

        

        # pack the buttons
        self.search_button.pack(side='left')
        

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        self.main_window.mainloop()
    
    def connectToDataBase(self, search_entry):
        self.Db_driver = DB_Driver(search_entry)
        self.present_all_tables_on_screen()
        

    def present_all_tables_on_screen(self):
        self.data_frame.destroy()
        self.data_frame = customtkinter.CTkFrame(self.main_window)
        listOfAllTables = self.Db_driver.query_all_table_names()
        self.data_screen = customtkinter.CTkLabel(self.data_frame, text="Click a Table to view its contents", font=("Arial", 13))
        self.data_screen.pack(anchor="n")

        for table in listOfAllTables:
            
            self.__table_button = customtkinter.CTkButton(self.data_frame, text=table, command=lambda table=table:self.search_in_Database(table))

            self.__table_button.pack(side="left")
            
        
        self.data_frame.pack()
        
    def search_in_Database(self, name):     # makes column frames with entries underneath
        try:        #everytime the new table button is pressed it attempts to wipe the frame
            self.parentFRAME.destroy()
        except AttributeError:
            pass
        self.parentFRAME = customtkinter.CTkFrame(self.main_window)
        
        

    
        tableName = name[0]
       
        
        all_columns = self.Db_driver.query_columns(tableName)
        


        for column in all_columns:
            columnFRame = customtkinter.CTkFrame(self.parentFRAME)
            self.__column_Title = customtkinter.CTkLabel(columnFRame, text=column, font=("Arial", 12))
            self.__column_Title.pack()
            column_entries = self.Db_driver.column_search(tableName, column)
            for entryList in column_entries:
                self.__entry = customtkinter.CTkLabel(columnFRame, text=entryList[0], font=("Arial", 12))
                self.__entry.pack()
            columnFRame.pack(side='left', padx=3)
        self.parentFRAME.pack()

            

        
        
        


                

        
        



       
        








          
           


        




    

class DB_Driver:        #drives the database searching elements

    def __init__(self, DB_NAME):
        db_query = DB_NAME + ".db"
        self.database = sqlite3.connect(db_query)
        self.cursor = self.database.cursor()
       
 
    def query_all_table_names(self):      # searches all the database for table names and returns a list of them
        sql_table_query = """SELECT name FROM sqlite_master WHERE type='table'"""
        self.cursor.execute(sql_table_query)
        list_of_tables = self.cursor.fetchall()
        return list_of_tables

    

    def query_columns(self, tableName): #retrives a list of all the columns in the corresponding table name
       
        column_query = f"""SELECT * FROM {tableName}"""
        
        data = self.cursor.execute(column_query)
        col_list = []
        for column in data.description:     # appends the ite, for the query into col_listn 
            
            col_list.append(column[0])
  
        return col_list
    
    def column_search(self, tableName, columnName):     #takes table name and column name and returns the entries of the following two
        sqlS = f"""SELECT {columnName} FROM {tableName}""" #placeholder string with empty space for search queries, cant use ? method when the tablename is unknown 
        column_results = self.cursor.execute(sqlS)
        return column_results.fetchall()
       










DatabaseGUI()



    

        