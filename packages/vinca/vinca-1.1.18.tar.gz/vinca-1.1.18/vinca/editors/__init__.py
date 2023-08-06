import importlib

def edit(card, mode):
	m = importlib.import_module('editors.' + card.editor)
	return m.edit(card, mode)
