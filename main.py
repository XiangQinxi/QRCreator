# 导入库
from ttkbootstrap.window import *
from ttkbootstrap.widgets import *
import tkinter
from time import sleep
from tkinter import *
from tkinter import ttk, messagebox, filedialog, simpledialog
import shutil
import os.path
import os
import qrcode

# 初始变量
Toggle = 1
Version = 0.2

Language = "中文(简体)"
PathError = None
DebugCheck = False
ImagePath = None


# 保存二维码
def SaveQR():
    global PathError, ImagePath  # 导入全局变量
    if not os.path.exists(PathEntryString.get()):  # 检查文件是否存在
        PathError = messagebox.showerror(title="错误", message="请输入正确的目录地址！")
    else:
        FileName = simpledialog.askstring(title="提示", prompt="请输入文件名")  # 由用户输入文件名
        open(PathEntryString.get() + FileName + ".png", "w")  # 保存图片文件在用户输入的地址里
        Image = qrcode.make(TextEntryString.get())  # 设置二维码的内容
        type(Image)  # qrcode.image.pil.PilImage
        Image.save(FileName + ".png")  # 制作二维码图在本地
        shutil.copy(os.getcwd() + "\\" + FileName + ".png", PathEntryString.get())  # 将本地二维码文件复制到用户输入的地址
        NewQR = PhotoImage(file=(os.getcwd() + "\\" + FileName + ".png"))
        QRImage.configure(image=NewQR)
        os.remove(os.getcwd() + "\\" + FileName + ".png")  # 移除本地的二维码图
        ImagePath = str(PathEntryString) + str(FileName) + ".png"
        messagebox.showinfo(title="提升", message="生成成功！")


def OpenQRSettings():
    QRSettings = Toplevel()  # 初始化二维码设置窗口
    QRSettings.geometry("600x300")  # 初始化二维码大小
    QRSettings.bind("<Control-KeyPress-R>", lambda ckr: ToggleTheme())  # Ctrl+R键切换主题 (大写)
    QRSettings.bind("<Control-KeyPress-r>", lambda ckr: ToggleTheme())  # Ctrl+r键切换主题 (小写)

    QRTab = ttk.Notebook(QRSettings)
    QRTabLanguage = ttk.Frame(QRTab)

    QRTabLanguageLabel = ttk.Label(QRTabLanguage, text="语言设置")
    QRTabLanguageLabel.grid(row=0, column=0, padx=10, pady=10)

    def SelectLanguage(Select=None):
        print(Select)
        if QRTabLanguageChooser.get() == "中文(简体)":
            QRTabLanguageLabel.configure(text="语言设置")
            SaveButton.configure(text="生成")
            DebugButton.configure(text="调试")
            ChoosePath.configure(text="选择目录")
            if PathEntryString.get() == "Please entry the address":
                PathEntryString.set("请输入保存地址")

        elif QRTabLanguageChooser.get() == "English":
            QRTabLanguageLabel.configure(text="Language Setting")
            SaveButton.configure(text="Save")
            DebugButton.configure(text="Debug")
            ChoosePath.configure(text="Chooser Path")
            if PathEntryString.get() == "请输入保存地址":
                PathEntryString.set("Please entry the address")
        Window.update()

    QRTabLanguageChooser = ttk.Combobox(QRTabLanguage, values=("中文(简体)", "English"))
    QRTabLanguageChooser.bind("<<ComboboxSelected>>", SelectLanguage)
    QRTabLanguageChooser.set(Language)
    QRTabLanguageChooser.grid(row=0, column=1, padx=10, pady=10)

    QRTab.add(QRTabLanguage, text="Language")
    QRTab.pack(fill=BOTH, expand=YES)

    QRSettings.mainloop()


def OpenChoosePath():
    PathEntryString.set(filedialog.askdirectory(title="选择保存目录"))


def ToggleTheme():
    global Toggle
    Window.configure(cursor="watch")
    if Toggle == 0:
        Style.theme_use("MiLight-B 1.0")
        print("Light")
        Toggle = 1
    elif Toggle == 1:
        Style.theme_use("MiDark-B 1.0")
        print("Dark")
        Toggle = 0
    Window.configure(cursor="arrow")


def AboutQR():
    messagebox.showinfo(title="关于", message="这是一个用于生成QR码的小程序，使用Python语言编写，界面库是tkinter，QR生成库是qrcode。\n"
                                            "使用rdbende的Sun-Valley-ttk-theme主题界面\n"
                                            "作者:XiangQinxi")


