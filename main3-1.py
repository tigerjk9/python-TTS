from gtts import gTTS

text = "안녕하세요. 파이썬 공부를 열심히 하는군요. 응원합니다."

tts = gTTS(text=text, lang='ko')  #text변수의 문자열을 ko(한글)로 변환하여 tts변수에 바인딩한다.
tts.save(r"3. 텍스트를 음성으로 변환\hi.mp3")  #[3. 텍스트를 음성으로 변환] 폴더에 hi.mp3의 파일이름으로 저장한다. AI 프로그래밍이라는 폴더에서 상대 경로로 지정되었음. 