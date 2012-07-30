#coding:utf-8
import unittest
from filter import Filter
from product import Product
from product_color import ProductColor
from product_size import ProductSize

class TestFilter(unittest.TestCase):
	def test_filter_by_blue_return_2(self):
		filter = Filter()
		products = BuildProducts()
		
		result = filter.by_color(products, ProductColor.Blue)
		
		self.assertEqual(2, len(result))
		for product in result:
			self.assertEqual(product.Color, ProductColor.Blue)
			
	def test_filter_by_small_return_2(self):
		filter = Filter()
		products = BuildProducts()
		
		result = filter.by_size(products, ProductSize.Small)
		
		self.assertEqual(2, len(result))
		for product in result:
			self.assertEqual(product.Size, ProductSize.Small)
			
	def test_filter_by_blue_and_small_return_1(self):
		filter = Filter()
		products = BuildProducts()
		
		result = filter.by_color_and_size(products, ProductColor.Blue, ProductSize.Small)
		
		self.assertEqual(1, len(result))
		for product in result:
			self.assertEqual(product.Color, ProductColor.Blue)
			self.assertEqual(product.Size, ProductSize.Small)
			
def BuildProducts():
	return [
		Product(ProductColor.Blue, ProductSize.Small), 
		Product(ProductColor.Yellow, ProductSize.Small), 
		Product(ProductColor.Yellow, ProductSize.Medium), 
		Product(ProductColor.Red, ProductSize.Large), 
		Product(ProductColor.Blue, ProductSize.ReallyBig)
	]

def run_tests():
    """Método para iniciar la sesión de testeo"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFilter)
    unittest.TextTestRunner(verbosity=2).run(suite)

#corremos los tests sólo si fuimos llamados desde la consola
if __name__ == "__main__":
    run_tests()