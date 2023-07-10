from flask import Flask

# Flask 패키지에 있는 클래스를 통해 어플리케이션의 입구를 만들어줍니다
app = Flask(__name__)

@app.route('/')
def hello():
    return f'Hello, {__name__}'

@app.route('/haejung/')
def hello_haejung():
    return f'Hello, haejung'


#라우팅 주소를 만드실 때는 /경로명 까지만 적어줍니다.
#그다음에 만들어질 하위 경로도 /경로명
@app.route('/jjangu')
def hello_jjangu():
    return f'<b> JJANGU </b>'