var TileContentComponent = React.createClass({
	render: function() {
		return (
			<div className="tileContentComponent tileContent">
				<img src={this.props.album.image} />
				<div>
					<span>{this.props.album.name}</span><br />
					<span>{this.props.album.artist}</span>
				</div>
			</div>
		);
	}
});

var TileComponent = React.createClass({
	render: function() {
		return (
			<div className="tileComponent tile">
				<TileContentComponent album={this.props.album} />
			</div>
		);
	}
});

var TilesComponent = React.createClass({
	loadAlbumsFromServer: function() {
		$.ajax({
			url: this.props.url,
			dataType: 'json',
			cache: false,
			success: function(albums) {
				this.setState({albums: albums});
			}.bind(this),
			error: function(xhr, status, err) {
				console.error(this.props.url, status, err.toString());
			}.bind(this)
		});
	},
	getInitialState: function() {
		return {albums: []};
	},
	componentDidMount: function() {
		this.loadAlbumsFromServer();
	},
	render: function() {
		var tiles = this.state.albums.map(function(album) {
			return (
				<TileComponent album={album} />
			);
		});
		return (
			<div className="tilesComponent container">
				{tiles}
			</div>
		);
	}
});

ReactDOM.render(
  <TilesComponent url='/api/albums' />,
  document.getElementById('main')
);
