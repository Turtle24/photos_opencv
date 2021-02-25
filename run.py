from picture_transformer import photo_transform as pt
import cv2 as cv

# random = pt.PictureTransformer('quotes', 'Photos')
# random.random_photo()
# random.effect_randomizer()
# quote = random.random_quote_selector()
# photo, r_quote = random.photo, random.random_quote
settings = pt.TextSettings('quotes', 'Photos')
# text_settings
settings.random_photo()
settings.effect_randomizer()
settings.random_quote_selector()
settings.text_settings_default()
settings.place_text()
print(settings)

# cv.imwrite("image.jpg", photo)