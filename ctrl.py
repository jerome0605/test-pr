# ctrl.py

class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self):    # ^, % 연산자 제거
        try: # 숫자가 아닌 값이 입력되었을 때도 프로그램이 동작하도록 예외처리 구문 추가    
            num1 = float(self.view.le1.text())
            num2 = float(self.view.le2.text())
            operator = self.view.cb.currentText()
            # 연산자에 따라 계산을 수행하고 결과를 반환하는 부분 수정
            if operator == '+':
                return f'{num1} + {num2} = {self.sum(num1, num2)}'
            elif operator == '-':
                return f'{num1} - {num2} = {self.sub(num1, num2)}' 
            elif operator == '*':
                return f'{num1} * {num2} = {self.mul(num1, num2)}'
            elif operator == '/':
                return f'{num1} / {num2} = {self.div(num1, num2)}'
            #elif operator == '^':
            #    return f'{num1} ^ {num2} = {self.pow(num1, num2)}'
            #elif operator == '%':
            #    return f'{num1} % {num2} = {self.mod(num1, num2)}'
            else:
                return 'Calculation Error'
        except:
            return 'Calculation Error'
        
    def mod(self, a, b):    # 나머지 연산 함수 추가
        try:
            if (b==0):  # 0으로 나누는 경우 예외 처리
                raise Exception("Divisor Error")  
        except Exception as e:
            return e
        
        return a % b
    
    def connectSignals(self):   # 시그널 연결
        self.view.btn1.clicked.connect(lambda:self.view.setDisplay(self.calculate()))  
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self, a, b):    # 덧셈 함수 추가
        return a+b
    
    def sub(self, a, b):    # 뺄셈 함수 추가
        return a-b
        
    def mul(self, a, b):    # 곱셈 함수 추가
        return a*b
    
    def div(self, a, b):    # 예외 처리를 사용하도록 수정
        try:
            if (b==0):  # 0으로 나누는 경우 예외 처리
                raise Exception("Divisor Error")  
            
        except Exception as e:
            return e
        
        return a / b 
    
    def pow(self, a, b):    # 거듭제곱 함수 수정
        try:
            if (a==0):
                raise Exception("Base Error")
        except Exception as e:
            return e
        
        return pow(a, b)
        
    
    

    
