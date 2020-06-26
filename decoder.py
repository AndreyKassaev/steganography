import cv2

class Decoder:
    
    def __init__(self, img):
        self.img = img
        
    def decode(self):
        
        img_len = img[0,0,0] 
        encoded_msg = img[1:img_len + 1, 0, 0]
        msg = ''
        
        for i in encoded_msg:
            msg += chr(i)
        
        print(msg)
        
if __name__ == "__main__":
    try:
        img = cv2.imread('encoded_img.png')
        Decoder(img).decode()
    except Exception as error:
        print(error)