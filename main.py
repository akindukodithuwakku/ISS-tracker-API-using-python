from tkinter import *
import requests


def get_quote():

    response = requests.get(url="https://api.kanye.rest") #fetch API key
    response.raise_for_status() #sending the exeption error code

    quote = response.json() #take the response from json file
    data = quote["quote"] #taking the data from the tupple quotes

#change the data inside the canvas text
    canvas.itemconfig(quote_text, text= data)




window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="press kanye to see his thoughts", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()