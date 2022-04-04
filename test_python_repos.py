import unittest
import requests
import json

class TestPythonRepos(unittest.TestCase):
	"""Тестирует запросы API в 'python_repos'."""

	def setUp(self):
		"""Cоздает запрос API и выгружает json с инофрмацией."""
		self.url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
		self.headers = {'Accept': 'application/vnd.github.v3+json'}
		self.r = requests.get(self.url, headers=self.headers)
		self.response_dict = self.r.json()

	def test_status_code200(self):
		"""Тестирует статус код 200."""
		
		self.assertEqual(self.r.status_code, 200)

	def test_number_dict(self):
		"""Проверяет наличие информации в полученом файле."""

		self.assertTrue(len(self.response_dict) > 0)

	def test_kyes_dict(self):
		"""Проверяет ключи  полученого словаря."""

		self.keys = []
		for key in self.response_dict:
			self.keys.append(key)
		
		self.assertIn('items', self.keys)
		self.assertIn('total_count', self.keys)
		self.assertIn('incomplete_results', self.keys)






if __name__ == '__main__':
	unittest.main()
