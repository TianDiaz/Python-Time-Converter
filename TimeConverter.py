# Importing the modules
import tkinter as tk
import tkinter.font as font
from functools import partial
from tkinter import StringVar, messagebox
from tkinter import ttk

# Creating the window
window = tk.Tk()
window.geometry('570x350')
window.title('Python Time Converter')
window.configure(bg='#58A4B4')

# Creating the fonts
font1 = font.Font(family='helvetica', size=30, weight='bold')
font2 = font.Font(family='helvetica', size=10, weight='bold')
font3 = font.Font(family='helvetica', size=8)

# The text-variables
number_from = StringVar()

# All the functions

def fromfunc(event):
    global result_from
    result_from = event.widget.get()


# Tofunc function
def tofunc(event):
    global result_to
    result_to = event.widget.get()


# The answer function
def answer(n1):
    num1 = n1.get()
    try:
        number1 = float(num1)
    except:
        messagebox.showerror('Error', 'Invalid input')

# Nanosecond Conversion
    if result_from == 'Nanosecond' and result_to == 'Nanosecond':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Nanosecond' and result_to == 'Microsecond':
        calculate = number1 / 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Nanosecond' and result_to == 'Millisecond':
        calculate = number1 / 1000000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Nanosecond' and result_to == 'Second':
        calculate = number1 / 1000000000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Nanosecond' and result_to == 'Minute':
        calculate = number1 / 60000000000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Nanosecond' and result_to == 'Hour':
        calculate = number1 / 3600000000000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Nanosecond' and result_to == 'Day':
        calculate = number1 / 8.64e+13
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Nanosecond' and result_to == 'Week':
        calculate = number1 / 6.048e+14
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Nanosecond' and result_to == 'Month':
        calculate = number1 / 2.628e+15
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Nanosecond' and result_to == 'Calendar Year':
        calculate = number1 / 3.154e+16
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Nanosecond' and result_to == 'Decade':
        calculate = number1 / 3.154e+17
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Nanosecond' and result_to == 'Century':
        calculate = number1 / 3.154e+18
        result.cget('text')
        result.configure(text=(calculate, result_to))

# Microsecond Conversion
    elif result_from == 'Microsecond' and result_to == 'Nanosecond':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Microsecond' and result_to == 'Microsecond':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Microsecond' and result_to == 'Millisecond':
        calculate = number1 / 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Microsecond' and result_to == 'Second':
        calculate = number1 / 1e+6
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Microsecond' and result_to == 'Minute':
        calculate = number1 / 6e+7
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Microsecond' and result_to == 'Hour':
        calculate = number1 / 3.6e+9
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Microsecond' and result_to == 'Day':
        calculate = number1 / 8.64e+10
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Microsecond' and result_to == 'Week':
        calculate = number1 / 6.048e+11
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Microsecond' and result_to == 'Month':
        calculate = number1 / 2.628e+12
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Microsecond' and result_to == 'Calendar Year':
        calculate = number1 / 3.154e+13
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Microsecond' and result_to == 'Decade':
        calculate = number1 / 3.154e+14
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Microsecond' and result_to == 'Century':
        calculate = number1 / 3.154e+15
        result.cget('text')
        result.configure(text=(calculate, result_to))

# Millisecond Conversion
    elif result_from == 'Millisecond' and result_to == 'Nanosecond':
        calculate = number1 * 1e+6
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Millisecond' and result_to == 'Microsecond':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Millisecond' and result_to == 'Millisecond':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Millisecond' and result_to == 'Second':
        calculate = number1 / 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Millisecond' and result_to == 'Minute':
        calculate = number1 / 60000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Millisecond' and result_to == 'Hour':
        calculate = number1 / 3.6e+6
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Millisecond' and result_to == 'Day':
        calculate = number1 / 8.64e+7
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Millisecond' and result_to == 'Week':
        calculate = number1 / 6.048e+8
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Millisecond' and result_to == 'Month':
        calculate = number1 / 2.628e+9
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Millisecond' and result_to == 'Calendar Year':
        calculate = number1 / 3.154e+10
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Millisecond' and result_to == 'Decade':
        calculate = number1 / 3.154e+11
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Millisecond' and result_to == 'Century':
        calculate = number1 / 3.154e+12
        result.cget('text')
        result.configure(text=(calculate, result_to))

