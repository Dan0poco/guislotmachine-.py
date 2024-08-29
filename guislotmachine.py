from tkinter import Tk, Label
import random

window = Tk()
window.title("slot machine")
window.geometry("400x332")

print("(Not a real slot machine)")
print("Just a test")
print("")

credit = 100

show_credit01 = Label(window, font=("Helvectica", 10))
show_credit01.config(text=("You had =", credit, "credit"))
show_credit01.pack()

slot01_res = random.randint(0,2)

slot01 = Label(window, font=("Helvectica", 80))


slot01.config(text=(slot01_res))
slot01.pack()

slot02_res = random.randint(0,2)

slot02 = Label(window, font=("Helvectica", 80))


slot02.config(text=(slot02_res))
slot02.pack()

result_intext = ""

if slot01_res == slot02_res:
    result_intext = "Nice you won"
    credit += 100
else:
    result_intext = "Aww you we're so so soo close"
    credit -= 50


text_frog = Label(window, font=("Helvectica", 19))
text_frog.config(text=(result_intext))
text_frog.pack()

show_credit = Label(window, font=("Helvectica", 10))
show_credit.config(text=('You currently have =',credit, 'credit'))
show_credit.pack()


window.mainloop()