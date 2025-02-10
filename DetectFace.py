import boto3
import json

def detect_faces(photo):
    
    client = boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.detect_faces(Image={'Bytes': image.read()}, Attributes=['ALL'])

    # 1. 20 between 30 -> 25
    # 연령 : 25(세)

    # 2. 성별 Male, Female
    # 성별 : 남성 혹은 여성

    # 3. 대표감정 : HAPPY

    print('Detected faces for ' + photo)
    for faceDetail in response['FaceDetails']:
        # print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
        #       + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')

        age = (faceDetail['AgeRange']['High'] + faceDetail['AgeRange']['Low']) / 2
        print(f'연령 : {age}세')
        # print(json.dumps(faceDetail, indent=4, sort_keys=True))
        # Access predictions for individual face details and print them
        # print("Gender: " + str(faceDetail['Gender']))

        if faceDetail['Gender']['Value'] == 'Male':
            print('성별 : 남성')
        else:
            print('성별 : 여성')

        # print("Smile: " + str(faceDetail['Smile']))
        # print("Eyeglasses: " + str(faceDetail['Eyeglasses']))
        # print("Face Occluded: " + str(faceDetail['FaceOccluded']))
        # print("Emotions: " + str(faceDetail['Emotions'][0]))

        print('대표 감정 : {}'.format(faceDetail['Emotions'][0]['Type']))
        print('2번째 감정 : {}'.format(faceDetail['Emotions'][1]['Type']))
        print('3번째 감정 : {}'.format(faceDetail['Emotions'][2]['Type']))

    return len(response['FaceDetails'])
    
def main():
    photo='../../Downloads/resumePic.jpg'
    face_count=detect_faces(photo)
    print("Faces detected: " + str(face_count))

if __name__ == "__main__":
    main()
