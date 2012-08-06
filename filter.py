#coding:utf-8
class Filter(object):		
	def matching(self, products):
		result = []
		for product in products:
			if self.matches(product):
				result.append(product)
		return result

class ColorFilter(Filter):
	def __init__(self, color):
		self.color = color
		
	def matches(self, product):
		return product.Color == self.color
		
class SizeFilter(Filter):
	def __init__(self, size):
		self.size = size
		
	def matches(self, product):
		return product.Size == self.size
		
class MultiFilter(Filter):
	def __init__(self, *filters):
		self.filters = filters
		
	def matches(self, product):
		for filter in self.filters:
			if not filter.matches(product):
				return False
		return True
