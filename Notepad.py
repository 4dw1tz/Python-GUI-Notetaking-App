#Notetaking App
from tkinter import *   #As tkinter is the only imported framework, I imported all packages without worrying about naming collisions.
                        #This saved me from having to make a reference to the module everytime I used a tkinter function or method.

#This try and except sequence is used for error handling.
try:   #The "try" sequence checks if the relevant text file database is retrievable before running the rest of the program.
    Pad=open("notes.txt", "r")
    Pad.close()
except FileNotFoundError:   #This "except" sequence creates a NEW text file database if the "try" sequence wasn't able to retrieve a previously stored one.
    Pad=open("notes.txt", "w")
    Pad.close()
    
root=Tk()  #This line creates the main window for the graphics user interface (GUI)
root.title("Witpad")
root.geometry("500x500")  #I had to consider the possibility of the user using a smaller screen so made the window 250,000 pixels in area.
root.config(bg="light green") 

#This decryption function is used to decrypt information from the database so it can be displayed as plain text to the user.
def Decryption(Ciphertext):  #The function can be called and accepts 1 input parameter which is the ciphertext to be decrypted
    Decrypt=[]
    for cipher in Ciphertext:   #This is a Ceasar's Cipher algorithm with a shift of -1 and uses a count-controlled loop as it decrypts one chacracter at a time.
        plain=chr(ord(cipher)-1)
        Decrypt.append(plain)
    Decrypt=str(Decrypt).replace("', '", "") #The these next 4 lines are used so the output string is in the correct format.
    Decrypt=Decrypt.replace("['", "")
    Decrypt=Decrypt.replace("']", "")
    Decrypt=Decrypt.replace("[w6e", "~")
    return Decrypt   #The function outputs the plain text to be displayed to the user

#This encryption function is used to encrypt information from
def Encryption(UserPwd):   #The function has 1 input parameter which is the plaintext that is to be encrypted
    Encrypt=[]
    for plain in UserPwd:  #"plain" is a local variable used here to refer to the plaintext character in an iteration of the count-controlled loop.
        cipher=chr(ord(plain)+1)
        Encrypt.append(cipher)
    Encrypt=str(Encrypt).replace("', '", "")
    Encrypt=Encrypt.replace("['", "")
    Encrypt=Encrypt.replace("']", "")
    return Encrypt   #The function outputs the ciphertext to be written to the encrypted database.

