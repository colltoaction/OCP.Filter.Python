#coding:utf-8
class Filter(object):
	def by_color(self, products, product_color):
		colorFilter = ColorFilter(product_color)
		result = []
		for product in products:
			if colorFilter.equals(product):
				result.append(product)
		return result
		
	def by_size(self, products, product_size):
		result = []
		for product in products:
			if product.Size == product_size:
				result.append(product)
		return result
		
	def by_color_and_size(self, products, product_color, product_size):
		result = []
		for product in products:
			if product.Color == product_color and product.Size == product_size:
				result.append(product)
		return result

class ColorFilter(object):
	def __init__(self, color):
		self.color = color
		
	def equals(self, product):
		return product.Color == self.color
		