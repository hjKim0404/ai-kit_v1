from utils.helper import paths2numpy, show_images, glob_all_files
import cv2


def face_resize_augmentation(images):
    """

    해당 함수는 wally 의 얼굴을 tight 하게 crop 해놓은 이미지를 사용합니다.
    예를 들어
    아래와 같이 3가지 각기 다른 h, w 을 가진 image들이 있다면

            image 1    image 2      image 3
    h, w    (10, 6)     (10,7)      (10,8)

    각 이미지들을  각각의 h, w으로  resize 시킵니다.

            image 1    image 2      image 3
    h, w    (10, 6)     (10,6)      (10,6)
    h, w    (10, 7)     (10,7)      (10,7)
    h, w    (10, 7)     (10,8)      (10,8)

    :return:
    """
    # image들의 h, w 을 추춣합니다.
    sizes = []
    for image in images:
        sizes.append(image.shape[:2])

    # 이미지들을 resize 합니다.
    ret_imgs = []
    for image in images:
        for h, w in sizes:
            ret_imgs.append(cv2.resize(image, dsize=(w, h), interpolation=cv2.INTER_NEAREST))
    return ret_imgs


if __name__ == '__main__':
    face_folder = '/Users/pai/Downloads/Find_Wally_Deploy/data/wally_face_tight_crop'
    paths = glob_all_files(face_folder)
    imgs = paths2numpy(paths)
    augimgs = face_resize_augmentation(imgs)
    show_images(augimgs)
