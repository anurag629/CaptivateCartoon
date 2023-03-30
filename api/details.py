import heapq

from .imageToDetails import image_to_details


def detail(img):
    ''' 
    Convert the image to a dictionary of details.

    img: image path

    Output: 
        Generate a dictionary of details from the given image using the DeepFace API as given below format.

        face_analysis = [{'emotion': {'angry': 6.721813231706619,
        'disgust': 0.0009493059224041644,
        'fear': 9.754016250371933,
        'happy': 0.03365158336237073,
        'sad': 27.769500017166138,
        'surprise': 0.013286530156619847,
        'neutral': 55.70678114891052},
        'dominant_emotion': 'neutral',
        'region': {'x': 105, 'y': 529, 'w': 987, 'h': 987},
        'age': 30,
        'gender': {'Woman': 0.00331170012941584, 'Man': 99.99668598175049},
        'dominant_gender': 'Man',
        'race': {'asian': 1.0386232286691666,
        'indian': 3.0180728062987328,
        'black': 0.14522826531901956,
        'white': 38.41095566749573,
        'middle eastern': 32.77770280838013,
        'latino hispanic': 24.609413743019104},
        'dominant_race': 'white'}]

        From the above analysis, the the below dictionary will be generated.

        emotion = face_analysis[0]['emotion']

        largest_emotion = heapq.nlargest(1, emotion, key=emotion.get)[-1]
        second_largest_emotion = heapq.nlargest(2, emotion, key=emotion.get)[-1]
        age = face_analysis[0]['age']
        dominant_gender = face_analysis[0]['dominant_gender']

        detail = {
            largest_emotion: largest_emotion,
            second_largest_emotion: second_largest_emotion,
            age: age,
            dominent_gender: dominent_gender,
        }
    '''

    face_analysis = image_to_details(img)

    emotion = face_analysis[0]['emotion']

    largest_emotion = heapq.nlargest(1, emotion, key=emotion.get)[-1]
    second_largest_emotion = heapq.nlargest(2, emotion, key=emotion.get)[-1]
    age = face_analysis[0]['age']
    dominant_gender = face_analysis[0]['dominant_gender']

    detail = {
        'largest_emotion': largest_emotion,
        'second_largest_emotion': second_largest_emotion,
        'age': age,
        'dominant_gender': dominant_gender,
    }

    return detail
