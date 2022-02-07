import requests


class OpenfoodfactsClient:
    """Client permettant de récupérer des données nutritionnelles sur
    Openfoodfacts."""

    MAX_PAGE_SIZE = 1000
    DEFAULT_PAGE_SIZE = 100

    def __init__(self, lang="fr", page_size=DEFAULT_PAGE_SIZE):
        """Initialise un nouveau client.

        Args:
            lang (str): langue du site operfoodfacts
            page_size (int): taille de la page récupérée depuis l'api
        """
        if lang not in ("fr", "en", "world", "it"):
            raise ValueError("La langue désirée n'est pas supportée")
        if page_size > self.MAX_PAGE_SIZE:
            raise ValueError(f"La taille de page max est {self.MAX_PAGE_SIZE}")
        self.url = f"https://{lang}.openfoodfacts.org/cgi/search.pl"
        self.page_size = page_size

    def get_products_by_popularity(self, page_number=1, fields=None):
        """Récupère une liste de produits sous forme de dictionnaires triés par
        popularité."""
        products = []
        for page in range(1, 1 + page_number):
            params = {
                "action": "process",
                "json": True,
                "sort_by": "unique_scans_n",
                "page_size": self.page_size,
            }
            if isinstance(fields, str):
                params['fields'] = fields

            try:
                response = requests.get(self.url, params=params)
                response.raise_for_status()
            except requests.exceptions.RequestException:
                return []

            data = response.json()
            products_data = data.get("products")
            if products_data is not None:
                products.extend(products_data)

        return products
