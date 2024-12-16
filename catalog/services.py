from catalog.models import Category, Product

class ProductService:

    @staticmethod
    def get_product_by_category(category_id):
        """Функция получает все продукты в выбранной категории"""
        products_by_category = Product.objects.filter(category=category_id)

        return products_by_category


class CategoryService:

    @classmethod
    def get_categories(cls):
        """Функция получает все категории продуктов"""
        categories = Category.objects.all()

        return categories