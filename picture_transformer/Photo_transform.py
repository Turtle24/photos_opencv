# pylint:disable=no-member
import cv2 as cv
import numpy as np
import random
import os
from textwrap import TextWrapper
import time
import logging


def timer(func):
    """A decorator that times each method

    Args:
        func (Method): Timer
    """

    def wrapper(self, *args, **kwargs):
        start = time.time()
        rv = func(self, *args, **kwargs)
        runtime = time.time() - start
        self.total_time += runtime
        return rv

    return wrapper


class PictureTransformer:
    def __init__(self, quotes_file, directory):
        """PictureTransformer is a class

        Args:
            quotes_file (string): The name of the quotes file being used in data
            directory (string): The location of the photos to use for transformation
        """
        self.quotes_file = quotes_file
        self.directory = directory
        self.num_files = len(
            [
                f
                for f in os.listdir(directory)
                if os.path.isfile(os.path.join(directory, f))
            ]
        )
        self.rand_pos = random.randint(1, self.num_files)
        self.rand_effect = random.randint(1, 3)
        self.photo = None
        self.random_quote = ""
        self.number = len(
            [
                f
                for f in os.listdir("created_images")
                if os.path.isfile(os.path.join("created_images", f))
            ]
        )
        self.text_settings = {
            "position": 0,
            "font_scale": 0,
            "colour": (0, 0, 0),
            "thickness": 0,
            "font": None,
            "line_type": None,
            "text_size": 0,
            "line_height": 0,
        }
        self.total_time = 0

    def __str__(self):
        return f"Picture state {self.photo} \nQuote: {self.random_quote}"

    @timer
    def random_photo(self):
        """A function that returns a random photo

        Returns:
            Numpy Array: The photo read by opencv
        """
        try:
            self.photo = cv.imread(
                f"{self.directory}/{os.listdir(self.directory)[self.rand_pos]}"
            )
        except BaseException as e:
            print(f"Couldn't select a picture, oops")
        return self.photo

    @timer
    def effect_randomizer(self):
        """A function that applies a random filter

        Returns:
            Numpy Array: A numpy array of the photo with an effect applied
        """
        if self.rand_effect == 1:
            self.photo = cv.cvtColor(self.photo, cv.COLOR_BGR2GRAY)
            return self.photo

        elif self.rand_effect == 2:
            gray = cv.cvtColor(self.photo, cv.COLOR_BGR2GRAY)
            gauss = cv.GaussianBlur(gray, (3, 3), 0)
            lap = cv.Laplacian(gauss, cv.CV_16S, ksize=3)
            self.photo = np.uint8(np.absolute(lap))
            return self.photo

        elif self.rand_effect == 3:
            return self.photo

    @timer
    def random_quote_selector(self):
        """A function that selects a random quote from the quote file.

        Returns:
            string: A quote
        """
        quotes = open(f"data/{self.quotes_file}.txt", "r").readlines()
        for no, line in enumerate(quotes, 1):
            tw = TextWrapper()
            tw.width = 50

            if self.rand_pos == no:
                if len(line) > 50:
                    self.random_quote = "\n".join(tw.wrap(line))
                else:
                    self.random_quote = line
                return self.random_quote

    @timer
    def text_settings_default(self):
        """A function that generates the default text settings"""
        self.text_settings["position"] = (
            self.photo.shape[1] // 20,
            self.photo.shape[0] // 2 + self.photo.shape[0] // 5,
        )
        self.text_settings["font_scale"] = 0.6
        self.text_settings["colour"] = (255, 255, 255)
        self.text_settings["thickness"] = 1
        self.text_settings["font"] = cv.FONT_HERSHEY_DUPLEX
        self.text_settings["line_type"] = cv.LINE_AA
        self.text_settings["text_size"], _ = cv.getTextSize(
            self.random_quote,
            self.text_settings["font"],
            self.text_settings["font_scale"],
            self.text_settings["thickness"],
        )
        self.text_settings["line_height"] = self.text_settings["text_size"][1] + 5
        self.x, self.y0 = self.text_settings["position"]

    @timer
    def black_outline(self):
        """A function that applies a black outline to the text for readability"""
        for i, line in enumerate(self.random_quote.split("\n")):
            y = self.y0 + i * self.text_settings["line_height"]
            cv.putText(
                self.photo,
                line,
                (self.x, y),
                self.text_settings["font"],
                self.text_settings["font_scale"],
                (0, 0, 0),
                self.text_settings["thickness"] + 1,
                self.text_settings["line_type"],
            )

    @timer
    def white_text(self):
        """A function that creates the text seen on the images"""
        for i, line in enumerate(self.random_quote.split("\n")):
            y = self.y0 + i * self.text_settings["line_height"]
            cv.putText(
                self.photo,
                line,
                (self.x, y),
                self.text_settings["font"],
                self.text_settings["font_scale"],
                self.text_settings["colour"],
                self.text_settings["thickness"],
                self.text_settings["line_type"],
            )

    @timer
    def place_text(self):
        """The text is applied to the photo and depending on the filter applied the text is altered."""
        if len(self.random_quote) > 50:
            # Black Outline
            self.black_outline()
            # Normal white text
            self.white_text()

        else:
            # Black Outline
            self.black_outline()
            # Normal white text
            self.white_text()

        cv.waitKey(0)
        cv.imwrite(f"created_images/image{self.number + 1}.jpg", self.photo)
