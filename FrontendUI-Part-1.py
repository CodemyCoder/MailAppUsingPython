from tkinter import *


golden = "#fa0"
pink = "#f08"
yellow = "#ffc400"
orange = "#ff5100"
green = "#0c3"
purple = "#cc00c2"
blue = "#006eff"
red = "#f00"
white = "#fff"
black = "#000"
bg = white

def wayToPage1():
    framePage2.pack_forget()
    framePage3.pack_forget()
    framePage1.pack(expand=1, fill=BOTH, padx=5, ipadx=5, ipady=5)

def wayToPage2():
    framePage1.pack_forget()
    framePage3.pack_forget()
    framePage2.pack(expand=1, fill=BOTH, padx=5, ipadx=5, ipady=5)

def wayToPage3():
    framePage1.pack_forget()
    framePage2.pack_forget()
    framePage3.pack(expand=1, fill=BOTH, padx=5, ipadx=5, ipady=5)


# mainWindow
window = Tk()
window.title("Python Mail App")
window.geometry("1200x700")
window.minsize(1200, 700)

# header
headerFrame = Frame(window, bg=bg, bd=0)
headerFrame.pack(fill=X, padx=5)

themeButton = Button(headerFrame, text="🌙", bg=yellow, fg=black,
font=("Calibri", 18, "bold"), cursor="hand2", activebackground=pink, activeforeground=white)
themeButton.pack(side=RIGHT, padx=5)

headerLabel = Label(headerFrame, text="Python Mail Application", bg=bg, fg=pink,
font=("Monotype Corsiva", 35, "bold underline"))
headerLabel.pack(anchor=CENTER)

# main
mainFrame = Frame(window, bg=bg, bd=0)
mainFrame.pack(expand=1, fill=BOTH)

# #page1
framePage1 = LabelFrame(mainFrame, text="Email Message Credentials", bg=bg, fg=blue,
font=("Monotype Corsiva", 18, "bold underline"), bd=2)
framePage1.pack(expand=1, fill=BOTH, padx=5, ipadx=5, ipady=5)

senderLabelFrame = LabelFrame(framePage1, text="Sender's Email Address", 
bg=bg, fg=blue, font=("Monotype Corsiva", 18, "bold underline"), bd=2)
senderLabelFrame.pack(fill=X, padx=5)

senderLabel = Label(senderLabelFrame, text="Sender's Email", bg=bg, fg=pink,
font=("Monotype Corsiva", 28, "bold"))
senderLabel.pack(side=LEFT, padx=5)

senderEntry = Entry(senderLabelFrame, bg=pink, fg=white,
font=("Calibri", 22, "bold"), width=30)
senderEntry.pack(side=RIGHT, padx=5)

senderInfoLabel = Label(senderLabelFrame, text="** Registered Email Only **", bg=bg, fg=golden,
font=("Monotype Corsiva", 16, "bold"))
senderInfoLabel.pack(anchor=CENTER)

receiverLabelFrame = LabelFrame(framePage1, text="Receiver's Email Address", 
bg=bg, fg=blue, font=("Monotype Corsiva", 18, "bold underline"), bd=2)
receiverLabelFrame.pack(fill=X, padx=5)
# ### To
receiver1Frame = Frame(receiverLabelFrame, bg=bg, bd=0)
receiver1Frame.pack(fill=X)

receiverLabel1 = Label(receiver1Frame, text="Receiver's Email", bg=bg, fg=orange,
font=("Monotype Corsiva", 28, "bold"))
receiverLabel1.pack(side=LEFT, padx=5)

receiverEntry1 = Entry(receiver1Frame, bg=orange, fg=white,
font=("Calibri", 22, "bold"), width=30)
receiverEntry1.pack(side=RIGHT, padx=5)

receiverInfoLabel1 = Label(receiver1Frame, text="** TO **", bg=bg, fg=golden,
font=("Monotype Corsiva", 16, "bold"))
receiverInfoLabel1.pack(anchor=CENTER)

# ### CC
receiver2Frame = Frame(receiverLabelFrame, bg=bg, bd=0)
receiver2Frame.pack(fill=X)

receiverLabel2 = Label(receiver2Frame, text="Receiver's Email", bg=bg, fg=green,
font=("Monotype Corsiva", 28, "bold"))
receiverLabel2.pack(side=LEFT, padx=5)

receiverEntry2 = Entry(receiver2Frame, bg=green, fg=white,
font=("Calibri", 22, "bold"), width=30)
receiverEntry2.pack(side=RIGHT, padx=5)

receiverInfoLabel2 = Label(receiver2Frame, text="** CC **", bg=bg, fg=golden,
font=("Monotype Corsiva", 16, "bold"))
receiverInfoLabel2.pack(anchor=CENTER)

