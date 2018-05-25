#Prahar Patel
from tkinter import *
    
import googletrans
    
translator = googletrans.Translator()


class BaseFrame:
    def __init__(self, master):
        def clip():
            master.clipboard_clear()
            master.clipboard_append(translator.translate(self.box.get(1.0, END), self.var.get()).text)

        master = Frame(master)
        frame1 = LabelFrame(master, text="Enter text: ")
        frame1.pack()
        self.box = Text(frame1, width=150, height=20)
        self.box.pack(fill=BOTH)

        frame2 = LabelFrame(master, text="Select language:")
        frame2.pack()
        self.var = StringVar()
        self.var.set("es")
        w = OptionMenu(frame2, self.var,
                                            "af",
                                            "sq",
                                            "ar",
                                            "az",
                                            "eu",
                                            "bn",
                                            "be",
                                            "bg",
                                            "ca",
                                            "zh-CN",
                                            "zh-TW",
                                            "hr",
                                            "cs",
                                            "da",
                                            "nl",
                                            "en",
                                            "eo",
                                            "et",
                                            "tl",
                                            "fi",
                                            "fr",
                                            "gl",
                                            "ka",
                                            "de",
                                            "el",
                                            "gu",
                                            "ht",
                                            "iw",
                                            "hi",
                                            "hu",
                                            "is",
                                            "id",
                                            "ga",
                                            "it",
                                            "ja",
                                            "kn",
                                            "ko",
                                            "la",
                                            "lv",
                                            "lt",
                                            "mk",
                                            "ms",
                                            "mt",
                                            "no",
                                            "fa",
                                            "pl",
                                            "pt",
                                            "ro",
                                            "ru",
                                            "sr",
                                            "sk",
                                            "sl",
                                            "es",
                                            "sw",
                                            "sv",
                                            "ta",
                                            "te",
                                            "th",
                                            "tr",
                                            "uk",
                                            "ur",
                                            "vi",
                                            "cy",
                                            "yi",)
        w.pack()

        Button(master, text="translate", command=self.translate).pack()

        frame3 = LabelFrame(master, text="Result:")
        frame3.pack()
        self.result = Text(frame3, width=150, height=20)
        self.result.pack(fill=BOTH)

        Button(master, text="Copy!", command=clip).pack()
        Button(master, text="clear", command=self.clear).pack()

        master.pack(fill=BOTH)

    def translate(self):
        self.result.delete(1.0, END)
        self.result.insert(END, translator.translate(self.box.get(1.0, END), self.var.get()).text) # box.get is the actual text, self.var.get is for target lang

    def clear(self):
        self.result.delete(1.0, END)
        self.box.delete(1.0, END)

if __name__ == '__main__':
    root = Tk()
    root.title("CS 352 Language Translator")
    BaseFrame(root)
    root.mainloop()
