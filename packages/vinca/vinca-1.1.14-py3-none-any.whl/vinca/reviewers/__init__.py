import importlib

def review(card, mode):
	m = importlib.import_module('reviewers.'+card.reviewer)
	return m.review(card, mode)