# ### BCC
receiver3Frame = Frame(receiverLabelFrame, bg=bg, bd=0)
receiver3Frame.pack(fill=X)

receiverLabel3 = Label(receiver3Frame, text="Receiver's Email", bg=bg, fg=purple,
font=("Monotype Corsiva", 28, "bold"))
receiverLabel3.pack(side=LEFT, padx=5)

receiverEntry3 = Entry(receiver3Frame, bg=purple, fg=white,
font=("Calibri", 22, "bold"), width=30)
receiverEntry3.pack(side=RIGHT, padx=5)

receiverInfoLabel3 = Label(receiver3Frame, text="** BCC **", bg=bg, fg=golden,
font=("Monotype Corsiva", 16, "bold"))
receiverInfoLabel3.pack(anchor=CENTER)

# #### pageTogglers

pageTogglersLabelFrame = LabelFrame(framePage1, text="Page Togglers", bg=bg, fg=blue,
font=("Monotype Corsiva", 18, "bold underline"), bd=2)
pageTogglersLabelFrame.pack(fill=X, padx=5)

page2Toggler = Button(pageTogglersLabelFrame, text="Email Subject & Body", bg=pink, fg=white,
font=("Monotype Corsiva", 24, "bold"), cursor="hand2", activebackground=white, activeforeground=pink,
command=wayToPage2)
page2Toggler.pack(side=LEFT, padx=5, pady=5)

page3Toggler = Button(pageTogglersLabelFrame, text="Email Attachments", bg=green, fg=white,
font=("Monotype Corsiva", 24, "bold"), cursor="hand2", activebackground=white, activeforeground=green,
command=wayToPage3)
page3Toggler.pack(side=RIGHT, padx=5, pady=5)


# #### validation and clear and send

actionsLabelFrame = LabelFrame(framePage1, text="Actions", bg=bg, fg=blue,
font=("Monotype Corsiva", 18, "bold underline"), bd=2)
actionsLabelFrame.pack(fill=X, padx=5)

validateAll = Button(actionsLabelFrame, text="Validate All", bg=green, fg=white, width=20,
font=("Monotype Corsiva", 24, "bold"), cursor="hand2", activebackground=white, activeforeground=green)
validateAll.pack(side=LEFT, padx=5, pady=5)

sendMsg = Button(actionsLabelFrame, text="Send Email", bg=blue, fg=white, width=20,
font=("Monotype Corsiva", 24, "bold"), cursor="hand2", activebackground=white, activeforeground=blue)
sendMsg.pack(side=RIGHT, padx=5, pady=5)

clearAll = Button(actionsLabelFrame, text="Reset All", bg=red, fg=white, width=20,
font=("Monotype Corsiva", 24, "bold"), cursor="hand2", activebackground=white, activeforeground=red)
clearAll.pack(anchor=CENTER)

# # #page2
framePage2 = LabelFrame(mainFrame, text="Email Subject & Body", bg=bg, fg=blue,
font=("Monotype Corsiva", 18, "bold underline"), bd=2)
framePage2.pack(expand=1, fill=BOTH, padx=5, ipadx=5, ipady=5)

subjectLabelFrame = LabelFrame(framePage2, text="Email Subject", bg=bg, fg=blue,
font=("Monotype Corsiva", 18, "bold underline"), bd=2, height=20)
subjectLabelFrame.pack(fill=X, padx=5, ipadx=5, ipady=5)

subjectEntryBox = Entry(subjectLabelFrame,
bg=pink, fg=white, font=('Helvetica', 17, 'bold'), )
subjectEntryBox.pack(expand=1, fill=BOTH, padx=5, ipadx=5, ipady=5, pady=10)

bodyLabelFrame = LabelFrame(framePage2, text="Email Body", bg=bg, fg=blue,
font=("Monotype Corsiva", 18, "bold underline"), bd=2)
bodyLabelFrame.pack(fill=X, padx=5, ipadx=5, ipady=5)

bodyEntryBox = Text(bodyLabelFrame,
bg=golden, fg=black, font=('Helvetica', 17, 'bold'), bd=0, height=8)
bodyEntryBox.pack(expand=1, fill=BOTH, padx=5, ipadx=5, ipady=5)

bodyFrame = Frame(bodyLabelFrame, bg=bg, bd=0)
bodyFrame.pack(expand=1, fill=BOTH, padx=5)

openHtmlHelp = Label(bodyFrame,
text="Use the (Open File) Button To Use The Data From A Text Or Html File",
bg=bg, fg=orange, font=('Monotype Corsiva', 18, 'bold'))
openHtmlHelp.pack(side=LEFT)

