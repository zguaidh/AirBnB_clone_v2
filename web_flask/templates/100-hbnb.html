<!DOCTYPE html>
<html lang="en">
	<head>
		<title>AirBnB clone</title>

		<link rel="shortcut icon" href="{{ url_for('static', filename='images/icon.ico') }}" >
		<link rel="stylesheet" href="{{ url_for('static', filename='styles/4-common.css') }}"/>
		<link rel="stylesheet" href="{{ url_for('static', filename='styles/3-header.css') }}" />
		<link rel="stylesheet" href="{{ url_for('static', filename='styles/6-filters.css') }}" />
		<link rel="stylesheet" href="{{ url_for('static', filename='styles/8-places.css') }}" />
		<link rel="stylesheet" href="{{ url_for('static', filename='styles/3-footer.css') }}" />
	</head>
    <body>
		<header>
			<div id="header_logo"></div>
		</header>
		<div class="container">
			<section class="filters">
				<button>Search</button>
				<div class="locations">
					<h3>States</h3>
					&nbsp;
					<ul class="popover">
						{% for state in data['State']|sort(attribute='name') %}
						<li><h2>{{ state.name }}</h2>
							<ul>
							{% for city in state.cities|sort(attribute='name') %}
								<li><h4>{{ city.name }}</h4></li>
							{% endfor %}
							</ul>
						</li>
						{% endfor %}
					</ul>
				</div>
				<div class="filter_amenities">
					<h3>Amenities</h3>
					&nbsp;
					<ul class="popover">
						{% for amenity in data['Amenity']|sort(attribute='name') %}
							<li><h4>{{ amenity.name }}</h4></li>
						{% endfor %}
					</ul>
				</div>
			</section>
			<section class="places">
				<h1>Places</h1>
				{% for place in data['Place']|sort(attribute='name') %}
					<article>
						<div class="headline">
							<h2>{{ place.name }}</h2>
							<div class="price_by_night">{{ place.price_by_night }}</div>
						</div>
						<div class="information">
							<div class="max_guest">
								<div class="guest_icon"></div>
								<p>{{ place.max_guest }} Guests</p>
							</div>
							<div class="number_rooms">
								<div class="bed_icon"></div>
								<p>{{ place.number_rooms }} Bedroom</p>
							</div>
							<div class="number_bathrooms">
								<div class="bath_icon"></div>
								<p>{{ place.number_bathrooms }} Bathrooms</p>
							</div>
							<div class="user">
								<b>Owner</b>: {{ place.user.first_name }} {{ place.user.last_name }}
							</div>
							<div class="description">
								{% set text = place.description %}
								{% set lines = text.split('<BR />') %}
								{% for line in lines %}
									{{ line }}<BR />
								{% endfor %}
							</div>
						</div>
					</article>
				{% endfor %}
			</section>
		</div>
		<footer>
			<p>Holberton School</p>
		</footer>
	</body>
</html>
