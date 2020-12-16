from googletrans import Translator
translator = Translator()

# translator = Translator(service_urls=[
# 'translate.google.com',
# 'translate.google.co.kr',
# ])

translated = translator.translate("Bonjour", dest="en")
print(translated.origin)
print(translated.text)