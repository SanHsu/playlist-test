import re

TAG = 'session'

def get_element_length(elements):
	return len(re.findall(TAG, elements))

def get_text_set(elements, texts=[]): 
	values = set(map(lambda item: item.text, elements))
	return list(set(texts) | values)