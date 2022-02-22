import tkinter.ttk as __cached__
import tkinter as __init__
"""Credits: Used tkinter for almost the whole module lol
OPEN SOURCE NO LICENSE.
PyWin made by ByteVolx"""
window = __init__.Tk()
window.geometry('300x200')
window.title('PyWin Module')

winstate = window.resizable(False, False)

def wintitle(window_title):
    window.title(window_title)

def mainloop():
    window.mainloop()

def displaylabel(labelstr, labelrow, labelcolumn):
    label = __init__.Label(window, text=labelstr).grid(row=labelrow, column=labelcolumn)

def inputbox(inputrow, inputcolumn):
    e = __init__.Entry()
    e.grid(row=inputrow, column=inputcolumn)

def button(buttontext, buttonrow, buttoncolumn, buttoncommand):
    button = __init__.Button(window, text=buttontext, command=buttoncommand).grid(row=buttonrow, column=buttoncolumn)

def quit(optionalquitmessage):
    if optionalquitmessage == True:
        quitmessage = __init__.Tk()
        quitmessage.geometry('300x200')
        quitmessage.title('You are quitting this application')
        quitmsg = __init__.Label(quitmessage, text='You are quitting this application. Confirm please.').grid(row=1, column=1)
        quitbutton = __init__.Button(window, text='Quit', command=quitmessage.quit()).grid(row=2, column=1)

    elif optionalquitmessage == False:
        window.quit()

class call():
    class static_function():
        def newLabel(label_text: str, label_row: str, label_column: str):
            """Calls a static function"""
            print('Called static_function/label')
            newlabel = __init__.Label(window, text=label_text).grid(row=label_row, column=label_column)

        class math_functions():    
            def call_add(num1: str, num2: str, result_in_row, result_in_column):
                """Adds a number with the other.
                And the result will vary with each operation."""
                def addition():
                    return num1 + num2
                call_addition = addition()
                call_addition_label = __init__.Label(text=call_addition).grid(row=result_in_row, column=result_in_column)

            def call_sub(num1: str, num2: str, result_in_row, result_in_column):
                """Subtracts a number with the other.
                And the result will vary with each operation."""
                def subtract():
                    return num1 - num2
                call_subtraction = subtract()
                call_subtraction_label = __init__.Label(text=call_subtraction).grid(row=result_in_row, column=result_in_column)

            def call_multiply(num1: str, num2: str, result_in_row, result_in_column):
                """Multiplies a number with the other.
                And the result will vary with each operation."""
                def multiplication_res():
                    return num1 * num2
                callmultiply = multiplication_res()
                call_subtraction_label = __init__.Label(text=callmultiply).grid(row=result_in_row, column=result_in_column)
                    

                
                    
    class options():
        """These are the options for the window
        @self(KWARGS)"""
        def resizable(horizontal_resizable, vertical_resizable):
            """
            Make sure these values are boolean
            true or false.
            """
            window.resizable(horizontal_resizable, vertical_resizable)

        def window_geometry(window_geometry: str):
            """Sets the window Geometry to a certain number provided by the user.
            Type in number x number for the window geometry.
            Example: 20x50"""
            window.geometry(window_geometry)

        def window_name(window_name):
            """Sets the window name provided by the coder
            Ex. win"""
            window.title(window_name)