# Second Conversion
    elif result_from == 'Second' and result_to == 'Nanosecond':
        calculate = number1 * 1e+9
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Second' and result_to == 'Microsecond':
        calculate = number1 * 1e+6
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Second' and result_to == 'Millisecond':
        calculate = number1 * 1000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Second' and result_to == 'Second':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Second' and result_to == 'Minute':
        calculate = number1 / 60
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Second' and result_to == 'Hour':
        calculate = number1 / 3600
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Second' and result_to == 'Day':
        calculate = number1 / 86400
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Second' and result_to == 'Week':
        calculate = number1 / 604800
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Second' and result_to == 'Month':
        calculate = number1 / 2.628e+6
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Second' and result_to == 'Calendar Year':
        calculate = number1 / 3.154e+7
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Second' and result_to == 'Decade':
        calculate = number1 / 3.154e+8
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Second' and result_to == 'Century':
        calculate = number1 / 3.154e+9
        result.cget('text')
        result.configure(text=(calculate, result_to))

# Minute Conversion
    elif result_from == 'Minute' and result_to == 'Nanosecond':
        calculate = number1 * 6e+10
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Minute' and result_to == 'Microsecond':
        calculate = number1 * 6e+7
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Minute' and result_to == 'Millisecond':
        calculate = number1 * 60000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Minute' and result_to == 'Second':
        calculate = number1 * 60
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Minute' and result_to == 'Minute':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Minute' and result_to == 'Hour':
        calculate = number1 / 60
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Minute' and result_to == 'Day':
        calculate = number1 / 1440
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Minute' and result_to == 'Week':
        calculate = number1 / 10080
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Minute' and result_to == 'Month':
        calculate = number1 / 43800
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Minute' and result_to == 'Calendar Year':
        calculate = number1 / 525600
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Minute' and result_to == 'Decade':
        calculate = number1 / 5.256e+6
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Minute' and result_to == 'Century':
        calculate = number1 / 5.256e+7
        result.cget('text')
        result.configure(text=(calculate, result_to))

# Hour Conversion
    elif result_from == 'Hour' and result_to == 'Nanosecond':
        calculate = number1 * 3.6e+12
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Hour' and result_to == 'Microsecond':
        calculate = number1 * 3.6e+9
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Hour' and result_to == 'Millisecond':
        calculate = number1 * 3.6e+6
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Hour' and result_to == 'Second':
        calculate = number1 * 3600
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Hour' and result_to == 'Minute':
        calculate = number1 * 60
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Hour' and result_to == 'Hour':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Hour' and result_to == 'Day':
        calculate = number1 / 24
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Hour' and result_to == 'Week':
        calculate = number1 / 168
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Hour' and result_to == 'Month':
        calculate = number1 / 730
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Hour' and result_to == 'Calendar Year':
        calculate = number1 / 8760
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Hour' and result_to == 'Decade':
        calculate = number1 / 87600
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Hour' and result_to == 'Century':
        calculate = number1 / 876000
        result.cget('text')
        result.configure(text=(calculate, result_to))

# Day Conversion
    elif result_from == 'Day' and result_to == 'Nanosecond':
        calculate = number1 * 8.64e+13
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Day' and result_to == 'Microsecond':
        calculate = number1 * 8.64e+10
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Day' and result_to == 'Millisecond':
        calculate = number1 * 8.64e+7
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Day' and result_to == 'Second':
        calculate = number1 * 86400
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Day' and result_to == 'Minute':
        calculate = number1 * 1440
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Day' and result_to == 'Hour':
        calculate = number1 * 24
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Day' and result_to == 'Day':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Day' and result_to == 'Week':
        calculate = number1 / 7
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Day' and result_to == 'Month':
        calculate = number1 / 30.417
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Day' and result_to == 'Calendar Year':
        calculate = number1 / 365
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Day' and result_to == 'Decade':
        calculate = number1 / 3650
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Day' and result_to == 'Century':
        calculate = number1 / 36500
        result.cget('text')
        result.configure(text=(calculate, result_to))

