#Prahar Patel
from tkinter import *
    
import googletrans
    
translator = googletrans.Translator()


class BaseFrame:
    def __init__(self, mainApp):
        def clip():
            mainApp.clipboard_clear()
            mainApp.clipboard_append(translator.translate(self.box.get(1.0, END), self.var.get()).text)

        mainApp = Frame(mainApp)
        inputFrame = LabelFrame(mainApp, text="Enter text: ") # enter text to translate, auto-detects input language
        inputFrame.pack()
        self.box = Text(inputFrame, width=150, height=15)
        self.box.pack(fill=BOTH)

        languageFrame = LabelFrame(mainApp, text="Select language:") # dropdown to select target language
        languageFrame.pack()
        self.var = StringVar()
        self.var.set("es")
        w = OptionMenu(languageFrame, self.var,
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

        Button(mainApp, text="translate", command=self.translate).pack()

        resultFrame = LabelFrame(mainApp, text="Result:") 
        resultFrame.pack()
        self.result = Text(resultFrame, width=150, height=15)
        self.result.pack(fill=BOTH)

        Button(mainApp, text="Copy text", command=clip).pack() 
        Button(mainApp, text="Clear All", command=self.clear).pack()

        mainApp.pack(fill=BOTH)

    def translate(self):
        self.result.delete(1.0, END)
        self.result.insert(END, translator.translate(self.box.get(1.0, END), self.var.get()).text) # box.get is the actual text, self.var.get is for target lang

    def clear(self):
        self.result.delete(1.0, END)
        self.box.delete(1.0, END)

if __name__ == '__main__':
    root = Tk()
    root.title("CS 352 Language Translator") #frame TEXT
    BaseFrame(root)
    root.mainloop()
