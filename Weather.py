from tkinter import *
import requests, os
import tkinter.font as tkfont

HEIGHT = 500
WIDTH = 600

def test_function(entry):
	print("This is the entry:", entry)

# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}
# e320aa323238b2a5c666e78c762e9592

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem\nretrieving that information'

	return final_str

def get_weather(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)



root = Tk()
root.resizable(height = 0, width = 0)
root.title("Weather")

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = PhotoImage(file=str(os.getcwd())+'\\landscape.png')
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = Frame(root, bg='#fec051', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

fontStyle = tkfont.Font(family='calibri', size = '20')

entry = Entry(frame, font='calibri')
entry.place(relwidth=0.65, relheight=1)

button = Button(frame,
                   text="Get Weather",
                   bg="#392033",
                   font='calibri',
                   fg="#fd6051",
                   command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = Frame(root, bg='#fd6051', bd=15)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame, font = fontStyle)
label.place(relwidth=1,relheight=1)

root.mainloop()
