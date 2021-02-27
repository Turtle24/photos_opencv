from picture_transformer import photo_transform as pt
from automation import email_image 
import cv2 as cv

settings = pt.PictureTransformer('quotes', 'Photos')
settings.random_photo()
settings.effect_randomizer()
settings.random_quote_selector()
settings.text_settings_default()
settings.place_text()
test = email_image.EmailSettings()
test.send_email()