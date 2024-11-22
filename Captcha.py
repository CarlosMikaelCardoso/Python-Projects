from captcha.image import ImageCaptcha

image =  ImageCaptcha(width=280, height=80)

captchaText = 'Mikael'

data = image.generate(captchaText)

image.write(captchaText, 'captcha.png')