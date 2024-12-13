import unittest

if __name__ == "__main__":
    # Busca todas las pruebas en el módulo 'tests'
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests", pattern="*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