#The "In" function is the main function that is called once a user successfully logs in.
def In(Account, line):   #Input parameters are Account(Decrypted) and the list position of the account when spilt by "~~~"
    def Logout():  #This nested function is attached to the "logout" button press event and causes the program to stop.
        exit()
    def Create():  #This nested function is attached to the "create new note" button press event.
        
        def enter(): #This nested function is attached to the "save" button press event, it saves the new note to the database.
            Edit="~"+User.get()  #This retrives the string inputted at the current time by the user in the "create note" entry box. (Fetches the new note)
            Pad1=open("notes.txt", "r", encoding="utf-8") #This loads the whole "notes" text file (database) to the RAM and reads it using the unicode character set.
            Pad=Pad1.read()
            Pad1.close()
            Pad=Pad.split("~~~") #The database is structured so that different accounts are separated by this string "~~~".
            Pad[line]=Decryption(Pad[line]) #The account of the user logged in ONLY is decrypted and no one else's using the decryption algorithm above.
            Pad[line]=Pad[line]+Edit #The new note is appended to the account.
            Pad[line]=Encryption(Pad[line]) #The account details are encrypted again using the encryption function above (with the new note).
            Pad=str(Pad).replace(", ", "~~~") #These next 7 lines modify the string so that it is in the correct format to be entered back into the database. (Data Sanitisation)
            Pad=Pad.replace("[", "")
            Pad=Pad.replace("'", "")
            Pad=Pad.replace("\n", "")
            Pad=Pad.replace("]", "")
            Pad=Pad.replace("\\\\", "\\")
            Pad=str(Pad).replace("\\x7f\\x7f\\x7f", "~~~")  #\x7f is the code given by the textfile to the encrypted "~" character.
            Pad1=open("notes.txt", "w", encoding="utf-8") #The whole database is re-written back to the "notes" text file but this time with the new note present as well.
            Pad1.write(Pad)
            Pad1.close()
            Enter.place_forget() #The "save" button widget is temporarily hidden from the window using the "place_forget" method.
            Pad=Pad.split("~~~")
            In(Decryption(Pad[line]), line) #Relaunches the "In" function incase the user wants to do more whilst logged in.
            
        Info.config(text="NEW NOTE:") #The Info label widget is edited so the text changes to "NEW NOTE" using the "config" method.
        User.config(width=75)
        User.delete(0, END)  #This line clears the entry box
        User.place(x=10, y=100) #This line places the User entry box widget visibly on the screen with the speicified x and y co-orinate parametrs using the "place" method.
        Enter=Button(root, text="Save", height=3, width=6, command=enter) #This line creates the "save" Button widget and attaches it's button press event to call "enter" function above. 
        Enter.place(x=225, y=200)
        
    def Expand(Note, Num): #This function accepts 2 input parameters 1)the note 2)position of the note in the "Acc" array. (Look below). This displays each individual note.
        def Edit():  #This function is attached to the "Edit Note" button press event and allows the user to edit an old note without havig to delete it and create a new note.
            def Save(): #This save function replaces the old note with the edited version of it in the database. Works in the same way as the "enter" nested function above ^.
                Edit=Editor.get()
                Pad1=open("notes.txt", "r", encoding="utf-8")
                Pad=Pad1.read()
                Pad1.close()
                Pad=Pad.split("~~~")
                Pad[line]=Decryption(Pad[line])
                Pad[line]=Pad[line].split("~")
                Temp=Pad[line].copy() #When an array is given a new name, the new name and the old name equate to the same array so you can't change the value of 1 without affecting the other.
                Temp[Num+1]=Edit      #So I used the "copy" function which creates a whole new array under the new name and the 2 names do NOT equate to the same array anymore.
                Pad[line]=Temp
                Pad[line]=str(Pad[line]).replace(", ", "~") #All these ".replace" lines just modify the string so that it is in the correct format to be written to the database.
                Pad[line]=Pad[line].replace("'", "")
                Pad[line]=Pad[line].replace("[", "")
                Pad[line]=Pad[line].replace("]", "")
                Pad[line]=Encryption(Pad[line])
                Pad=str(Pad).replace(", ", "~~~")
                Pad=Pad.replace("'", "")
                Pad=Pad.replace("[", "")
                Pad=Pad.replace("]", "")
                Pad=Pad.replace("\\\\", "\\")
                Pad1=open("notes.txt", "w", encoding="utf-8")
                Pad1.write(Pad)
                Pad1.close()
                save.destroy() #The following buttons are deleted (not just hidden) using the "destroy" function as they are no longer required.
                Inform.destroy()
                Editor.destroy()
                Note=Edit
                NOTE.config(text=Note)
                NOTE.pack() #In the "sticky note" windows, everything is placed there using the "pack" method which requires no parameters so widgets can move according to note size and window size 
                EdBut.pack()
                DelBut.pack()
            Full.geometry("500x400") #When editing the note I have increased the window size of the individual window from 400x400 to 500x400 to allow the user more writing space.
            NOTE.pack_forget()
            EdBut.pack_forget()
            DelBut.pack_forget()
            Inform=Label(Full, text="Edit your Note Below:", font="ArielBold 15") #This clearly informs the user what they need to do to edit a note.
            Inform.pack()
            Editor=Entry(Full, width=75) #This makes sure that the entry box is pretty wide so the user can usually see their full note on screen at any given point of time
            Editor.insert(0, Note)  #This line puts the old note into the entry box so the user can just make edits rather than having to copy and paste the note into there or type up again.
            Editor.pack()
            save=Button(Full, text="SAVE", height=3, width=10, command=Save)
            save.pack()
        def Delete():  #This nested function runs when the "Delete Note" button pressed event occurs and asks the user if they are sure they want to delete the note incase of accidental presses.
            def Yes():  #This function runs when the "Yes" button pressed event occurs and deletes the note permanently from the database. It works in a similar way to the "enter" function above,
                        #however this function removes a note rather than adding one.
                Pad1=open("notes.txt", "r", encoding="utf-8")
                Pad=Pad1.read()
                Pad1.close()
                Pad=Pad.split("~~~")
                Pad[line]=Decryption(Pad[line])
                Pad[line]=Pad[line].split("~")
                Pad[line].pop(Num+1) #The "pop" method can be used to remove an element from an array specified. The input parameter specifies which position from the list should be removed.
                Pad[line]=str(Pad[line]).replace(", ", "~")
                Pad[line]=Pad[line].replace("'", "")
                Pad[line]=Pad[line].replace("[", "")
                Pad[line]=Pad[line].replace("]", "")
                Pad[line]=Encryption(Pad[line])
                Pad=str(Pad).replace(", ", "~~~")
                Pad=Pad.replace("'", "")
                Pad=Pad.replace("[", "")
                Pad=Pad.replace("]", "")
                Pad=Pad.replace("\\\\", "\\")
                Pad1=open("notes.txt", "w", encoding="utf-8")
                Pad1.write(Pad)
                Pad1.close()
                Full.destroy() #This destroys/ removes the whole window that that individual sticky note was in.
            def No(): #This nested function runs when the "No" button pressed event occurs and cancels stops the "Delete" function and takes the user back to the previous window layout
                Sure.destroy()
                yes.destroy()
                no.destroy()
                NOTE.pack()
                EdBut.pack()
                DelBut.pack()
            NOTE.pack_forget()
            DelBut.pack_forget()
            EdBut.pack_forget()
            Sure=Label(Full, text="ARE YOU SURE YOU WANT TO DELETE THIS NOTE?", font="15") #This label widget is created which asks the user to confirm if they want to delete the note or not.
            Sure.pack()
            yes=Button(Full, text="YES", command=Yes) #These new buttons are created and placed on the window and execute different commands depending on what's pressed (look above for functions).
            yes.pack()
            no=Button(Full, text="NO", command=No)
            no.pack()
            
        Full=Tk()
        Full.title("STICKY NOTE "+str(Num)) #This gives each individual note window it's own title and note number to make it easier for the user to count and identify notes.
        Full.geometry("400x400")
        NOTE=Label(Full, text=Note)
        NOTE.pack()
        EdBut=Button(Full, text="Edit Note", height=3, width=10, command=Edit) #This edit button pressed event causes the "Edit" function to execute
        EdBut.pack()
        DelBut=Button(Full, text="Delete Note", height=3, width=10, command=Delete) #This delete button pressed event causes the "Delete" function to execute
        DelBut.pack()
        
    Account=str(Account).replace("\n", "") #This makes sure there are no new line characters in the input parameter which could misalign notes from positions.
    Account=Account.split("~")
    Main.config(text="Welcome "+Account[0], font="ArielBold 25")
    Main.place(x=0, y=0)
    #DISPLAY NOTES
    Log.place_forget()  #The next lines involves a lot of widgets being hidden and created as its supposed to be like a new tab to the user as they have just logged in.
    Sign.place_forget()
    User.place_forget()
    PWD.place_forget()
    Info1.place_forget()
    Info2.place_forget()
    CreateBut=Button(root, text="Create New Note", height=5, width=15, command=Create) #When this button is pressed, the "Create" function above executues
    CreateBut.place(x=350, y=350)
    Info.config(text="Sticky Notes:", bg="light green", font="ArielBold 12")
    Info.place(x=225, y=50)
    logout=Button(root, text="Logout", height=5, width=15, command=Logout)
    logout.place(x=150, y=350)
    if len(Account) < 3:  #This checks if the user has any notes in their account at all by checking if the length of the array is >3 or not as notes come after Username and PWD.
        Info.config(text="You don't seem to have any notes yet!")
    else:
        Acc=Account[2:len(Account)] #This removes the first 2 elements (username and password) from the new array as we don't want them to show up as notes on screen!
        Odd=0
        for i in Acc:
            i=Button(root, text=Acc[Odd], width=30, command=Expand(Acc[Odd], Odd+1)) #Each element (Note) is run through the expand function above which diplays them on separate windows.
            Odd=Odd+1

