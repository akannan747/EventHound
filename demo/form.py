from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from hound import find_sim_event
from functools import partial
import webbrowser
from tkHyperlinkManager import *

root = Tk()
root.geometry("1000x500")
w = Label(root, text="EventHound")
w.pack()

messagebox.showinfo("Welcome to EventHound!", "Enter your search query here.")

name = simpledialog.askstring("Name", "What is your name?")
query_string = simpledialog.askstring("Query", "Please enter a query string. (our vocabulary is limited at the moment, test with 'dance')")
num_results = simpledialog.askinteger("Number of Results", "How many results would you like to see?")

search_results = find_sim_event(query_string, num_results)

text = Text()
text.pack()
hyperlink = HyperlinkManager(text)
text.insert(INSERT, "Here are your search results for " + query_string + ":\n\t")
for result in search_results:
    text.insert(INSERT, result[0], hyperlink.add(partial(webbrowser.open, result[0])))
    text.insert(INSERT, "\n\t")

mainloop()