from aip import AipFace
import cv2
import ssl
import base64
import time


def get_aip():
    # 个人

    # 初始化AipFace对象
    aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)
    return aipFace


def face_detect(aipFace, file, mode=1):
    a = time.time()
    image = str(base64.b64encode(open(file, 'rb').read()), 'utf-8')
    imageType = "BASE64"

    """ 如果有可选参数 """
    options = {}
    options["face_field"] = "age,beauty,expression,face_shape,gender,glasses,landmark,race,quality,face_type"
    options["max_face_num"] = mode
    # options["face_type"] = "LIVE"

    """ 带参数调用人脸检测 """
    while True:
        try:
            result = aipFace.detect(image, imageType, options)
            break
        except:
            print('try again...')
            continue
    return result


def face_rec(aipFace, file1, file2):
    a = time.time()
    image = str(base64.b64encode(open(file1, 'rb').read()), 'utf-8')
    image1 = {}
    image1['image'] = image
    image1['image_type'] = 'BASE64'

    image = str(base64.b64encode(open(file2, 'rb').read()), 'utf-8')
    image2 = {}
    image2['image'] = image
    image2['image_type'] = 'BASE64'

    images = [image1, image2]

    """ 带参数调用人脸检测 """
    for y in range(3):
        try:
            result = aipFace.match(images)
            break
        except:
            print('try again...')
            continue
    try:
        # print(result)
        print(result['result']['score'], file1, file2, time.time() - a)
        return result['result']['score']
    except Exception as e:
        print(e)
        return 0


def compare_quality(aipFace, q1, q2):
    if (q1[0] >= q2[0]) and ((abs(q1[1])*2 + abs(q1[2]) + abs(q1[3])*0.5) < (abs(q2[1])*2 + abs(q2[2]) + abs(q2[3])*0.5)) and abs(q1[4] - q2[4]) < 0.1:
        return True
    return False


def user_add(aipFace, file, user_id, group='test_baidu_0'):
    a = time.time()
    image = str(base64.b64encode(open(file, 'rb').read()), 'utf-8')
    while True:
        try:
            result = aipFace.addUser(image, 'BASE64', group, user_id)
            break
        except:
            print('try again...')
            continue
    return result


def user_update(aipFace, file, user_id, group='test_baidu_0'):
    a = time.time()
    image = str(base64.b64encode(open(file, 'rb').read()), 'utf-8')
    for y in range(3):
        try:
            result = aipFace.updateUser(image, 'BASE64', group, user_id)
            break
        except:
            print('try again...')
            continue
    try:
        # print(result)
        print(result['result']['location'], time.time() - a)
        return True
    except Exception as e:
        print(e)
        return False


def face_num(aipFace, group='test_baidu_0'):
    a = time.time()
    for y in range(3):
        try:
            result = aipFace.getGroupUsers(group)
            break
        except Exception as e:
            print(e, 'try again...')
            continue
    print(result)
    return len(result['result']['user_id_list'])


def search_face(aipFace, file, group='test_baidu_0'):
    a = time.time()
    image = str(base64.b64encode(open(file, 'rb').read()), 'utf-8')
    while True:
        try:
            result = aipFace.search(image, 'BASE64', group)
            break
        except:
            print('try again...')
            continue
    return result


def add_group(aipFace, group_name):
    result = aipFace.groupAdd(group_name)
    print(result)
    result = aipFace.getGroupList()
    print(result)


if __name__ == '__main__':
    aip = get_aip()
    # print(face_detect(aip, 'face-6.jpg'))
    # face_rec(aip, 'baidu_face\\face-187.jpg', 'baidu_face\\face-167.jpg')
    # print(face_num(aip, 'test_baidu_0'))
    # for x in range(571):
    #     # user_add(aip, 'face_cut_all\\face-%d.jpg' % x, str(x), 'test_baidu_1')
    #     time.sleep(0.3)
    #     search_face(aip, 'face_cut_all\\face-%d.jpg' % x)
    # add_group(aip, 'African_black')