#This Signup function is attched to the "Register" button pressed event and takes the user through the process of creating a new account and then logging them in automatically.
def Signup():
    Main.place(x=200, y=0)
    def enter(): #This function runs when the "Enter" button pressed event occurs and runs checks on the data provided by the user before creating them a new account.
        Pad1=open("notes.txt", "r", encoding="utf-8")
        Pad=Pad1.read()
        Pad1.close()
        Encrypt=Encryption(User.get()+"~"+PWD.get())
        if len(PWD.get()) < 8:  #This length check ensures that 1)The entery box hasn't been left blank; 2)The password is of a decent strength (8 characyers long at least)
            Main.config(text="Your password needs to atleast be 8 characters long!", font="ArielBold 15")
            Main.place(x=0, y=0)
        elif len(User.get()) < 1: #This length check ensures that the entry box hasn't been left blank.
            Main.config(text="You forgot to enter a Username!", font="ArielBold 15")
            Main.place(x=0, y=0)
        elif "~" in User.get() or "~" in PWD.get(): #This charcter check ensures that the user hasn't entered the split character as this will confuse the database.
            Main.config(text="You cannot use this character '~'.", font="ArielBold 15")
            Main.place(x=0, y=0)
        elif Encrypt in Pad: #This check is there to make sure that that specific username and password hasn't been used before as this could result in a mix-up of notes.
            Main.config(text="Username already in use")
            Main.place(x=0, y=0)
        else:   #If all the checks show the data is fine, it is encrypted and appended to the notes.txt file database.
            Pad=open("notes.txt", "a", encoding="utf-8")
            Pad.write("~~~")
            Pad.write(Encrypt)
            Pad.close()
            Pad1=open("notes.txt", "r", encoding="utf-8")
            Pad=Pad1.read()
            Pad=Pad.split("~~~")
            Pad1.close()
            Enter.destroy()
            In(Decryption(Pad[-1]), len(Pad)-1) #This runs the "In" function and passes the account and position of account in the database to that function.
            
    Log.place(x=400, y=400)
    Sign.place_forget()
    Main.config(text="Create New Account!")
    Info1.place(x=150, y=50)
    Info2.place(x=150, y=100)
    User.place(x=225, y=50)
    PWD.place(x=225, y=100)
    Enter.config(command=enter)
    Enter.place(x=225, y=150)

