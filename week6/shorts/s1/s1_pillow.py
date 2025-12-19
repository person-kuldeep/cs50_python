from PIL import Image, ImageFilter


def main():
    """
    img = Image.open("in.jpeg")
    img.close()
    """
    with Image.open("in.jpeg") as img:
        print(img.size)
        print(img.format_description)
        print(img.mode)
        # print(img.info)
        # img sige in bytes
        # type(img.tobytes())
        # print(img.tobytes())
        # img = img.rotate(180)
        # img_gray = img.convert("L")

        # img_gray.save("out_gray.jpeg")
        # img_filetered = img_gray.filter(ImageFilter.EMBOSS)
        # img_filetered.save("out_gray_filtered.jpeg")
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("out.jpeg")
main()

