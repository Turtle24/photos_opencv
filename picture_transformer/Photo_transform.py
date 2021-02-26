#pylint:disable=no-member
import cv2 as cv
import numpy as np
import random
import os
from textwrap import TextWrapper
import time

def timer(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		rv = func(*args, **kwargs)
		total = time.time() - start
		print(f"Time: {total}")
		return rv
	return wrapper

class PictureTransformer:
    def __init__(self, quotes_file, directory):
        self.quotes_file = quotes_file
        self.directory = directory
        self.num_files = len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
        self.rand_pos = random.randint(1, self.num_files)
        self.rand_effect = random.randint(1,3)
        self.photo = None
        self.random_quote = ""
        self.number = len([f for f in os.listdir("created_images") if os.path.isfile(os.path.join("created_images", f))]) 

    def __str__(self):
        return f"Picture state {self.photo} \nQuote: {self.random_quote}"

    @timer
    def random_photo(self):    
        self.photo = cv.imread(f"{self.directory}/{os.listdir(self.directory)[self.rand_pos]}")
        return self.photo

    @timer
    def effect_randomizer(self):
        if self.rand_effect == 1:
            self.photo = cv.cvtColor(self.photo, cv.COLOR_BGR2GRAY)
            return self.photo
        elif self.rand_effect == 2:
            gray = cv.cvtColor(self.photo, cv.COLOR_BGR2GRAY)
            gauss = cv.GaussianBlur(gray, (3,3), 0)
            lap = cv.Laplacian(gauss, cv.CV_16S,ksize=3)
            self.photo = np.uint8(np.absolute(lap))
            return self.photo
        elif self.rand_effect == 3:
            return self.photo
    @timer
    def random_quote_selector(self):
        quotes = open(f"data/{self.quotes_file}.txt", "r").readlines()
        for no, line in enumerate(quotes,1):
            tw = TextWrapper()
            tw.width = 50
            # Random quote
            
            if self.rand_pos == no:            
                if len(line) > 50:
                    self.random_quote = "\n".join(tw.wrap(line))
                else:
                    self.random_quote = line
                return self.random_quote

class TextSettings(PictureTransformer):
    def __init__(self, random_quote, photo):
        super().__init__(random_quote, photo)
        self.position = 0
        self.font_scale = 0
        self.colour = (None, None, None)
        self.thickness = 0
        self.font = None 
        self.line_type = None
        self.text_size, _ = 0, 0
        self.line_height = None
        self.x, self.y0 = (None, None)

    def __str__(self):
        return f"Photo {self.photo} \n{self.random_quote}"

    @timer
    def text_settings_default(self):
        # Text on image variables
        self.position = (self.photo.shape[1] // 20, self.photo.shape[0] // 2 + self.photo.shape[0] // 5)
        self.font_scale = .6
        self.colour = (255, 255, 255)
        self.thickness = 1
        self.font = cv.FONT_HERSHEY_DUPLEX  
        self.line_type = cv.LINE_AA
        self.text_size, _ = cv.getTextSize(self.random_quote, self.font, self.font_scale, self.thickness)
        self.line_height = self.text_size[1] + 5
        self.x, self.y0 = self.position
    
    @timer
    def place_text(self):
        if len(self.random_quote) > 50:
            #Black Outline
            for i, line in enumerate(self.random_quote.split("\n")):
                y = self.y0 + i * self.line_height
                cv.putText(self.photo,
                            line,
                            (self.x, y),
                            self.font,
                            self.font_scale,
                            (0, 0, 0),
                            self.thickness + 1,
                            self.line_type)
            # Normal white text
            for i, line in enumerate(self.random_quote.split("\n")):
                y = self.y0 + i * self.line_height
                cv.putText(self.photo,
                            line,
                            (self.x, y),
                            self.font,
                            self.font_scale,
                            self.colour,
                            self.thickness,
                            self.line_type)

        else:
            #Black Outline
            for i, line in enumerate(self.random_quote.split("\n")):
                y = self.y0 + i * self.line_height
                cv.putText(self.photo,
                            self.line,
                            (self.x, y),
                            self.font,
                            self.font_scale,
                            (0, 0, 0),
                            self.thickness + 1,
                            self.line_type)
            # Normal white text
            for i, line in enumerate(self.random_quote):
                y = self.y0 + i * self.line_height
                cv.putText(self.photo,
                            self.line,
                            (self.x, y),
                            self.font,
                            self.font_scale,
                            self.colour,
                            self.thickness,
                            self.line_type)           
        cv.waitKey(0)
        cv.imwrite(f"created_images/image{self.number + 1}.jpg", self.photo)