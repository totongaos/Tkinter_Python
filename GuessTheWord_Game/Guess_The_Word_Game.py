from tkinter import *
from random import choice


def start():
    BT_start.destroy()
    lb0.destroy()
    global lb_inning, lb_question, BT_quit, BT_guess,innings
    lb_inning = Label(windown, text=f'Inning: {innings}',
                      bg='#888DF2', fg='#FFFFD8', font='Times 14 bold')
    lb_inning.grid(row=0, column=0, pady=10, padx=10)

    lb_question = Label(windown, text='Choose \'Quit\' or \'Guess\': ',
                      bg='#888DF2', fg='#FFFFD8', font='Times 14 bold')
    lb_question.grid(row=0, column=1, pady=10, padx=10)

    BT_quit = Button(windown, text='Quit',font='Times 14 bold', command=BT_Quit)
    BT_quit.grid(row=0, column=4, pady=10, padx=10)

    BT_guess = Button(windown, text='Guess',font='Times 14 bold', command=def_step1)
    BT_guess.grid(row=0, column=5, pady=10, padx=10)

def def_step1(): #sử dụng entry
    lb_question.destroy()
    BT_guess.destroy()
    BT_quit.destroy()
    global entry,word,encode_display,word_display,lb_step1,BT_done,words

    word = choice(words) #choice 1 chữ trong data
    encode_display = [" _"] * len(word) #chuyển text sang kí tự ' _'
    word_display = "".join(encode_display) #join kí tự ' _' vào mảng

    lb_step1 = Label(windown, text=f"Word to guess: {word_display}",
                      bg='#042444', fg='#FFFFD8', font='Times 30 bold')
    lb_step1.place(relx=0.5, rely=0.3, anchor=S)

    entry = Entry(windown, width=10, font='Times 14')
    entry.place(relx=0.2, rely=0.4,anchor=W)
    entry.focus()

    BT_done = Button(windown, text='Done', command=def_done)
    BT_done.place(relx=0.4, rely=0.4, anchor=W)

def def_done():
    global word_display, innings,  lb_er, lb_inning,entry,lb_Wrong,lb_Win,user_guess,BT_quit1,hide_win,BT_quit1,hide_lb_error,word ,lb_YouGuess
    user_guess = str(entry.get())

    if len(user_guess) > 1: #nếu số lượng từ nhiều hơn 1
        if user_guess!= word: # nếu nhập nhiều từ mà sai sẽ wrong -1
            innings -= 1
            entry.delete(0, END)
            if hide_win == False: # fix bug nếu nhập sai 1 kí tự trước
                lb_Wrong.destroy()
            elif hide_lb_error == False:  # đang fix-bug nếu nhập nhieu ki tự lần đầu
                lb_YouGuess.destroy()
                lb_YouGuess = Label(windown, text=f'You guess: {user_guess}')
                lb_er.destroy()
                lb_er = Label(windown, text=f'Số lượng từ không hợp lệ. You have {innings} innings', bg='#042444',
                              fg='#FFFFD8', font='Times 12 italic bold')

            lb_YouGuess = Label(windown, text=f'You guess: {user_guess}')
            lb_YouGuess.place(relx=0.2, rely=0.5, anchor=W)

            lb_er = Label(windown, text=f'Số lượng từ không hợp lệ. You have {innings} innings', bg='#042444',
                          fg='#FFFFD8', font='Times 12 italic bold')
            lb_er.place(relx=0.2, rely=0.6, anchor=W)

            lb_inning.config(text=f'Inning: {innings}',
                             bg='#888DF2', fg='#FFFFD8', font='Times 14 bold')
            hide_lb_error = False
            if innings == 0:
                hide_win = False
                def_innings0()
        elif user_guess == word: #nếu nhập nhiều từ mà đúng sẽ win
            if hide_win == False: #fix BUG5
                lb_Wrong.destroy() #fix BUG2
            hide_win = True
            def_win()

    elif user_guess not in word:
        innings -= 1
        entry.delete(0, END)
        # hide_lb_error = False
        if hide_lb_error == False: # đang fix-bug nếu nhập nhieu ki tự
            lb_YouGuess.destroy()
            lb_er.destroy()
            lb_Wrong = Label(windown, text=f"Wrong, you lose -1 round. You have {innings} innings",
                             bg='#042444', fg='#FFFFD8', font='Times 18 bold')
            hide_win = False
        elif hide_win == False: # fix bug nếu nhập sai 1 kí tự trước
            lb_Wrong.destroy()
            lb_Wrong = Label(windown, text=f"Wrong, you lose -1 round. You have {innings} innings",
                             bg='#042444', fg='#FFFFD8', font='Times 18 bold')

        lb_inning.config(text=f'Inning: {innings}',
                         bg='#888DF2', fg='#FFFFD8', font='Times 14 bold')
        lb_Wrong = Label(windown, text=f"Wrong, you lose -1 round. You have {innings} innings",
                       bg='#042444', fg='#FFFFD8', font='Times 18 bold')
        lb_Wrong.place(relx=0.04, rely=0.7, anchor=W)
        hide_win = False
        if innings == 0:
            lb_Wrong.destroy()
            entry.destroy()
            BT_done.destroy()
            BT_quit1 = Button(windown, text='Quit', font='Times 14 bold', command=Lose)
            BT_quit1.grid(row=0, column=4, pady=10, padx=10)


    elif user_guess in word:  # check user's guess word
        for i in range(len(word)):
            if word[i] == user_guess:
                encode_display[i] = user_guess
                word_display = "".join(encode_display)
                entry.delete(0,END)

                lb_step1.config(text=f"Word to guess: {word_display}",
                                 bg='#042444', fg='#FFFFD8', font='Times 30 bold')
                if word_display == word: #win
                    hide_win = True
                    def_win()

        if hide_win == False: #fix BUG6
            lb_Wrong.destroy()
        if hide_lb_error == False: #fix BUG7
            lb_er.destroy()
            lb_YouGuess.destroy()

