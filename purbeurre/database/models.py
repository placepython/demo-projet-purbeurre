from purbeurre.database import db


class Product:
    """Représente un produit géré par notre programme."""

    def __init__(
        self,
        code=None,
        product_name=None,
        generic_name=None,
        nutriscore_grade=None,
        url=None,
    ):
        """Initialise un nouveau produit."""
        self.code = code
        self.name = product_name
        self.decription = generic_name
        self.nutriscore = nutriscore_grade
        self.url = url

    @classmethod
    def create_table(cls):
        cursor = db.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS product (
                code INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                nutriscore TEXT NOT NULL,
                url TEXT NOT NULL
            )
            """
        )
        db.commit()


class Category:
    """Représente une des catégories de produits de openfoodfacts."""

    def __init__(self, id_=None, name=None):
        """Initialise une nouvelle catégorie."""
        self.id = id_
        self.name = name

    @classmethod
    def create_table(cls):
        cursor = db.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS category (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            """
        )
        db.commit()


class Store:
    """Représente un des magasins listé sur openfoofacts."""

    def __init__(self, id_=None, name=None):
        """Initialise un nouveau magasin."""
        self.id = id_
        self.name = name

    @classmethod
    def create_table(cls):
        cursor = db.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS store (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """
        )
        db.commit()


class ProductCategory:
    """Représente l'association entre un produit et ses catégories et
    symétriquement entre une catégorie et ses produits."""

    def __init__(self, product=None, category=None):
        self.product_code = product.code
        self.category_id = category.id


class ProductStore:
    """Représente l'association entre un produit et ses magasins et
    symétriquement entre un magasin et ses produits."""

    def __init__(self, product=None, store=None):
        self.product_code = product.code
        self.store = store.id
