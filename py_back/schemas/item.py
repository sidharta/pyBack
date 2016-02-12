from .. import ma
from ..models.item import Item


class ItemSchema(ma.Schema):

    class Meta:
        fields = ('id', 'desc')


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
