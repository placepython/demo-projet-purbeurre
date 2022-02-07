from http.client import responses
import pytest

from purbeurre.api import clients


@pytest.fixture
def fake_api_data(monkeypatch):
    """Simulation de 3 réponses de l'API de openfoodfacts."""

    class FakeResponse:
        responses = iter(
            [
                {
                    "products": [
                        {"product_name": "product in page 1"},
                    ]
                },
                {
                    "products": [
                        {"product_name": "product in page 2"},
                        {"product_name": "product in page 2"},
                    ]
                },
                {
                    "products": [
                        {"product_name": "product in page 3"},
                        {"product_name": "product in page 3"},
                        {"product_name": "product in page 3"},
                    ]
                },
            ]
        )

        def json(self):
            return next(self.responses)

        def raise_for_status(self):
            pass

    def fake_request_get(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr("purbeurre.api.clients.requests.get", fake_request_get)


class TestOpenfoodfactsClient:
    def test_get_products_by_popularity_returns_zero_page_of_products(
        self, fake_api_data
    ):
        """Vérifie que lorsque l'API ne retourne aucun produit, la méthode
        get_products_by_popularity retourne une liste vide."""
        client = clients.OpenfoodfactsClient()
        products = client.get_products_by_popularity(page_number=0)
        assert isinstance(products, list)
        assert len(products) == 0

    def test_get_products_by_popularity_returns_one_page_of_products(
        self, fake_api_data
    ):
        """Vérifie que lorsque l'API retourne une page de produit, la méthode
        get_products_by_popularity retourne une liste contenant les bon
        produits."""
        client = clients.OpenfoodfactsClient()
        products = client.get_products_by_popularity(page_number=1)
        product_names = [product['product_name'] for product in products]
        assert isinstance(products, list)
        assert len(products) == 1
        assert "2" not in ",".join(product_names)
        assert "3" not in ",".join(product_names)

    def test_get_products_by_popularity_returns_one_page_of_products_by_default(
        self, fake_api_data
    ):
        """Vérifie que lorsque l'API retourne le nombre par défaut de pages de
        produit, la méthode get_products_by_popularity retourne une liste
        contenant les bon produits."""
        client = clients.OpenfoodfactsClient()
        products = client.get_products_by_popularity()
        product_names = [product['product_name'] for product in products]
        assert isinstance(products, list)
        assert len(products) == 1
        assert "2" not in ",".join(product_names)
        assert "3" not in ",".join(product_names)

    def test_get_products_by_popularity_returns_two_pages_of_products(
        self, fake_api_data
    ):
        """Vérifie que lorsque l'API retourne deux pages de produit, la méthode
        get_products_by_popularity retourne une liste contenant les bon
        produits."""
        client = clients.OpenfoodfactsClient()
        products = client.get_products_by_popularity(page_number=2)
        product_names = [product['product_name'] for product in products]
        assert isinstance(products, list)
        assert len(products) == 3
        assert "3" not in ",".join(product_names)

    def test_get_products_by_popularity_returns_three_pages_of_products(
        self, fake_api_data
    ):
        """Vérifie que lorsque l'API retourne trois pages de produit, la
        méthode get_products_by_popularity retourne une liste contenant les bon
        produits."""
        client = clients.OpenfoodfactsClient()
        products = client.get_products_by_popularity(page_number=3)
        assert isinstance(products, list)
        assert len(products) == 6
