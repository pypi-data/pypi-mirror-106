from PIL import Image


def convertTopdf(path, pdf_name):
    '''
    Collects images and make pdf of all images
    :param path:
    :param pdf_name:
    :return:
    '''
    li = []
    for img in path.glob("*"):
        im = Image.open(img)
        li.append(im)

    im_list = li
    pdf_name = pdf_name + ".pdf"
    im_list[0].save(pdf_name, "PDF", resolution=50.0, save_all=True, append_images=im_list[1:])


