#pylint:disable=no-member
import cv2 as cv
import numpy as np
import random
import os
from textwrap import TextWrapper


class PictureTransformer:
    def __init__(self, quotes_file, directory):
        self.quotes_file = quotes_file
        self.directory = directory
        self.quotes = open(str(self.quotes_file)+".txt", "r").readlines()
        self.num_files = len([f for f in os.listdir(directory)if os.path.isfile(os.path.join(directory, f))])
        self.rand_pos = random.randint(1, self.num_files)
        self.rand_effect = random.randint(1,3)
        self.photo = None
        self.random_quote = ""

    def __str__(self):
        return f"Pictures from {self.directory} directory and there are {self.num_files} photos. Stoic quotes from {self.quotes_file}.txt. Picture state {self.photo}"

    def __repr__(self):
        return self.photo

    # # Select random pictures from directory
    # directory = "Photos"

    # # Access quotes from txt
    # quotes = open("quotes.txt", "r")
    # lines = quotes.readlines()

    # # Random photo vars
    # num_files = len([f for f in os.listdir(directory)if os.path.isfile(os.path.join(directory, f))])
    # rand_pos = random.randint(1,num_files)

    # Select a Random photo
    def random_photo(self):    
        # for idx ,filename in enumerate(os.listdir(self.directory)):
        #     print(self.rand_pos)
        #     if self.rand_pos == idx:
        #         print(filename)
        #         return cv.imread(self.directory + "/" + filename)
        # print(os.listdir(self.directory)[self.rand_pos])
        self.photo = cv.imread(f"{self.directory}/{os.listdir(self.directory)[self.rand_pos]}")
        return self.photo


    # Select random image effect 
    def effect_randomizer(self):
        if self.rand_effect == 1:
            return cv.cvtColor(self.photo, cv.COLOR_BGR2GRAY)
        elif self.rand_effect == 2:
            gray = cv.cvtColor(self.photo, cv.COLOR_BGR2GRAY)
            gauss = cv.GaussianBlur(gray, (3,3), 0)
            lap = cv.Laplacian(gauss, cv.CV_16S,ksize=3)
            return np.uint8(np.absolute(lap))
        elif self.rand_effect == 3:
            return self.photo

    # # Random text place
    # rand_pos_text = random.randint(1,len(lines) - 1)
    # # randomly choose quote and assign it to text variable
    def random_quote_selector(self):
        for no, line in enumerate(self.quotes,1):
            # insert \n for line split in putText
            tw = TextWrapper()
            tw.width = 50
            # Random quote
            
            if self.rand_pos == no:            
                if len(line) > 50:
                    self.random_quote = "\n".join(tw.wrap(line))
                else:
                    self.random_quote = line
                return self.random_quote

    # # Call random photo
    # photo = randomPhoto(directory, rand_pos)
    # # Call random quote
    # text = randomQuote(lines, rand_pos_text)
    # # Call random effect and image
    # img = effectRandomizer(photo)

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

    # Place text 
    def place_text(self):
        if len(self.random_quote) > 50:
            #Black Outline
            for i, line in enumerate(self.random_quote.split("\n")):
                y = self.y0 + i * self.line_height
                cv.putText(self.photo,
                            line,
                            (x, y),
                            self.font,
                            self.font_scale,
                            (0, 0, 0),
                            self.thickness + 1,
                            self.line_type)
            # Normal white text
            for i, line in enumerate(random_quote.split("\n")):
                y = self.y0 + i * self.line_height
                cv.putText(self.photo,
                            line,
                            (x, y),
                            self.font,
                            self.font_scale,
                            self.colour,
                            self.thickness,
                            self.line_type)

        else:

            #Black Outline
            for i, line in enumerate(random_quote.split("\n")):
                y = self.y0 + i * self.line_height
                cv.putText(self.photo,
                            self.line,
                            (x, y),
                            self.font,
                            self.font_scale,
                            (0, 0, 0),
                            self.thickness + 1,
                            self.line_type)
            # Normal white text
            for i, line in enumerate(random_quote):
                y = self.y0 + i * self.line_height
                cv.putText(self.photo,
                            self.line,
                            (x, y),
                            self.font,
                            self.font_scale,
                            self.colour,
                            self.thickness,
                            self.line_type)
                            
        cv.waitKey(0)
        cv.imwrite("image.jpg", self.photo)
# Call place text
# placeText(text, img)

random = PictureTransformer('quotes', 'Photos')
random.random_photo()
random.effect_randomizer()
random.random_quote_selector()
random.text_settings()
random.place_text()
print(random)