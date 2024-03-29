import datetime
from haystack import indexes
from web.models import Product, Seller


class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #seller = indexes.ForeignKey(Seller)
    category = indexes.CharField(model_attr = 'category')

    def get_model(self):
        return Product

    # def index_queryset(self, using=None):
    #     """Used when the entire index for model is updated."""
    #     return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

