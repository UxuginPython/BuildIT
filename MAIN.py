#!/usr/bin/env python3
#1.8.0 Unfinished
try:
    from tkinter import *
    import tkinter.ttk as ttk
except:
    from Tkinter import *
    import ttk
window=Tk()
window.title('BuildIT')

def setup():
    global window
    progressbar=ttk.Progressbar(window, orient=HORIZONTAL, length=250, mode='determinate')
    percent=Label(window, text='0%')
    command=Label(window, text='', font=('Arial', 10, ''))
    progressbar.grid(column=0, row=1)
    percent.grid(column=0, row=0)
    command.grid(column=0, row=2)
    window.update()
    window.update_idletasks()
    def updateLoadingScreen(progress, _command):
        #global progressbar, command, percent, window
        progressbar['value']=progress*250
        percent.config(text=str(int(progress*100))+'%')
        command.config(text=_command)
        window.update()
        window.update_idletasks()
    
    updateLoadingScreen(0, 'global selected, tiles, tiles_placeable, tiles_solid, colors, change, world, world_x, player_x, player_y, left, right, up, down, onClick, gui, updateGui, save, _open')
    global selected, tiles, tiles_placeable, tiles_solid, colors, change, world, world_x, player_x, player_y, left, right, up, down, onClick, gui, updateGui, save, _open
    updateLoadingScreen(1/27, 'selected=0')
    selected=0
    updateLoadingScreen(2/27, 'tiles=[\'air\', \'grass\', \'dirt\', \'stone\']')
    tiles=['air', 'grass', 'dirt', 'stone']
    updateLoadingScreen(3/27, 'tiles_placeable=[\'grass\', \'dirt\', \'stone\']')
    tiles_placeable=['grass', 'dirt', 'stone']
    updateLoadingScreen(4/27, 'tiles_solid=[\'grass\', \'dirt\', \'stone\']')
    tiles_solid=['grass', 'dirt', 'stone']
    updateLoadingScreen(5/27, 'colors={')
    colors={
        'air':'aqua',
        'grass':'lime',
        'dirt':'saddlebrown',
        'stone':'silver'}
    
    #from time import sleep
    #sleep(5)
    
    updateLoadingScreen(6/27, 'def change(typeErrorFixer):')
    def change(typeErrorFixer): #I got "TypeError: change() takes 0 positional arguments but 1 was given", so I added that argument and it fixed it
        global selected
        selected+=1
        selected=selected%len(tiles_placeable) #Modulo
    updateLoadingScreen(7/27, 'window.bind(\'<c>\')')
    window.bind('<c>', change)
    updateLoadingScreen(8/27, 'world=[]')
    
    world=[]
    updateLoadingScreen(9/27, 'world_x=0')
    #for x in range(0, 15):
    #    column=[]
    #    for y in range(0, 10):
    #        if y<4:
    #            column.append('air')
    #        elif y==4:
    #            column.append('grass')
    #        elif y==5:
    #            column.append('dirt')
    #        else:
    #            column.append('stone')
    #    world.append(column)
    
    world_x=0
    updateLoadingScreen(10/27, 'player_x=7')
    player_x=7
    updateLoadingScreen(11/27, 'player_y=3')
    player_y=3
    updateLoadingScreen(12/27, 'def left(typeErrorFixer):')
    def left(typeErrorFixer):
        global world, world_x, player_x, player_y
        if world_x>0:
            if world[world_x+player_x-1][player_y] not in tiles_solid: #So glad I learned about the 'in' keyword (or is it an operator?)
                world_x-=1
    updateLoadingScreen(13/27, 'window.bind(\'<Left>\')')
    window.bind('<Left>', left)
    updateLoadingScreen(14/27, 'def right(typeErrorFixer):')
    def right(typeErrorFixer):
        global world, world_x, player_x, player_y
        if world[world_x+player_x+1][player_y] not in tiles_solid:
            world_x+=1
    updateLoadingScreen(15/27, 'window.bind(\'<Right>\', right)')
    window.bind('<Right>', right)
    updateLoadingScreen(16/27, 'def up(typeErrorFixer):')
    def up(typeErrorFixer):
        global world, world_x, player_x, player_y
        if player_y>0:
            if world[world_x+player_x][player_y-1] not in tiles_solid:
                player_y-=1
    updateLoadingScreen(17/27, 'window.bind(\'<Up>\', up)')
    window.bind('<Up>', up)
    updateLoadingScreen(18/27, 'def down(typeErrorFixer):')
    def down(typeErrorFixer):
        global world, world_x, player_x, player_y
        if player_y<10:
            if world[world_x+player_x][player_y+1] not in tiles_solid:
                player_y+=1
    updateLoadingScreen(19/27, 'window.bind(\'<Down>\', down)')
    window.bind('<Down>', down)
    updateLoadingScreen(20/27, 'def onClick(event):')
    
    def onClick(event):
        global world_x, player_x, player_y
        tile=event.widget
        column=int(tile.grid_info()['column'])
        column+=world_x
        row=int(tile.grid_info()['row'])
        #print('Column: '+str(column))
        #print('Row: '+str(row))
        if not(column==player_x+world_x and row==player_y):
            if world[column][row]=='air':
                world[column][row]=tiles_placeable[selected]
            else:
                world[column][row]='air'
    updateLoadingScreen(21/27, 'gui=[]')
    
    gui=[]
    updateLoadingScreen(22/27, 'for l in range(0, 15):')
    for x in range(0, 15):
        column=[]
        for y in range(0, 10):
            label=Label(window, text='    ')
            #label.config(bg=colors[world[x][y]])
            label.bind('<Button-1>', onClick)
            column.append(label)
        gui.append(column)
    updateLoadingScreen(23/27, 'def UpdateGui():')
    
    def updateGui():
        global world_x
        for x in range(0, 15):
            for y in range(0, 10):
                if x==player_x and y==player_y:
                    gui[x][y].config(bg='red')
                elif x==0 and y==0:
                    gui[x][y].config(bg=colors[tiles_placeable[selected]])
                else:
                    try:
                        gui[x][y].config(bg=colors[world[x+world_x][y]])
                    except IndexError:
                        column=[]
                        for y in range(0, 10):
                            if y<4:
                                column.append('air')
                            elif y==4:
                                column.append('grass')
                            elif y==5:
                                column.append('dirt')
                            else:
                                column.append('stone')
                                world.append(column)
                                
                                #for y in range(0, 10):
                                    #    label=Label(window, text='    ')
                                    #    label.config(bg=colors[world[x][y]])
                                    #    label.bind('<Button-1>', onClick)
                                    #    column.append(label)
                                    #gui.append(column)
    updateLoadingScreen(24/27, 'def save():')
    def save():
        file=open('world.py', 'w')
        file.write('{\'world\':'+str(world)+', \'world_x\':'+str(world_x)+', \'player_y\':'+str(player_y)+', \'selected\':'+str(selected)+'}')
        file.close()
    updateLoadingScreen(25/27, 'def _open():')
    def _open():
        global world, world_x, player_y, selected
        file=open('world.py', 'r')
        data=eval(file.read())
        world=data['world']
        world_x=data['world_x']
        player_y=data['player_y']
        selected=data['selected']
        file.close()
    updateLoadingScreen(26/27, '_open()')
    _open() #Replaces lines 23-34
    updateLoadingScreen(27/27, '')
    
    #from time import sleep
    #sleep(5)
    
    percent.grid_forget()
    progressbar.grid_forget()
    command.grid_forget()
    for x in range(0, 15):
        for y in range(0, 10):
            gui[x][y].grid(column=x, row=y)
#import threading
#_setup=threading.Thread(target=setup)
#_setup.start()
#_setup.join()

count=0
while True:
    window.update()
    window.update_idletasks()
    if count==0:
        setup()
    updateGui()
    save()
    count+=1
