#!/usr/bin/env python3
from tkinter import *
window=Tk()
window.title('BuildIT Compatibilitifier')
from webbrowser import open_new as link

_from=''
def q1_a1_c():
    q1.pack_forget()
    q1_a1.pack_forget()
    q1_a2.pack_forget()
    q1_a3.pack_forget()
    n1.pack_forget()
    a1.pack()
    a1_a1.pack()
def q1_a2_c():
    q1.pack_forget()
    q1_a1.pack_forget()
    q1_a2.pack_forget()
    q1_a3.pack_forget()
    n1.pack_forget()
    global _from
    _from='v1.2.0-v1.6.0'
    q2.pack()
    q2_a1.pack()
    #q2_a2.pack()
    q2_a3.pack()
    n1.pack()
def q1_a3_c():
    q1.pack_forget()
    q1_a1.pack_forget()
    q1_a2.pack_forget()
    q1_a3.pack_forget()
    n1.pack_forget()
    global _from
    _from='v1.7.0-v1.8.0'
    q2.pack()
    q2_a1.pack()
    q2_a2.pack()
    #q2_a3.pack()
    n1.pack()
def n1_c(typeErrorFixer):
    global link
    link('https://github.com/UxuginPython/BuildIT/releases')
q1=Label(window, text='Which version was the world created in?')
q1_a1=Button(window, text='Before v1.2.0', command=q1_a1_c)
q1_a2=Button(window, text='v1.2.0-v1.6.0', command=q1_a2_c)
q1_a3=Button(window, text='v1.7.0-v1.8.0', command=q1_a3_c)
n1=Label(window, text='''If you do not see your version of BuildIT, Compatibilitifier may be out of date.
         Check GitHub here: https://github.com/UxuginPython/BuildIT/releases''', font=('Arial', 11, ''))
n1.bind('<Button-1>', n1_c)

to=''
def q2_a1_c():
    q2.pack_forget()
    q2_a1.pack_forget()
    q2_a2.pack_forget()
    q2_a3.pack_forget()
    n1.pack_forget()
    a1.pack()
    a1_a1.pack()
def q2_a2_c():
    q2.pack_forget()
    q2_a1.pack_forget()
    q2_a2.pack_forget()
    q2_a3.pack_forget()
    n1.pack_forget()
    global to
    to='v1.2.0-v1.6.0'
    a2.pack()
    a2_a1.pack()
def q2_a3_c():
    q2.pack_forget()
    q2_a1.pack_forget()
    q2_a2.pack_forget()
    q2_a3.pack_forget()
    n1.pack_forget()
    global to
    to='v1.7.0-v1.8.0'
    a2.pack()
    a2_a1.pack()
q2=Label(window, text='Which version do you want the world to be compatible with?')
q2_a1=Button(window, text='Before v1.2.0', command=q2_a1_c)
q2_a2=Button(window, text='v1.2.0-v1.6.0', command=q2_a2_c)
q2_a3=Button(window, text='v1.7.0-v1.8.0', command=q2_a3_c)

a1=Label(window, text='Versions before v1.2.0 do not save or open worlds.')
def a1_a1_c():
    from sys import executable, argv
    from os import execl
    execl(executable, executable, *argv)
a1_a1=Button(window, text='Start Over', command=a1_a1_c)

def a2_a1_c():
    global _from, to
    file=open('world.py', 'r')
    contents=file.read()
    file.close()
    file=open('world.py', 'w')
    if _from=='v1.2.0-v1.6.0' and to=='v1.7.0-v1.8.0':
        file.write('{\'world\':'+contents+', \'world_x\':0, \'player_y\':3, \'selected\':0}')
    elif _from=='v1.7.0-v1.8.0' and to=='v1.2.0-v1.6.0':
        file.write(str(eval(contents)['world']))
    file.close()
    a2.pack_forget()
    a2_a1.pack_forget()
    done.pack()
a2=Label(window, text='Please move the world file to the same directory as Compatibilitifier.')
a2_a1=Button(window, text='Continue', command=a2_a1_c)
done=Label(window, text='Done!', fg='green', font=('Arial', 36, ''))

q1.pack()
q1_a1.pack()
q1_a2.pack()
q1_a3.pack()
n1.pack()
mainloop()
