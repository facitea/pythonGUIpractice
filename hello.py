import tkinter

window=tkinter.Tk()

window.title("첫 프로그램") # 프로그램 이름

window.geometry("640x480+100+100") # 가로세로길이+팝업가로+팝업세로 좌표

window.resizable(False, False) #가로세로 창 크기 조절 여부

window.mainloop()
