from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from deep_translator import GoogleTranslator

app = Flask(__name__)
api = Api(app)



language_dict = {"amharic":"am",
"arabic":"ar",
"basque":"eu",
"bengali":"bn",
"english":"en",
"portuguese":"pt-BR",
"bulgarian":"bg",
"catalan":"ca",
"cherokee":"chr",
"croatian":"hr",
"czech":"cs",
"danish":"da",
"dutch":"nl",
"estonian":"et",
"filipino":"fil",
"finnish":"fi",
"french":"fr",
"german":"de",
"greek":"el",
"gujarati":"gu",
"hebrew":"iw",
"hindi":"hi",
"hungarian":"hu",
"icelandic":"is",
"indonesian":"id",
"italian":"it",
"japanese":"ja",
"kannada":"kn",
"korean":"ko",
"latvian":"lv",
"lithuanian":"lt",
"malay":"ms",
"malayalam":"ml",
"marathi":"mr",
"norwegian":"no",
"polish":"pl",
"romanian":"ro",
"russian":"ru",
"serbian":"sr",
"chinese":"zh-CN",
"slovak":"sk",
"slovenian":"sl",
"spanish":"es",
"swahili":"sw",
"swedish":"sv",
"tamil":"ta",
"telugu":"te",
"thai":"th",
"turkish":"tr",
"urdu":"ur",
"ukrainian":"uk",
"uietnamese":"vi",
"welsh":"cy"}

@app.route('/')
class HelloWorld(Resource):
    def get(self):
        language_code = 'en'
        language = request.args.get('language')
        print(language)
        try:
            language_code = language_dict[str(language).lower()]
            print(language_code)
        except Exception as e:
            print('Language not available')
        
        translator = GoogleTranslator(source='auto', target=language_code)
    
        translated_text = str(translator.translate("Hello World!"))
        return translated_text

api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    
    app.run(debug=True,host="0.0.0.0",port=8080)
