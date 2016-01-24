import json
import os
from flask import Flask, Response, request

app = Flask(__name__, static_url_path='', static_folder='')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

@app.route('/api/albums', methods=['GET'])
def albums_controller():
	albums = [
		{
			'image': 'https://images-na.ssl-images-amazon.com/images/I/41Xehm3A6AL._SS280.jpg',
			'amazonUrl': 'https://www.amazon.com/gp/product/B005LL8708',
			'itunesUrl': 'https://itunes.apple.com/us/album/major-minor-bonus-track-version/id722641259',
			'name': 'Major/Minor',
			'artist': 'Thrice'
		},
		{
			'image': 'http://ecx.images-amazon.com/images/I/41g1r2T9AWL._SY300_QL70_.jpg',
			'amazonUrl': 'http://www.amazon.com/Watershed-OPETH/dp/B0018CWWFK',
			'itunesUrl': 'https://itunes.apple.com/us/album/watershed-special-edition/id277989716',
			'name': 'Watershed',
			'artist': 'Opeth'
		},
		{
			'image': 'https://images-na.ssl-images-amazon.com/images/I/41GjZKJNXCL._SS280.jpg',
			'amazonUrl': 'https://www.amazon.com/gp/product/B00E5E1H8Q',
			'itunesUrl': 'https://itunes.apple.com/us/album/loveboat/id675447595',
			'name': 'Loveboat',
			'artist': 'Erasure'
		},
		{
			'image': 'http://ecx.images-amazon.com/images/I/51JL3BDIAZL.jpg',
			'amazonUrl': 'http://www.amazon.com/One-World-Martyn-John/dp/B000025XJT',
			'itunesUrl': 'https://itunes.apple.com/us/album/one-world-deluxe-edition/id995260831',
			'name': 'One World',
			'artist': 'John Martyn'
		},
		{
			'image': 'http://ecx.images-amazon.com/images/I/51Kx3Lhnd1L.jpg',
			'amazonUrl': 'http://www.amazon.com/Volumes-Mirimar-Disaster/dp/B001C3MYE4',
			'itunesUrl': 'https://itunes.apple.com/us/album/volumes-ep/id287395963',
			'name': 'Volumes',
			'artist': 'The Mirimar Disaster'
		},
	]

	return Response(json.dumps(albums), mimetype='application/json', headers={'Cache-Control': 'no-cache'})


if __name__ == '__main__':
	app.run(port=int(os.environ.get("PORT", 3000)))
