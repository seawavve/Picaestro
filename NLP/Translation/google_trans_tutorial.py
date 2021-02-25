from google_trans_new import google_translator
translator = google_translator()  
translate_text = translator.translate('나는 가끔 내 미래가 불안할 때가 있지',lang_src='ko', lang_tgt='en')  
print(translate_text)
