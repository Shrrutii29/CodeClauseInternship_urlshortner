from tkinter import *
import pyshorteners

def shortenurl():
	url = url_input.get()
	if url:
		s = pyshorteners.Shortener()
		output = s.tinyurl.short(url)
		result_label.config(text=output)
	else:
		result_label.config(text='Error : Enter URL')

def clearr():
	url_input.delete(0,END)
	result_label.config(text='')

root = Tk()
root.title('ShortenURL')
root.minsize(600,600)
root.configure(background='#007ea7')

#headline
text_label = Label(root,text='URL Shortener',fg='white',bg='#007ea7')
text_label.pack(pady=(200,5))
text_label.config(font=('verdana',30,'bold'))

#description
desp_label = Label(root,text='Intented to shorten given URL using python library called pyshorteners',fg='black',bg='#007ea7')
desp_label.pack()
desp_label.config(font=('verdana',20))

#URL input
url_label = Label(root,text='Enter/Paste URL to be shortened ',fg='white',bg='#007ea7')
url_label.pack(pady=(30,15))
url_label.config(font=('verdana',30,'bold'))

url_input = Entry(root,width=50)
url_input.pack(ipady=6,pady=(1,15))

#frame to align buttons horizontally
button_frame = Frame(root, bg='#007ea7')
button_frame.pack(pady=(15,25))

#clear button
clr_btn = Button(button_frame,text='Clear',bg="#003459",fg="white",width=20,height=2,command=clearr)
clr_btn.pack(side=LEFT,padx=(0,10))
clr_btn.config(font=('verdana',12))

#generate button
gen_btn = Button(button_frame,text='Shorten URL',bg="#003459",fg="white",width=20,height=2,command=shortenurl)
gen_btn.pack(side=LEFT,padx=(0,10))
gen_btn.config(font=('verdana',12))

#exit button
exit_btn = Button(button_frame,text='Exit',bg="#003459",fg="white",width=20,height=2,command=root.quit)
exit_btn.pack(side=LEFT)
exit_btn.config(font=('verdana',12))

#result
result_label = Label(root,text='',fg='white',bg='#007ea7')
result_label.pack()
result_label.config(font=('verdana',30,'bold'))

root.mainloop()	



