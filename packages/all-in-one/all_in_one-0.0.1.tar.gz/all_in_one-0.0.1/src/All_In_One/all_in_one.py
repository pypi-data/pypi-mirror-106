import time
import threading
import vidstream
import pyautogui
import os
import cv2
import vpython
import smtplib
import socket
import webbrowser
import pyttsx3
import speech_recognition as sr
import gtts
import logging
import pynput
import winsound

class VoiceRecieveError(Exception) :
	pass

class CamBaseException(Exception) :
	pass

class WebException(Exception) :
	pass	

class Sound :
	def text_to_speech(self, text) :
		engine = pyttsx3.init()
		engine.say(text)
		engine.runAndWait()

	def save_tts(self, text, fOut) :
		return gtts.gTTS(text).save(fOut)

	def speech_to_text(self) :
		with sr.Microphone() as source :
			audio = sr.Recognizer().listen(source)
			try :
				return sr.Recognizer().recognize_google(audio)
			except :
				raise VoiceRecieveError("Unable to receive voice from microphone")

	def play_audio(self, audio_file, flags):
		winsound.PlaySound(audio_file, flags)

	def play_beep(self, frequency, duration) :
		winsound.Beep(frequency, duration)

	def play_msgBeep(self) :
		winsound.MessageBeep()					

class CamImage :
	def screenshot(self) :
		try :
			return pyautogui.screenshot()
		except :
			raise CamBaseException("Unable to take screenshot") 	

	def open_webcam(self, win_title, webcam_no, quit_key) :
		try :
			cap = cv2.VideoCapture(webcam_no)
			while True :
				ret, img = cap.read()
				cv2.imshow(win_title, img)
				if cv2.waitKey(10) == quit_key :
					break
			cap.release()		
			cv2.destroyAllWindows()
		except :
			raise CamBaseException("Some error occured")

class Virt3D :
	def draw_uiSquare(self) :
		try :
			vpython.box()
		except :
			pass	

	def draw_uiCircle(self) :
		try :
			vpython.ring()
		except :
			pass	

	def draw_arrow(self) :
		try :
			vpython.arrow()
		except :
			pass

class Keyboard :
	def combi_key(self, key1, key2) :
		pyautogui.hotkey(key1, key2)

	def hit_key(self, key) :
		pyautogui.press(key)

	def type_keys(self, chars) :
		pyautogui.typewrite(chars)

	def save_logs(self, fOut) :
		logging.basicConfig(filename=(fOut), level=logging.DEBUG)
		def onPress(key) :
			logging.info(str(key))

		with pynput.keyboard.Listener(on_press=onPress) as listener :
			listener.join()	

class Mouse :
	def click(self, x, y) :
		pyautogui.click(x, y)

	def left_click(self, x, y) :
		pyautogui.leftClick(x, y)

	def right_click(self, x, y) :
		pyautogui.rightClick(x, y)

	def middle_click(self, x, y) :
		pyautogui.middleClick(x, y)

	def double_click(self, x, y) :
		pyautogui.doubleClick(x, y)

	def triple_click(self, x, y) :
		pyautogui.tripleClick(x, y)

	def move(self, x, y) :
		pyautogui.move(x, y)

class Network :
	def video_chat_as_streamer(self, start_end, receiving_end, port) :
		client = vidstream.StreamingServer(start_end, port)
		receiver = vidstream.CameraClient(receiving_end, port)
		t2 = threading.Thread(target=receiver.start_stream)
		t2.start()
		time.sleep(2)
		t1 = threading.Thread(target=client.start_server)
		t1.start()
		time.sleep(2)
		client.stop_server()
		receiver.stop_stream()

	def video_chat_as_receiver(self, start_end, receiving_end, port) :
		receiver = vidstream.StreamingServer(receiving_end, 5555)
		client = vidstream.CameraClient(start_end, 5555)
		t1 = threading.Thread(target=client.start_stream)
		t1.start()
		time.sleep(2)
		t2 = threading.Thread(target=receiver.start_server)
		t2.start()
		time.sleep(2)
		while input("") != "STOP" :
		    continue
		receiver.stop_server()
		client.stop_stream()

class Web :
	def open_browser(self, url) :
		webbrowser.open(url)
	def open_in_new_tab(self, url) :
		webbrowser.open_new_tab(url)
	def open_in_new_window(self, url) :
		webbrowser.open_new(url)

class Mail :
	def set_mail_creds(self, mail_username, mail_password) :
		self.username = mail_username
		self.password = mail_password

	def mail_to(self, server, server_port, to_addr, from_addr, message) :
		s = smtplib.SMTP(server, server_port)
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(self.username, self.password)
		s.sendmail(from_addr, to_addr, message)

class Open :
	def Chrome(self) :
		os.system("start chrome")
	def Firefox(self) :
		os.system("start firefox")
	def MS_Edge(self) :
		os.system("start msedge")
	def Notepad(self) :
		os.system("notepad.exe")
	def Paint(self) :
		os.system("mspaint")
	def PowerShell(self) :
		os.system("start powershell")
	def CMD(self) :
		os.system("start")
	def File_Explorer(self) :
		os.system("explorer")