from picture_transformer import photo_transform as pt
import cv2 as cv

settings = pt.TextSettings('quotes', 'Photos')
settings.random_photo()
settings.effect_randomizer()
settings.random_quote_selector()
settings.text_settings_default()
settings.place_text()