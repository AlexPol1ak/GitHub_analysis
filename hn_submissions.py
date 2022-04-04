from operator import itemgetter
import requests
from plotly.graph_objs import Bar 
from  plotly import offline

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
#print(f"Status code: {r.status_code}")

sumbission_ids = r.json()
sumbission_dicts = []
for sumbission_id in sumbission_ids[:30]:
	url = f"https://hacker-news.firebaseio.com/v0/item/{sumbission_id}.json"
	r = requests.get(url)
	#print(f"id {sumbission_id}\tstatus: {r.status_code}.")
	response_dict = r.json()
	#print(response_dict)

	sumbission_dict = {
	'title': response_dict['title'],
	'hn_link': f"https://news.ycombinator.com/item?id={sumbission_id}",
	'comments': response_dict.get('descendants', 1),
	}
	sumbission_dicts.append(sumbission_dict)

sumbission_dicts = sorted(sumbission_dicts, key=itemgetter('comments'), reverse=True)

comm, header, urls, labs = [], [], [], []
for sumbission_dict in sumbission_dicts:
	print(f"\nTilte: {sumbission_dict['title']} ")
	print(f"\nDescussion link: {sumbission_dict['hn_link']} ")
	print(f"\nComments: {sumbission_dict['comments']} ")
	comm.append(sumbission_dict['comments'])
	header.append(sumbission_dict['title'])
	urls.append(sumbission_dict['hn_link'])
	link_title = f"<a href='{sumbission_dict['hn_link']}'>{sumbission_dict['title']}</a>"
	labs.append(link_title)

data = [{
	'type': 'bar',
	'x': labs,
	'y': comm,
	'hovertext': urls,
	'marker': {
	    'color': 'blue',
	    'line': {'width': 1.5, 'color': 'red'},
	    'opacity': 0.5,
	    	}
}]

fg_layout = {
	'title': 'Discussed articles',
	'titlefont': {'size': 28},
	'xaxis': {
	    'title': 'Articles',
	    'titlefont': {'size': 24},
	    'tickfont': {'size': 12}
	},
	'yaxis': {
	    'title': 'Comments',
	    'titlefont': {'size': 24},
	    'tickfont': {'size': 12},
	},
}

fig = {'data': data, 'layout': fg_layout}
offline.plot(fig, filename='Popular_Articles.html')