# Week Conversion
    elif result_from == 'Week' and result_to == 'Nanosecond':
        calculate = number1 * 6.048e+14
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Week' and result_to == 'Microsecond':
        calculate = number1 * 6.048e+11
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Week' and result_to == 'Millisecond':
        calculate = number1 * 6.048e+8
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Week' and result_to == 'Second':
        calculate = number1 * 604800
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Week' and result_to == 'Minute':
        calculate = number1 * 10080
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Week' and result_to == 'Hour':
        calculate = number1 * 168
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Week' and result_to == 'Day':
        calculate = number1 * 7
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Week' and result_to == 'Week':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Week' and result_to == 'Month':
        calculate = number1 / 4.345
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Week' and result_to == 'Calendar Year':
        calculate = number1 / 52.143
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Week' and result_to == 'Decade':
        calculate = number1 / 521.4
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Week' and result_to == 'Century':
        calculate = number1 / 5214
        result.cget('text')
        result.configure(text=(calculate, result_to))

# Month Conversion
    elif result_from == 'Month' and result_to == 'Nanosecond':
        calculate = number1 * 2.628e+15
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Month' and result_to == 'Microsecond':
        calculate = number1 * 2.628e+12
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Month' and result_to == 'Millisecond':
        calculate = number1 * 2.628e+9
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Month' and result_to == 'Second':
        calculate = number1 * 2.628e+6
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Month' and result_to == 'Minute':
        calculate = number1 * 43800
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Month' and result_to == 'Hour':
        calculate = number1 * 730
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Month' and result_to == 'Day':
        calculate = number1 * 30.417
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Month' and result_to == 'Week':
        calculate = number1 * 4.345
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Month' and result_to == 'Month':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Month' and result_to == 'Calendar Year':
        calculate = number1 / 12
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Month' and result_to == 'Decade':
        calculate = number1 / 120
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Month' and result_to == 'Century':
        calculate = number1 / 1200
        result.cget('text')
        result.configure(text=(calculate, result_to))

# Calendar Year Conversion
    elif result_from == 'Calendar Year' and result_to == 'Nanosecond':
        calculate = number1 * 3.154e+16
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Calendar Year' and result_to == 'Microsecond':
        calculate = number1 * 3.154e+13
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Calendar Year' and result_to == 'Millisecond':
        calculate = number1 * 3.154e+10
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Calendar Year' and result_to == 'Second':
        calculate = number1 * 3.154e+7
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Calendar Year' and result_to == 'Minute':
        calculate = number1 * 525600
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Calendar Year' and result_to == 'Hour':
        calculate = number1 * 8760
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Calendar Year' and result_to == 'Day':
        calculate = number1 * 365
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Calendar Year' and result_to == 'Week':
        calculate = number1 * 52.143
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Calendar Year' and result_to == 'Month':
        calculate = number1 * 12
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Calendar Year' and result_to == 'Calendar Year':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Calendar Year' and result_to == 'Decade':
        calculate = number1 / 10
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Calendar Year' and result_to == 'Century':
        calculate = number1 / 100
        result.cget('text')
        result.configure(text=(calculate, result_to))

# Decade Conversion
    elif result_from == 'Decade' and result_to == 'Nanosecond':
        calculate = number1 * 3.154e+17
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Decade' and result_to == 'Microsecond':
        calculate = number1 * 3.154e+14
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Decade' and result_to == 'Millisecond':
        calculate = number1 * 3.154e+11
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Decade' and result_to == 'Second':
        calculate = number1 * 3.154e+8
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Decade' and result_to == 'Minute':
        calculate = number1 * 5.256e+6
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Decade' and result_to == 'Hour':
        calculate = number1 * 87600
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Decade' and result_to == 'Day':
        calculate = number1 * 3650
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Decade' and result_to == 'Week':
        calculate = number1 * 521.4
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Decade' and result_to == 'Month':
        calculate = number1 * 120
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Decade' and result_to == 'Calendar Year':
        calculate = number1 * 10
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Decade' and result_to == 'Decade':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Decade' and result_to == 'Century':
        calculate = number1 / 10
        result.cget('text')
        result.configure(text=(calculate, result_to))