def OperationIntroduction():
    messagebox.showinfo(title="操作介绍", message="双击右边QR码图片打开设置。\n"
                                              "双击选择目录打开选择目录对话框。\n"
                                              "主窗口按下Ctrl+A显示关于对话框\n"
                                              "主窗口按下Ctrl+R切换主题。\n")


def VersionDialog():
    messagebox.showinfo(title="版本", message=f"VERSION : {str(Version)}")


def OpenDebugDialog():
    DebugDialog = Toplevel()
    DebugDialog.title("调试器")
    DebugDialog.geometry("600x300")

    DebugSettingLabel = Label(DebugDialog, text="调试：")
    DebugSettingLabel.grid(row=0, column=0, padx=5, pady=10)

    DebugSettingSwitch = ttk.Checkbutton(DebugDialog, style="Switch.TCheckbutton", offvalue=DebugCheck)

    DebugSettingSwitch.grid(row=0, column=1, padx=5, pady=10)

    DebugDialog.mainloop()


def WindowReSize():
    Window.geometry("600x300")


if os.path.exists("image/QRCreator.png"):
    Window = Window(themename="MiDark-B 1.0", iconphoto="image\\QRCreator.png")
else:
    Window = Window(themename="MiDark-B 1.0")


Style = Style()
Style.theme_use("MiDark-B 1.0")
Window.title("二维码生成器")
Window.geometry("600x300")
#Window.resizable(False, False)
Window.bind("<Control-KeyPress-R>", lambda ckr: ToggleTheme())
Window.bind("<Control-KeyPress-r>", lambda ckr: ToggleTheme())
Window.bind("<Control-KeyPress-E>", lambda ckr: WindowReSize())
Window.bind("<Control-KeyPress-e>", lambda ckr: WindowReSize())
Window.bind("<Control-KeyPress-A>", lambda bt1: AboutQR())
Window.bind("<Control-KeyPress-a>", lambda bt1: AboutQR())
Window.bind("<Double-Button-2>", lambda bt3: VersionDialog())
Window.bind("<Double-Button-3>", lambda bt3: OperationIntroduction())


Editor = ttk.Frame(Window)

TextEntryString = StringVar()
TextEntryString.set("请输入二维码内容")
TextEntry = ttk.Entry(Editor, textvariable=TextEntryString)
TextEntry.bind("<Button-1>", lambda bt1: TextEntryString.set(""))
TextEntry.pack(fill=X, padx=10, pady=10, side=TOP)

PathFrame = ttk.Frame(Editor)
PathFrame.pack(fill=X, side=TOP)

PathEntryString = StringVar()
PathEntryString.set("请输入保存地址")
PathEntry = ttk.Entry(PathFrame, textvariable=PathEntryString)
PathEntry.bind("<Double-Button-1>", lambda bt1: OpenChoosePath())
PathEntry.pack(fill=X, pady=10, padx=10, side=LEFT, expand=YES)

ChoosePath = ttk.Button(PathFrame, style="Accent.TButton", text="选择目录", command=OpenChoosePath, cursor="hand2")
ChoosePath.pack(pady=10, padx=10, side=LEFT)

SSFrame = ttk.Frame(Editor)
SSFrame.pack(side=BOTTOM, fill=X, padx=10, pady=10)

DebugButton = ttk.Button(SSFrame, text="调试", cursor="hand2", command=OpenDebugDialog)
DebugButton.pack(anchor=SW, side=BOTTOM, fill=X, pady=10)

SaveButton = ttk.Button(SSFrame, style="Accent.TButton", text="生成", command=SaveQR, cursor="hand2")
SaveButton.pack(anchor=SW, side=BOTTOM, fill=X)

Editor.pack(side=LEFT, fill=BOTH, expand=YES)

QR = ttk.Frame(Window)

if os.path.exists("image\\Qr.png"):
    QRFile = PhotoImage(file="image\\Qr.png")
else:
    QRFile = PhotoImage()

QRImage = ttk.Label(image=QRFile)
QRImage.bind("<Double-Button-1>", lambda bt1: OpenQRSettings())
QRImage.pack(fill=BOTH, expand=YES, padx=10, pady=10)

QR.pack(side=RIGHT, fill=BOTH, expand=YES)

SizeDrip = ttk.Sizegrip(QR)
SizeDrip.pack(anchor=SE, side=RIGHT)

Window.mainloop()  # 运行窗口
