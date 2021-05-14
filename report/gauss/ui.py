import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from gauss import file_input, file_output, run

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType('gauss.ui')[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.readBtn.clicked.connect(self.readBtnEvent)
        self.writeBtn.clicked.connect(self.writeBtnEvent)
        self.runBtn.clicked.connect(self.runBtnEvent)
        self.exitBtn.clicked.connect(self.exitBtnEvent)

    def readBtnEvent(self):
        try:
            file_path = QFileDialog.getOpenFileName(self, '행렬 파일 선택', './')  # tuple 타입을 반환함
            file_input(file_path[0])  # 0번째를 선택한다.
            self.statusLabel.setText(f'{file_path[0]} 선택 완료')
            self.statusLabel.setStyleSheet('Color:blue')
        except Exception as e:
            print('파일을 읽어오는 과정에서 문제가 발생했습니다.', e)
            self.exitBtnEvent()  # 프로그램 종료

    def writeBtnEvent(self):
        try:
            file_path = QFileDialog.getSaveFileName(self, '저장 파일 선택', './')
            file_output(file_path[0])
            self.statusLabel.setText(f'{file_path[0]} 에 저장 완료')
            self.statusLabel.setStyleSheet('Color:blue')
        except Exception as e:
            print('실행 결과를 저장하는 과정에서 문제가 발생했습니다.', e)
            self.exitBtnEvent()  # 프로그램 종료

    def runBtnEvent(self):
        try:
            self.outputDisplay.setPlainText(run())
        except Exception as e:
            print('가우스 소거법 실행 중 문제가 발생했습니다.', e)
            self.exitBtnEvent()  # 프로그램 종료

    def exitBtnEvent(self):
        QCoreApplication.instance().quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 프로그램을 실행시켜주는 클래스
    myWindow = WindowClass()  # WindowClass의 인스턴스 생성
    myWindow.show()  # 프로그램 화면을 보여주는 코드
    app.exec_()  # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
