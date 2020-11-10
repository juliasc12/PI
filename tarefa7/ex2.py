from Tkinter import *
from PIL import ImageTk
from PIL import Image
import tkFileDialog
import cv2
import numpy as np

class GrabCutGUI(Frame):
    def init(self, master=None):
        Frame.init(self,master)
        self.iniciaUI()

    def iniciaUI(self):
        self.master.title("janela")
        self.pack()
        imagem = self.carregaImagem()
        self.canvas = Canvas(self.master, width = img.width(), height = img.height(), cursor = "cross")
        self.canvas.create_image(0,0, anchor = NW, image = img)
        self.canvas.pack()


    def carregaImagem(self):
        caminho = tkFileDialog.askopenfilename()

        if(caminho > 0):
            self.imagemOpenCV = cv2.imread(caminho)
            img = cv2.cvtColor(self.imagemOpenCV, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(img)
            return img

def main():
    root = Tk()
    appcut = GrabCutGUI(master=root)
    appcut.mainloop()

main()
