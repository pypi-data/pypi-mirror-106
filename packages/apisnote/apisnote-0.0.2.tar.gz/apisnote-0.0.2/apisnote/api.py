import requests


class Note:
	
	
	def __init__(self, apikey):
		self.apikey = apikey
	
	
	def _get(self, method: str, **kwargs):
		r = requests.get(f"https://apis.kgbot.pp.ua/api/{method}", params=kwargs)
		return r.json()
		
	
	def addNote(self, name: str, content: str):
		return self._get("addNote", apikey=self.apikey, name=name, content=content)
	
	
	def getNote(self, name: str):
		return self._get("getNote", apikey=self.apikey, name=name)
	
	
	def getNoteList(self):
		return self._get("getNoteList", apikey=self.apikey)
	
	
	def removeNote(self, name: str):
		return self._get("removeNote", apikey=self.apikey, name=name)
	
	
	def editNote(self, name: str, content: str):
		return self._get("editNote", apikey=self.apikey, name=name, content=content)