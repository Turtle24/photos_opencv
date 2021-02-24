from photo_transform import PictureTransformer

class TextSettings(PictureTransformer):
    def __init__(self):
        super().__init__(self)
        # Text on image variables
        self.position = 0
        self.font_scale = 0
        self.colour = (None, None, None)
        self.thickness = 0
        self.font = None 
        self.line_type = None
        self.text_size, _ = None
        self.line_height = None
        self.x, self.y0 = (None, None)



    def text_settings(self):
        # Text on image variables
        self.position = (self.photo.shape[1] // 20, self.photo.shape[0] // 2 + self.photo.shape[0] // 5)
        self.font_scale = .6
        self.colour = (255, 255, 255)
        self.thickness = 1
        self.font = cv.FONT_HERSHEY_DUPLEX  
        self.line_type = cv.LINE_AA
        self.text_size, _ = cv.getTextSize(self.random_quote, font, font_scale, thickness)
        self.line_height = text_size[1] + 5
        self.x, self.y0 = position