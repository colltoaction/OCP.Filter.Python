#coding:utf-8
class Filter(object):
	def by_color(self, products, product_color):
		result = []
		for product in products:
			if product.Color == product_color:
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
