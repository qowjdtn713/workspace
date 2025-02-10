from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

import uuid 
import os #시스템관련 라이브러리
import Label # Detect Label 관련 내가 만든 라이브러리
import Compare
from werkzeug.utils import secure_filename

app = Flask(__name__)

if not os.path.exists('static/imgs'):
    os.mkdir('static/imgs')

@app.route('/')
def home():
    return render_template('cal.html')

@app.route('/cal')
def cal():
    return render_template('cal.html')

#get post 등 데이터를 수신하는 route에는 전송방식을 명시
@app.route('/add', methods = ['GET', 'POST'])
def add():
    #2개의 get으로 온 값을 받아 더해서 출력
    #args get 방식 수신 | form: post 방식 수신
    num1 = int(request.args['num1'])
    num2 = int(request.args['num2'])
    result = num1 + num2  # 계산한 결과를 변수에 저장
    return render_template('cal.html', result=result, num1=num1, num2=num2)

@app.route('/pic')
def pic():
    return render_template('pic.html')

@app.route('/label', methods=['POST'])
def label():

    #전송방식 약한 체크
    if request.method == 'POST':
        f = request.files['label']
        filename = secure_filename(f.filename)
        f.save('static/imgs/' + filename)

    # 도착한 사진의 경로 r 전달
    r = 'static/imgs/' + filename
    result = Label.detect_labels_local_file(r)

    # 결과 문자열에서 줄바꿈을 <br> 태그로 교체
    result = result.replace("\n", "<br>")  # \n을 <br> 태그로 대체

    # 반환 시 result를 HTML로 안전하게 출력
    return render_template('pic.html', result=result, image_path=r)

@app.route('/face')
def face():
    return render_template('face.html')

@app.route('/compare', methods = ['POST'])
def compare():
    if request.method == 'POST':
        f1 = request.files['face1']
        filename1 = secure_filename(f1.filename)
        unique_filename1 = str(uuid.uuid4()) + os.path.splitext(filename1)[1]  # uuid를 파일명에 추가하여 고유화
        f1.save('static/imgs/' + unique_filename1)
        r1 = 'static/imgs/' + unique_filename1

        # 두 번째 이미지 처리
        f2 = request.files['face2']
        filename2 = secure_filename(f2.filename)
        unique_filename2 = str(uuid.uuid4()) + os.path.splitext(filename2)[1]  # uuid를 파일명에 추가하여 고유화
        f2.save('static/imgs/' + unique_filename2)
        r2 = 'static/imgs/' + unique_filename2

        result = Compare.compare_faces(r1, r2)

        # 결과를 반환할 때, 고유한 이미지 경로를 전달
        return render_template('face.html', result=result, image_path1=r1, image_path2=r2)
if __name__ == '__main__':
    app.run()