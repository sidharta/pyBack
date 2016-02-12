from flask import jsonify, request

from . import api
from ..models.item import Item
from ..schemas.item import item_schema, items_schema


@api.route('/items', methods=['GET'])
def get_items():
    return jsonify(name='Sidharta', email='snoleto@ciandt.com')


@api.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    pass
