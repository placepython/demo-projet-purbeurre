from pprint import pprint
import json

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
        "categories": "Cereal clusters with nuts",
        "code": "3168930010265",
        "generic_name": "Pépites de céréales croustillantes avec Mélange de Noix",
        "nutriscore_grade": "a",
        "product_name": "Cruesli Mélange de noix",
        "stores": "Intermarché,Magasins U, carrefour.fr",
        "url": "https://fr.openfoodfacts.org/produit/3168930010265/cruesli-melange-de-noix-quaker",
    },
]


def transform_fields_into_lowercase_letters(product):
    fields = {
        "product_name",
        "categories",
        "stores",
        "nutriscore_grade",
        "generic_name",
    }
    for field in fields:
        product[field] = product[field].lower()


def transform_fields_into_lists(product):
    fields = {"categories", "stores"}
    for field in fields:
        product[field] = [
            element.strip() for element in product[field].split(",")
        ]


class ProductNormalizer:
    """Objet responsable de normaliser les données pour chaque produit reçu de
    l'API."""

    normalizer_functions = [
        transform_fields_into_lowercase_letters,
        transform_fields_into_lists,
    ]

    def normalize(self, products):
        """Modifie les dictionnaires de products pour normaliser les données
        qu'ils contiennent."""
        for product in products:
            for fonction in self.normalizer_functions:
                fonction(product)


def test():
    normalizer = ProductNormalizer()
    normalizer.normalize(fake_data)

    with open("mesdonnee.json", "w") as json_file:
        json.dump(fake_data, json_file, indent=4)


if __name__ == '__main__':
    test()
