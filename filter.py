#coding:utf-8
class Filter(object):
	def filter_by_strategy(self, filter, products):
		result = []
		for product in products:
			if filter.equals(product):
				result.append(product)
		return result
		
	def by_color(self, products, product_color):
		colorFilter = ColorFilter(product_color)
		return self.filter_by_strategy(colorFilter, products)
		
	def by_size(self, products, product_size):
		sizeFilter = SizeFilter(product_size)
		return self.filter_by_strategy(sizeFilter, products)
		
	def by_color_and_size(self, products, product_color, product_size):
		sizeFilter = SizeFilter(product_size)
		sizeFilteredProducts = self.filter_by_strategy(sizeFilter, products)
		colorFilter = ColorFilter(product_color)
		return self.filter_by_strategy(colorFilter, sizeFilteredProducts)

class ColorFilter(object):
	def __init__(self, color):
		self.color = color
		
	def equals(self, product):
		return product.Color == self.color
		
class SizeFilter(object):
	def __init__(self, size):
		self.size = size
		
	def equals(self, product):
		return product.Size == self.size
		