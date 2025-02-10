# AWS 서비스 사용하기 위한 방법
# 1. AWS와 연결 (O)
# 2. Source Code 작성
import boto3

def detect_labels_local_file(photo):


    client=boto3.client('rekognition')
   
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
        
    print('Detected labels in ' + photo)
    # 강아지일 확률을 출력!!
    # 강아지일 확률 : 99.5%

    # Person 이라는 key값이 존재하지 않으면
    # '사람이 아닙니다' 출력

    isPerson = False

    # print(response['Labels'])
    for label in response['Labels']:
        if label['Name'] == 'Person':
            isPerson = True

        if label['Name'] == 'Dog':
            print('강아지일 확률 : {:.1f}%'.format(label['Confidence']))
        # print (label['Name'] + ' : ' + str(label['Confidence']))
        
    if isPerson == False:
        print('사람이 아닙니다.')

    return len(response['Labels'])

def main():
    photo='../../Downloads/dog.jpg'

    label_count=detect_labels_local_file(photo)
    print("Labels detected: " + str(label_count))


if __name__ == "__main__":
    main()



