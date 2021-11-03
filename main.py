#pylint:disable=W0235
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from re import compile

class MyLayout(Widget):
	def __init__(self, *args):
		super(MyLayout, self).__init__(*args)
		
		self.actions = ["+", "-", "*", "÷"]
		
	def exit(self):
		pass
	
	def clear(self):
		self.ids.show.text = "0"
	
	def remove(self):
		self.ids.show.text = self.ids.show.text[:-1]
		
	def button_press(self, button):
		prior = self.ids.show.text
		
		if prior == "Error":
			self.ids.show.text = str(button)
		elif prior == "0":
			self.ids.show.text = f"{button}"
		else:
			self.ids.show.text = f"{prior}{button}"
			
	def math_sign(self, sign):
		prior = self.ids.show.text
		
		
		if prior == "0" and sign == "-":
			self.ids.show.text = "-"
		elif prior[-1] in ["+", "-", "/", "%"]:
			return None
		elif prior == "0":
			self.ids.show.text = sign
		elif len(prior) > 1 and prior[-1] == "*" and prior[-2] == "*" and sign == "*":
			return None
		else:
			self.ids.show.text = f"{prior}{sign}"
	
	def dot(self):
		prior = self.ids.show.text
		prior2 = self.ids.show.text
		
		all_marks = [0]
		
		action = compile("[+,-,/,*]")
		for i in action.finditer(prior):
			print(i.start())
			all_marks.append(i.start())
		all_marks.append(len(prior))
		
		parts = [prior[all_marks[i]:all_marks[i+1]] for i in range(len(all_marks)-1)]
		
		if parts[-1] == "0":
			self.ids.show.text = f"{prior2}."
		elif "." in parts[-1]:
			return None
		else:
			self.ids.show.text = f"{prior2}."
		
	
	
	def reverse(self):
		prior = self.ids.show.text
		
		if prior == "0" or prior == "":
			return None
		elif prior[0] == "+":
			self.ids.show.text = f"-{prior[1:]}"
		elif prior[0] != "-":
			self.ids.show.text = f"-{prior}"
		elif "-" in prior:
			self.ids.show.text = prior.replace("-", "+")
		else:
			self.ids.show.text = prior.replace("+", "-")
		
		
	
	def total(self):
		prior = self.ids.show.text
		try:
			if prior[-1] in self.actions:
				self.ids.show.text = str(eval(prior[:-1]))
			else:
				self.ids.show.text = str(eval(prior))
		except:
			self.ids.show.text = "Error"
		

class MainApp(App):
	def build(self):
		return MyLayout()


if __name__ == "__main__":
	MainApp().run()