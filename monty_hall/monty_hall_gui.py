import random
import tkinter as tk

class Game(tk.Frame):
    """GUI app"""
    doors = ('a', 'b', 'c')
#OOP inheritence
    def __int__(self, parent):
        """Initialize frame"""
        super(Game, self).__init__(parent) #parent is root window
        self.parent = parent
        self.img_file = 'closed_doors.png' #current image of doors
        self.choice = '' #players door choice
        self.winner = '' #winning door
        self.reveal = '' #revealed goat door
        self.first_choice_wins = 0 #stats counter
        self.pick_change_wins = 0 #stats counter
        self.create_widgets

    def create_widgets(self):
        """create label, button, and text widgets for game"""
        img = tk.PhotoImage(file='abc.png')
        self.photo_lbl = tk.Label(self.parent, image=img, text='', borderwidth=0)
        self.photo_lbl.grid(row=0, column=0, columnspan=10, sticky='W')
        self.photo_lbl.image = img
        #create instruction label
        instru_input = [
            ('Behind one door is a car!', 1, 0, 5, 'W'),
            ('Behind the others is a goat!', 2, 0, 5, 'W'),
            ('Pick a door:', 1, 3, 1, 'E')
            ]
        for tex, row, column, columnspan, sticky in instru_input:
            instr_lbl = tk.Label(self.parent, text=text)
            instr_lbl.grid(row=row, column=column, columnspan=columnspan, sticky=sticky, ipadx=30)

    # create radio buttons for getting initial user choice
        self.door_choice = tk.StringVar()
        self.door_choice.set(None)
        a = tk.Radiobutton(self.parent, text='A', variable=self.door_choice, value='a', command=self.win_reveal)
        b = tk.Radiobutton(self.parent, text='B', variable=self.door_choice, value='b', command=self.win_reveal)
        c = tk.Radiobutton(self.parent, text='C', variable=self.door_choice, value='c', command=self.win_reveal)
        #create widgets for changing door choice
        self.change_door = tk.StringVar()
        self.change_door.set(None)

        instr_lbl = tk.Label(self.parent, text='Change doors?')
        instr_lbl.grid(row=2, column=3, columnspan=1, sticky='E')

        self.yes = tk.Radiobutton(self.parent, state='disable', text='Y', variable=self.change_door,
                                  value='y', command=self.show_final)
        self.no = tk.Radiobutton(self.parent, state='disable', text='N', variable=self.change_door,
                                 value='n', command=self.show_final)
        #create text widgets for win statistics
        defaultbg = self.parent.cget('bg')
        self.unchanged_wins_txt = tk.Text(self.parent, width=20, height=1, wrap=tk.WORD, bg=defaultbg,
                                          fg='black', borderwidth=0)
        self.changed_wins_txt = tk.Text(self.parent, width=20, height=1, wrap=tk.WORD, bg=defaultbg,
                                        fg='black', borderwidth=0)
        # place the widgets in the frame
        a.grid(row=1, column=4, sticky='W', padx=20)
        b.grid(row=1, column=4, sticky='N', padx=20)
        c.grid(row=1, column=4, sticky='E', padx=20)
        self.yes.grid(row=2, column=4, sticky='W', padx=20)
        self.no.grid(row=2, column=4, sticky='N', padx=20)
        self.unchanged_wins_txt.grid(row=1, column=5, columnspan=5)
        self.changed_wins_txt.grid(row=2, column=5, columnspan=5)

        def show_final(self):
            """Reveal image behind user's final door choice and count wins"""
            door_list = list(self.doors)
            switch_doors = self.change_door.get()

            if switch_doors == 'y':
                door_list.remove(self.choice)
                door_list.remove(self.reveal)
                new_pick = door_list[0]
                if new_pick == self.winner:
                    self.img_file = 'car_door.png'.format(new_pick)
                    self.pick_change_wins += 1
                else:
                    self.img_file = 'goat_door.png'.format(new_pick)
                    self.first_choice_wins += 1
            elif switch_doors == 'n':
                if self.choice == self.winner:
                    self.img_file = 'car_door.png'.format(self.choice)
                    self.first_choice_wins += 1
                else:
                    self.img_file = 'goat_door.png'.format(self.choice)
                    self.pick_change_wins += 1

                #update door image
            self.update_image()

            #update displayed stats
            self.unchagned_wins_txt.delete(1.0, 'end')
            self.unchanged_wins_txt.insert(1.0, 'Unchanged wins = {:d}'.format(self.first_choice_wins))
            self.changed_wins_txt.delete(1.0, 'end')
            self.changed_wins_txt.insert(1.0, 'Changed wins = {:d}'.format(self.pick_change_wins))
            # turn off yes/no buttons and clear door choice buttons
            self.yes.config(state='disabled')
            self.no.config(state='disabled')
            self.door_choice.set(None)
            # close doors 2 seconds after opening
            self.img_file = 'all_closed.png'
            self.parent.after(2000, self.update_image)

            #set up root window and run event loop
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Monty Hall Problem')
    root.geometry('1280x820')
    game = Game(root)
    root.mainloop()

