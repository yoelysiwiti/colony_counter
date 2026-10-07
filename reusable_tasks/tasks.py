import qrcode

class Tasks:
    @staticmethod
    def qr_generator(in_content):
        content = in_content
        img = qrcode.make(content)
        img.save("qr_img.png")
