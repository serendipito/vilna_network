# This file is responsible for generating family network data (without any biographical data).

import pandas as pd
import graphviz
from graphviz import Digraph
import random
import wikipedia

# A few custom-defined settings
colors=[ "#E8E9F3",  "#CECECE",  "#A6A6A8",  "#B1E5F2",  "#CBBEB3", '#F0F3BD']

# This database is taken from the Vilna Troupe project and can be found at http://vilnatroupe.com
# It is not included in the current dataset for reasons of rights and updatability.
df = pd.read_excel("current_database.xls")

# The code below parses the original file and saves it as connections:
members = df.loc[:,["Full Name"]].values.tolist()
members = [x[0] for x in members if isinstance(x[0], str)]
connections_list = df.iloc[:, 19:39].values.tolist()
connections = {}
for member in members:
	connections[member] = []

# The code below adds all connections to the table:
i = 0
for connection in connections_list:
	links = [x for x in connection if isinstance(x, str)]
	member = members[i]
	k = 0
	for link in links:
		if k%2 == 0:
			connections[member].append({"name": link, "type": links[k+1]})
		k+=1
	i+=1

#dot = Digraph(name='Vilna network', comment='Network of the Vilna Group', layout='neato')
dot = graphviz.Graph(engine='circo')
dot.attr('node', center='true', shape='oval',style="filled",fillcolor='darkolivegreen2',color='red')
dot.attr('edge', style='filled',color='grey48')


for member in members:

	summary = ''
	if include_biographies:
		try:
			summary = wikipedia.summary(member)
		except:
			summary = ''

	col = random.choice(colors)
	if len(connections[member]) > 0:
		dot.node(member, color=col,fillcolor=col, xlabel=summary)
	else:
		other_connect = False
		for conn in connections:
			list_of_contacts = connections[conn]
			for c in list_of_contacts:
				if c.get('name') == member:
					other_connect = True
		if other_connect == True:
			dot.node(member, color=col,fillcolor=col, xlabel=summary)

	# The code below is largely preocupied with excluding redundant connections and then creaitng the edges.
	for connection in connections[member]:
		name = connection.get('name')
		ctype = connection.get('type')
		if name in members:
			
			direction = 'forward'
			conns_connections = connections[name]

			bidirectional_conns_connections = list(filter(lambda x: (x.get("name") == member and (x.get('type') == 'Husband' or x.get('type') == 'Wife')), conns_connections))
			if(len(bidirectional_conns_connections)	> 0):
				direction = 'both'	
				ctype = "Married"

			bidirectional_conns_connections = list(filter(lambda x: (x.get("name") == member and (x.get('type') == 'Cousin' and x.get('type') == ctype)), conns_connections))
			if(len(bidirectional_conns_connections)	> 0):
				direction = 'both'	
				ctype = "Cousins"

			bidirectional_conns_connections = list(filter(lambda x: (x.get("name") == member and (x.get('type') == 'Brother' and x.get('type') == ctype)), conns_connections))
			if(len(bidirectional_conns_connections)	> 0):
				direction = 'both'	
				ctype = "Brothers"

			bidirectional_conns_connections = list(filter(lambda x: (x.get("name") == member and (x.get('type') == 'Sister' and x.get('type') == ctype)), conns_connections))
			if(len(bidirectional_conns_connections)	> 0):
				direction = 'both'	
				ctype = "Sisters"
				

			bidirectional_conns_connections = list(filter(lambda x: (x.get("name") == member and (x.get('type') == 'Brother-in-law' and x.get('type') == ctype)), conns_connections))
			if(len(bidirectional_conns_connections)	> 0):
				direction = 'both'	
				ctype = "Brothers-in-law"

			bidirectional_conns_connections = list(filter(lambda x: (x.get("name") == member and (x.get('type') == 'Sister-in-law' and x.get('type') == ctype)), conns_connections))
			if(len(bidirectional_conns_connections)	> 0):
				direction = 'both'	
				ctype = "Sisters-in-law"

			if direction == 'both' and members.index(member) > members.index(name):
				pass
			else:
				dot.edge(member, name, label=ctype, dir=direction)
			

dot.view()
