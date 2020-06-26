import cv2

class Encoder:
    
    def __init__(self, img):
        self.img = img

    def input_msg(self):
        """Requests a message from user."""
        msg = input('Enter your text (max 255 chars): ')
        self.validate_msg(msg)

    def validate_msg(self, msg):
        """Validate the message."""
        
        msg_len = len(msg)
        
        if msg_len == 0 :
            print('Message is empty, please type something')
            input_msg()

        elif msg_len > 255:
            print('Message too long, 255 chars is max') 
            input_msg()
            
        
        self.msg2ASCII(msg, msg_len)            

    def msg2ASCII(self, msg, msg_len):
        """Create list with ASCII codes of message.
        First element represent the length of message.
        """
        msg_ASCII = [msg_len]

        for i in msg:
            msg_ASCII.append(ord(i))
        self.encode_msg(msg_ASCII)

    def encode_msg(self, msg_ASCII):
        """Create new image from original by replacing
        rows of the first column of the first matrix
        with encoded message.
        """
        
        for i in range(len(msg_ASCII)):
            img[i,0,0] = msg_ASCII[i]

        cv2.imwrite('encoded_img.png',img)
        print('Encoded Image Created\nencoded_img.png')

if __name__ == "__main__":
    try:
        img = cv2.imread('harold.jpg')
        Encoder(img).input_msg()
    except Exception as error:
        print(error)