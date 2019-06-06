from flask import Blueprint, jsonify, request
from ..auth import login_required, authenticated_user
from .models import Ticket, Slot, Theater

book = Blueprint('book', __name__)

@book.route('/listing')
def listing():
	type_ = request.args.get('type')

	if not type_:
		return jsonify(success=False, message='Listing type is not specified'), 422

	items = [
		{
			'name': 'De De Pyar De',
			'shortDescriptions': [
				'UA',
				'Comedy',
				'Hindi',
			],
			'thumbnail': 'https://in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/de-de-pyaar-de-et00082637-28-08-2018-04-33-56.jpg',
			'slug': 'de-de-pyar-de',
		},
		{
			'name': 'De De Pyar De',
			'shortDescriptions': [
				'UA',
				'Comedy',
				'Hindi',
			],
			'thumbnail': 'https://in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/de-de-pyaar-de-et00082637-28-08-2018-04-33-56.jpg',
			'slug': 'de-de-pyar-de',
		},
		{
			'name': 'De De Pyar De',
			'shortDescriptions': [
				'UA',
				'Comedy',
				'Hindi',
			],
			'thumbnail': 'https://in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/de-de-pyaar-de-et00082637-28-08-2018-04-33-56.jpg',
			'slug': 'de-de-pyar-de',
		},
	]

	return jsonify(success=True, items=items)

@book.route('/details/<slug>/<type>')
@login_required
def details(slug, type):
	data = {
		'name': 'De De Pyar De',
		'shortDescriptions': [
			'UA',
			'Comedy',
			'Hindi',
		],
		'thumbnail': 'https://in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/de-de-pyaar-de-et00082637-28-08-2018-04-33-56.jpg',
		'releaseDate': '17 May, 2019',
		'info': [
			'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem voluptatibus distinctio illo dicta labore dolorum, ipsam laboriosam qui assumenda quod illum quaerat, quidem libero rem magni officia repellendus, recusandae suscipit. Blanditiis facere ullam sit beatae cupiditate repellendus est aspernatur! Iste recusandae veniam consectetur, error quis et minus quas nobis ex corporis doloribus ad quia cupiditate enim, inventore delectus consequuntur ducimus, hic vero. Voluptatum, vero fuga sequi esse dolore ut cupiditate impedit. Asperiores maiores tenetur doloremque? Ea quos similique dignissimos aspernatur odio animi laboriosam eligendi consequuntur quia eius accusantium laudantium cum fuga, ab facere tenetur. Eos cumque minus quas deleniti culpa quaerat qui, laborum voluptate modi repellat quos, molestiae perferendis molestias. Eos unde ipsam saepe repellat, vel ipsum culpa quod officiis!',
			'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem voluptatibus distinctio illo dicta labore dolorum, ipsam laboriosam qui assumenda quod illum quaerat, quidem libero rem magni officia repellendus, recusandae suscipit. Blanditiis facere ullam sit beatae cupiditate repellendus est aspernatur! Iste recusandae veniam consectetur, error quis et minus quas nobis ex corporis doloribus ad quia cupiditate enim, inventore delectus consequuntur ducimus, hic vero. Voluptatum, vero fuga sequi esse dolore ut cupiditate impedit. Asperiores maiores tenetur doloremque? Ea quos similique dignissimos aspernatur odio animi laboriosam eligendi consequuntur quia eius accusantium laudantium cum fuga, ab facere tenetur. Eos cumque minus quas deleniti culpa quaerat qui, laborum voluptate modi repellat quos, molestiae perferendis molestias. Eos unde ipsam saepe repellat, vel ipsum culpa quod officiis!',
		],
	}

	return jsonify(success=True, data=data)

@book.route('/theaters/has/movie/<slug>')
def theaters(slug):
	theaters = [
		{
			'name': 'Carnival: Himalaya Mall',
			'slots': [
				'12:05 AM',
				'03:15 PM',
				'06:25 PM',
				'09:45 PM',
			]
		},
		{
			'name': 'Carnival: Himalaya Mall',
			'slots': [
				'08:15 PM',
				'10:45 PM',
			]
		},
		{
			'name': 'Carnival: Himalaya Mall',
			'slots': [
				'08:15 PM',
				'10:45 PM',
			]
		},
		{
			'name': 'Carnival: Himalaya Mall',
			'slots': [
				'08:15 PM',
				'10:45 PM',
				'10:45 PM',
			]
		},
		{
			'name': 'Carnival: Himalaya Mall',
			'slots': [
				'08:15 PM',
				'10:45 PM',
			]
		},
	]

	return jsonify(success=True, theaters=theaters)
