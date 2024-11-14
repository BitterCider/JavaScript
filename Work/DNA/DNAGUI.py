from tkinter import * 
from sequences import *
from main import randomDNA
from bio_seq_class import *

app = Tk()
app.geometry("500x500")

seq = Entry(app)
seq_type = Entry(app)
label = Entry(app)
length = Entry(app)

seq.insert(0, "-ACTG-")
seq_type.insert(0, "-DNA-")
label.insert(0, "-No label given-")
length.insert(0,"-Number of bases-")

seq.grid(row=0, column=1)
seq_type.grid(row=1, column=1)
label.grid(row=2, column=1)
length.grid(row=3, column=1)

Label(app, text="Enter Sequence : ").grid(row=0, column=0)
Label(app, text="DNA/RNA : ").grid(row=1, column=0)
Label(app, text="Label : ").grid(row=2, column=0)
Label(app, text="Length: ").grid(row=3, column=0)


def Instanciate():
    bioseq = bio_seq(seq.get(), seq_type.get(), label.get())
    seqinfo = Label(app, text=bioseq.show_info)
    seqinfo.grid(row=5, column=1)
    
def rndInstanciate():
    if seq_type.get() == "RNA":
        dnaseq = bio_seq()
        dnaseq.randomseq(int(length.get()), "RNA")
        Label(app, text=dnaseq.show_info).grid(row=5, column=1)
        Label(app, text=dnaseq.nuc_frequency).grid(row=6, column=1)
        
        
    if seq_type.get() == "DNA":
        rnaseq = bio_seq()
        rnaseq.randomseq(int(length.get()), "DNA")
        Label(app, text=rnaseq.show_info).grid(row=5, column=1)
        Label(app, text=rnaseq.nuc_frequency).grid(row=6, column=1)
        
            
        
        
rndseqButton = Button(app, text="Generate", command=rndInstanciate)
rndseqButton.grid(row=3, column=2)
seqButton = Button(app, text="Run", command=Instanciate)
seqButton.grid(row=2, column=2)
app.title("Bio Sequence Interpreter")

app.mainloop()
    
