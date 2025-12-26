import unittest
import sys
import os

# Ajouter le dossier src au path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        """Configuration avant chaque test"""
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        """Test de la page d'accueil"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'healthy')
        self.assertEqual(data['service'], 'myapp')

    def test_health(self):
        """Test du health check"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'ok')

    def test_ready(self):
        """Test du readiness check"""
        response = self.app.get('/ready')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'ready')

    def test_info(self):
        """Test de l'endpoint info"""
        response = self.app.get('/api/info')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('application', data)
        self.assertIn('version', data)

    def test_echo(self):
        """Test de l'endpoint echo"""
        response = self.app.get('/api/echo/hello')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'hello')
        self.assertEqual(data['echo'], 'HELLO')

    def test_404(self):
        """Test d'une route inexistante"""
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