#This "Login" function is attached to the "Login" button pressed event and asks the user to input thir username and password to check if their account exists and may log them in.
def Login():
    Main.config(font="ArielBold 25")
    Main.place(x=200, y=0)
    def enter():
        Encrypt=User.get()+"~"+PWD.get()
        Pad1=open("notes.txt", "r", encoding="utf-8")
        Pad=Pad1.read()
        Pad=Pad.split("~~~") #The array "Pad" is a list of accounts
        Pad1.close()
        Found=False #The value Found is set to be False until a the user enters a correct username and password.
        nom=-1
        for line in Pad: #line is one of the elements in Pad so is an individual account.
                         #This for loop iterates through the Pad array testing each account if it matches the details user has entered.
            nom+=1
            line=Decryption(line)
            line=line.split("~") #line is now a list of the username, password and notes within an account
            line=line[0:2] #This narrows "line" down to the first 2 elements of the account which would be the username and passowrd in the database
            line=str(line).replace("[", "")
            line=line.replace("]", "")
            line=line.replace("'", "")
            line=line.replace(", ", "~")
            if Encrypt == line: #It then compares the encrypted version of the username and password the user has enetered to see if it matches any values of "line" (look above)
                Found=True
                Main.config(text="Logged In!", font="ArielBold 25") #The logged in message is clearly broadcasteds so the user knows if they have successfully logged in.
                Main.place(x=200, y=0)
                Enter.destroy()
                In(Decryption(Pad[nom]), nom) #The "Login" function now calls the "In" functtion to take over from here and gives it the account and account position in the database.
        if Found==False:   #If the there was no match found for what the user has entered, they are told this clearly from the header. (look below)
            Main.config(text="Username or Password Entered Incorrectly!", font="ArielBold 15") #The "Register" button is clickable in the corner incase the user realizes they don't have an account yet.
            Main.place(x=100, y=0)
    Log.place_forget()
    Sign.place(x=400, y=400)
    Main.config(text="Login!")
    Info1.place(x=150, y=50)
    Info2.place(x=150, y=100)
    User.place(x=225, y=50)
    PWD.place(x=225, y=100)
    Enter.config(command=enter)
    Enter.place(x=225, y=150)
    
#All the widgets that are used in more than one function are created here so they are global variables.
Main=Label(root, text="Welcome", font="ArielBold 25", bg="light green") #This label widget is the main "header" of the window throughout the program.
Main.place(x=200, y=0)
Log=Button(root, text="Login", activebackground="grey", height=2, width=10, command=Login)
Sign=Button(root, text="Register", activebackground="grey", height=2, width=10, command=Signup)
Sign.place(x=225, y=100)
Log.place(x=225, y=50)
User=Entry(root)
PWD=Entry(root, show="*") #This makes sure that as characters are being inputted into the password entry box, they show up on screen as "*" to prevent shoulder surfing (hacking).
Info1=Label(root, text="Username:")
Info2=Label(root, text="Password:")
Info=Label(root)
Enter=Button(root, text="Enter")

#The main event loop for the "root" window.
root.mainloop()


#Emphasize on: encryption (solves security issue), front end GUI, backend database, error handling, functions, nested functions, data sanitisation (including checks), a realistic interface (UX)
#Make a success criteria
#Explain the basic core concept of the code in English.
#Say why I used for loops instead of while loops so they know I can use it and give an example of what it may have looked like (eg from the encryption function)
#What tkinter is and why I used it.
#Define every technical term used for communication marks.
#LEARNT: When an array in Python is given another name, the same array can be referred to by 2 names and changes in one name thus change the array in the other name so I had to use the .copy function.
#Mention How the Database has been structured.
#Failure: Complex encryption algorithm included characters that weren't supported by Notepad
#The string "~Wasssup man! ~ Nah bro ~ DUDE" became this "\x9cóŔǇȺʭ̢ΒβПҀӮԏԯ֭\u05cd؛ټۤ܄ݦߘࡇࡧࣥअॉঞৢਧ מ" when encrypted
#The ciphertext in notepad included character codes for characters it didn't support like "~" became "\x9"
#All character codes start with a "\" and this disaligned the string lengths which the encryption algorithm relied upon.
#SOLUTION: I had to switch to a simpler encryption algorithm that didn't use charcters beyond English.
#Failure: No scrollbar so people may not be able to see all their notes on a small screen.
#SOLUTION: Make notes pop up on separate Windows
