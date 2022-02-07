from pprint import pprint

fake_data = [
    {
        "categories": "Beverages,Waters,Spring waters,Mineral waters,Natural mineral waters",
        "code": "3274080005003",
        "generic_name": "Eau de source naturelle",
        "nutriscore_grade": "a",
        "product_name": "Eau de source Cristaline Etat Naturel",
        "stores": "Carrefour,Leclerc,Auchan,Intermarché",
        "url": "https://fr.openfoodfacts.org/produit/3274080005003/eau-de-source-cristaline-etat-naturel",
    },
    {
        "categories": "Snacks,Snacks sucrés,Biscuits et gâteaux,Biscuits,Biscuits au chocolat",
        "code": "7622210449283",
        "generic_name": "BISCUITS FOURRÉS (35%) PARFUM CHOCOLAT",
        "nutriscore_grade": "d",
        "product_name": "Prince Chocolat",
        "stores": "Carrefour Market,Magasins U,Auchan,Intermarché,Carrefour,Casino,Leclerc,Cora,Bi1, carrefour.fr",
        "url": "https://fr.openfoodfacts.org/produit/7622210449283/prince-chocolat-lu",
    },
    {
        "categories": "Produits à tartiner,Petit-déjeuners,Produits à tartiner sucrés,Pâtes à tartiner,Pâtes à tartiner aux noisettes,Pâtes à tartiner au chocolat,Pâtes à tartiner aux noisettes et au cacao",
        "code": "3017620425035",
        "generic_name": "Pâte à tartiner aux noisettes",
        "nutriscore_grade": "e",
        "product_name": "Nutella",
        "stores": "Auchan, carrefour.fr",
        "url": "https://fr.openfoodfacts.org/produit/3017620425035/nutella-ferrero",
    },
    {
        "categories": "Snacks,Sweet snacks,Biscuits and cakes,Biscuits",
        "code": "3175680011480",
        "generic_name": "Biscuits au sésame",
        "nutriscore_grade": "b",
        "product_name": "Sésame",
        "stores": "E.Leclerc,Carrefour,Auchan,Monoprix, carrefour.fr",
        "url": "https://fr.openfoodfacts.org/produit/3175680011480/sesame-gerble",
    },
    {
        "categories": "Snacks,Snacks sucrés,Cacao et dérivés,Chocolats,Chocolats noirs,Chocolat noir en tablette extra dégustation à 70% de cacao minimum",
        "code": "3046920022651",
        "nutriscore_grade": "e",
        "product_name": "Excellence 70% Cacao Noir Intense",
        "stores": "Magasins U,Carrefour, carrefour.fr",
        "url": "https://fr.openfoodfacts.org/produit/3046920022651/excellence-70-cacao-noir-intense-lindt",
    },
    {
        "categories": "Cereal clusters with nuts",
        "code": "3168930010265",
        "generic_name": "Pépites de céréales croustillantes avec Mélange de Noix",
        "nutriscore_grade": "a",
        "product_name": "Cruesli Mélange de noix",
        "stores": "Intermarché,Magasins U, carrefour.fr",
        "url": "https://fr.openfoodfacts.org/produit/3168930010265/cruesli-melange-de-noix-quaker",
    },
]


def validate_fields_are_present_in_product(product):
    fields = {
        "code",
        "product_name",
        "categories",
        "stores",
        "nutriscore_grade",
        "url",
        "generic_name",
    }
    if fields - product.keys():
        return False
    return True


def validate_fields_are_not_empty_in_product(product):
    fields = {
        "code",
        "product_name",
        "categories",
        "stores",
        "nutriscore_grade",
        "url",
        "generic_name",
    }
    for field in fields:
        if isinstance(product[field], str) and not product[field].strip():
            return False
    return True


class ProductValidator:
    """Objet responsable de filtrer les produits contenues une liste selon
    certains critères."""

    validator_functions = [
        validate_fields_are_present_in_product,
        validate_fields_are_not_empty_in_product,
    ]

    def is_valid(self, product):
        """Retourne True si le produit passé en argument est considéré comme
        valide."""
        for function in self.validator_functions:
            if not function(product):
                return False
        return True

    def clean(self, products):
        """Supprime les produits non valides de la liste products."""
        cleaned_data = []
        for product in products:
            if self.is_valid(product):
                cleaned_data.append(product)
        return cleaned_data


def test():
    validator = ProductValidator()
    products = validator.clean(fake_data)
    pprint(products)


if __name__ == '__main__':
    test()
