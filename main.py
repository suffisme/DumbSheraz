import tkinter as tk
import tkinter.font as font
import random as rn
import time as t


window = tk.Tk()
movie_names = []

countDown_seconds = list(range(151))
countDown_seconds.reverse()

window.title('Dumb Cherades - Created By Sufiyan')
window.minsize(500,400)
window.columnconfigure(0,weight=1,minsize=500)

with open('movies.txt','r') as raw:
	for line in raw:
		movie_names.append(line)

def count_down(i=0):
	count_down_font  = font.Font(family='Helvetica',size=15,weight='bold')
	lbl_count_down  = tk.Label(frame_count_down,text=countDown_seconds[i],font=count_down_font)
	lbl_count_down.grid(row=0,column=0,sticky='we')
	if(i==150):
		lbl_count_down  = tk.Label(frame_count_down,text='Time\'s Up',font=count_down_font)
		lbl_count_down.grid(row=0,column=0,sticky='we')
		return
	frame_count_down.after(1000,count_down,i+1)

def generate_film():
	frame_movie_name = tk.Frame(window)
	film_font  = font.Font(family='Helvetica',size=15,weight='bold')
	num = rn.randint(0,len(movie_names))
	lbl_movie_name = tk.Label(frame_movie_name,text='Name : '+ movie_names[num],font=film_font,bg='#efefef')
	lbl_movie_name.pack()
	lbl_notif = tk.Label(frame_movie_name,text='You will have 150 seconds to play',bg='#efefef',font=font.Font(family='Helvetica',size=10,weight='bold'))
	lbl_notif.pack()
	btn_countdown = tk.Button(frame_count_down,text='Start Countdown',command=count_down)
	btn_countdown.grid(row=0,column=0,sticky='we')
	frame_movie_name.grid(row=2,column=0,padx=5,pady=5,ipadx=5,ipady=5,sticky='we')

head_font = font.Font(family='Helvetica',size=35,weight='bold')
lbl_head = tk.Label(window,text='dUmB CHerAdeS',font=head_font,fg='#000',bg='#a9d9d9') #666456
lbl_head.grid(row=0,column=0,sticky='ns',padx=5,pady=5,ipadx=5,ipady=5)
btn_font = font.Font(family='Helvetica',size=10,weight='bold')

btn_generate_film = tk.Button(window,text='Click to Generate A Movie',font=btn_font,command=generate_film)
btn_generate_film.grid(row=1,column=0,sticky='sn',ipadx=5,ipady=5,padx=5,pady=5)

frame_count_down = tk.Frame(window)
frame_count_down.grid(row=3,column=0,padx=5,pady=5,ipadx=5,ipady=5)

window.mainloop()