# Century Conversion
    elif result_from == 'Century' and result_to == 'Nanosecond':
        calculate = number1 * 3.154e+18
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Century' and result_to == 'Microsecond':
        calculate = number1 * 3.154e+15
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Century' and result_to == 'Millisecond':
        calculate = number1 * 3.154e+12
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Century' and result_to == 'Second':
        calculate = number1 * 3.154e+9
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Century' and result_to == 'Minute':
        calculate = number1 * 5.256e+7
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Century' and result_to == 'Hour':
        calculate = number1 * 876000
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Century' and result_to == 'Day':
        calculate = number1 * 36500
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Century' and result_to == 'Week':
        calculate = number1 * 5214
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Century' and result_to == 'Month':
        calculate = number1 * 1200
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Century' and result_to == 'Calendar Year':
        calculate = number1 * 100
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Century' and result_to == 'Decade':
        calculate = number1 * 10
        result.cget('text')
        result.configure(text=(calculate, result_to))

    elif result_from == 'Century' and result_to == 'Century':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate, result_to))


# Creating the main title
main = tk.Label(window, text='Python Time Converter', bg='#58A4B4', fg='White')
main['font'] = font1
main.place(relx=0.5, rely=0.15, anchor='center')

# Creating the label for Entry box
label_from = tk.Label(window, text='Enter Time', bg='#58A4B4', anchor='center')
label_from['font'] = font2
label_from.place(relx=0.19, rely=0.315)

# Creating the num_from entry box
num_from = tk.Entry(window, width=32, textvariable=number_from)
num_from.place(relx=0.5, rely=0.35, anchor='center')
num_from.insert(0, int("60"))

# Creating the fromdd combo box
f = StringVar()
fromdd = ttk.Combobox(window, width=29, textvariable=f, state="readonly")
fromdd['values'] = ('Nanosecond', 'Microsecond', 'Millisecond', 'Second', 'Minute', 'Hour',
                    'Day', 'Week', 'Month', 'Calendar Year', 'Decade', 'Century')
fromdd.place(relx=0.5, rely=0.425, anchor='center')
fromdd.current()
fromdd.bind('<<ComboboxSelected>>', fromfunc)

answer = partial(answer, num_from)

# Creating the result label
to = tk.Label(window, text='Result', bg='#58A4B4')
to['font'] = font2
to.place(relx=0.24, rely=0.538)

# Creating the label where the answer will be displayed
result = tk.Label(window, text='', bg='white', width=23, anchor="w")
result['font'] = font3
result.place(relx=0.5, rely=0.57, anchor='center', height=20, width=194)

# Creating the todd combo box
t = StringVar()
todd = ttk.Combobox(window, width=29, textvariable=t, state="readonly")
todd['values'] = ('Nanosecond', 'Microsecond', 'Millisecond', 'Second', 'Minute', 'Hour',
                  'Day', 'Week', 'Month', 'Calendar Year', 'Decade', 'Century')
todd.place(relx=0.5, rely=0.645, anchor='center')
todd.current()
todd.bind('<<ComboboxSelected>>', tofunc)

# Creating the instruction label
ins = tk.Label(window, text='Choose time unit from', bg='#58A4B4', font="helvetica 8", fg='White')
ins.place(relx=0.67, rely=0.4)
# Creating the instruction label (continuation)
ins = tk.Label(window, text='the drop down list', bg='#58A4B4', font="helvetica 8", fg='White')
ins.place(relx=0.672, rely=0.44)

# Creating the instruction 2 label
ins2 = tk.Label(window, text='Choose time unit from', bg='#58A4B4', font="helvetica 8", fg='White')
ins2.place(relx=0.67, rely=0.621)
# Creating the instruction 2 label (continuation)
ins = tk.Label(window, text='the drop down list', bg='#58A4B4', font="helvetica 8", fg='White')
ins.place(relx=0.672, rely=0.66)

# Creating the get answer button
get_answer = tk.Button(window, text='Convert', bg='cyan2', command=answer, width=15, background='#1f768A', fg='White')
get_answer['font'] = font2
get_answer.place(relx='0.492', rely='0.82', anchor='center')

# Creating the mainloop
window.mainloop()