openHtmlButton = Button(bodyFrame, text="Open File", bg=orange, fg=white,
activeforeground=orange, activebackground=white, cursor='hand2', font=('Monotype Corsiva', 16, 'bold'), width=15)
openHtmlButton.pack(side=RIGHT)

cmdLabelFrame = LabelFrame(framePage2, text="Page Togglers", bg=bg, fg=blue,
font=("Monotype Corsiva", 18, "bold underline"), bd=2)
cmdLabelFrame.pack(fill=X, padx=5, pady=5)

backBtnCmd = Button(cmdLabelFrame, text="◀ Back", bg=blue, fg=white,
font=("Monotype Corsiva", 20, "bold"), cursor="hand2", activebackground=white, activeforeground=blue,
command=wayToPage1)
backBtnCmd.pack(side=LEFT, ipadx=5, padx=10, pady=5)

doneBtnCmd = Button(cmdLabelFrame, text="Save And Validate", bg=green, fg=white,
font=("Monotype Corsiva", 20, "bold"), cursor="hand2", activebackground=white, activeforeground=green)
doneBtnCmd.pack(side=RIGHT, ipadx=5, padx=10, pady=5)

# # #page3
framePage3 = LabelFrame(mainFrame, text="Email Attachments", bg=bg, fg=blue,
font=("Monotype Corsiva", 18, "bold underline"), bd=2)
framePage3.pack(expand=1, fill=BOTH, padx=5, ipadx=5, ipady=5)

attachmentLabelFrame = LabelFrame(framePage3, text="Email Attached Files", bg=bg, fg=blue,
font=("Monotype Corsiva", 18, "bold underline"), bd=2)
attachmentLabelFrame.pack(expand=1, fill=BOTH, padx=5, ipadx=5, ipady=5)

attachmentHelpLabel = Label(attachmentLabelFrame, text='** Attached Files Will Be Shown In The Box Below **',
bg=bg, fg=pink, font=("Monotype Corsiva", 18, "bold"))
attachmentHelpLabel.pack(pady=5)

attachmentEntryBox = Text(attachmentLabelFrame,
bg=golden, fg=black, font=('Helvetica', 17, 'bold'), bd=0, height=8)
attachmentEntryBox.pack(expand=1, fill=BOTH, padx=5, ipadx=5, ipady=5)

attachmentFrame = Frame(attachmentLabelFrame, bg=bg, bd=0)
attachmentFrame.pack(expand=1, fill=BOTH, padx=5)

openHtmlHelp = Label(attachmentFrame,
text="Use the (Open File) Button To Attach Files",
bg=bg, fg=orange, font=('Monotype Corsiva', 18, 'bold'))
openHtmlHelp.pack(side=LEFT)

openHtmlButton = Button(attachmentFrame, text="Open File", bg=orange, fg=white,
activeforeground=orange, activebackground=white, cursor='hand2', font=('Monotype Corsiva', 16, 'bold'), width=15)
openHtmlButton.pack(side=RIGHT)

cmdLabelFrameAttachment = LabelFrame(framePage3, text="Page Togglers", bg=bg, fg=blue,
font=("Monotype Corsiva", 18, "bold underline"), bd=2)
cmdLabelFrameAttachment.pack(fill=X, padx=5, pady=5)

backAttachmentBtnCmd = Button(cmdLabelFrameAttachment, text="◀ Back", bg=blue, fg=white,
font=("Monotype Corsiva", 20, "bold"), cursor="hand2", activebackground=white, activeforeground=blue,
command=wayToPage1)
backAttachmentBtnCmd.pack(side=LEFT, ipadx=5, padx=10, pady=5)

doneAttachmentBtnCmd = Button(cmdLabelFrameAttachment, text="Save And Validate", bg=green, fg=white,
font=("Monotype Corsiva", 20, "bold"), cursor="hand2", activebackground=white, activeforeground=green)
doneAttachmentBtnCmd.pack(side=RIGHT, ipadx=5, padx=10, pady=5)


# footer
footerFrame = Frame(window, bg=bg, bd=0)
footerFrame.pack(fill=X)

footerLabelFrame = LabelFrame(footerFrame, text="Email Error Message", bg=bg, fg=blue,
font=("Monotype Corsiva", 18, "bold underline"), bd=2)
footerLabelFrame.pack(expand=1, fill=BOTH, padx=5, ipadx=5, ipady=5)

footerLabel = Label(footerLabelFrame, text="No Messages To Show", bg=bg, fg=red,
font=("Monotype Corsiva", 20, "bold underline"))
footerLabel.pack(anchor=CENTER)

framePage2.pack_forget()
framePage3.pack_forget()

window.mainloop()