def def_win():
    global word_display,word,words
    lb_Win = Label(windown, text=f"Win. You have {innings}",
                   bg='#042444', fg='#FFFFD8', font='Times 20 bold')
    lb_Win.place(relx=0.2, rely=0.7, anchor=W)
    if hide_lb_error == False: # đang fix-bug nếu nhập nhieu ki tự
        lb_YouGuess.destroy()
        lb_er.destroy()

    windown.after(2000,lambda : lb_Win.destroy())
    windown.after(2000, lambda: lb_step1.destroy())
    windown.after(2000, lambda: BT_done.destroy())
    windown.after(2000, lambda: entry.destroy())
    windown.after(2000, lambda: def_step1())
    windown.after(2000,lambda : choice(words))

def def_innings0():
    global BT_quit1,entry,BT_done,lb_YouGuess
    print('innings1',innings)
    entry.destroy()
    BT_done.destroy()
    BT_quit1 = Button(windown, text='Quit', font='Times 14 bold', command=Lose)
    BT_quit1.grid(row=0, column=4, pady=10, padx=10)

def Lose():
    if hide_lb_error == False: # đang fix-bug nếu nhập nhieu ki tự
        lb_YouGuess.destroy()
        lb_er.destroy()
    elif hide_lb_error == True: # fix bug nếu nhập sai 1 kí tự trước
        lb_Wrong.destroy()
    BT_done.destroy()
    lb_step1.destroy()
    lb_inning.destroy()

    lb_Quit = Label(windown, text='Thank you for playing',
                    bg='#042444', fg='#FFFFD8', font='Times 20 bold')
    lb_Quit.place(relx=0.5, rely=0.5, anchor=CENTER)
    BT_quit1.destroy()
    windown.after(1500, lambda: windown.destroy())

def BT_Quit():
    lb_inning.destroy()
    lb_question.destroy()
    BT_guess.destroy()
    BT_quit.destroy()

    lb_Quit = Label(windown, text='Thank you for playing',
                      bg='#042444', fg='#FFFFD8',
                      font='Times 20 bold')
    lb_Quit.place(relx=0.5, rely=0.5, anchor=CENTER)
    windown.after(1500,lambda: windown.destroy())


if __name__ == '__main__':
    # khai bao bien
    words = ["hello", "love", "yes", "us"]
    word_display = []
    innings = 3  # luot choi
    # Khai bao frame
    windown = Tk()
    srcW = windown.winfo_screenwidth() - 1000
    srcH = windown.winfo_screenheight() - 500
    windown.geometry(f'{srcW}x{srcH}')
    windown.title('Guess The Word')
    windown.iconbitmap('D:\Learn python\Tkinter_Python\GuessTheWord_Game\img\mushroom (2).ico')
    windown.config(bg="#042444")
    windown.attributes('-topmost', True)  # màn hình game luôn hiển thị top

    hide_win = True
    hide_lb_error = True

    lb0 = Label(windown, text='Guess The Word',
                bg='#042444', fg='#FFFFD8', font='Times 35 bold')
    lb0.place(relx=0.5, rely=0.5, anchor=S)

    BT_start = Button(windown, text='Start',
                      font='Times 18 bold', width=10, height=1, command=start)
    BT_start.place(relx=0.5, rely=0.9, anchor=S)

    windown.mainloop()

