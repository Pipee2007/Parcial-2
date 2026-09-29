import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

centro = "Andres (Pipe)"

familia = ["Angela", "Andersson", "Gladys", "Alvaro", "Isabel"]
amigos = ["Sofia", "Snaider", "Paula", "Pencue", "JP"]
companeros = ["Santiago", "Andy", "Adrian", "Mauricio"]

G.add_node(centro, grupo="Centro")

for p in familia:
    G.add_node(p, grupo="Familia")

for p in companeros:
    G.add_node(p, grupo="Companeros")

for p in amigos:
    G.add_node(p, grupo="Amigos")

for p in familia + amigos + companeros:
    G.add_edge(centro, p)

G.add_edge("Alvaro", "Gladys")
G.add_edge("Gladys", "Andersson")
G.add_edge("Alvaro", "Andersson")
G.add_edge("Angela", "Isabel")

for i in range(len(amigos)):
    for j in range(i + 1, len(amigos)):
        G.add_edge(amigos[i], amigos[j])

G.add_edge("Santiago", "Andy")
G.add_edge("Adrian", "Mauricio")

pos = {
    "Andres (Pipe)": (0, 0),
    
    "Angela": (-5.0, 3.0),
    "Andersson": (-4.5, 1.2),
    "Gladys": (-5.2, -0.5),
    "Alvaro": (-4.2, -2.2),
    "Isabel": (-4.8, -3.8),
    
    "Santiago": (-2.0, -5.0),
    "Andy": (-0.5, -5.2),
    "Adrian": (1.0, -5.0),
    "Mauricio": (2.5, -4.8),
    
    "Sofia": (2.2, 5.0),
    "Snaider": (3.8, 4.2),
    "Paula": (4.8, 2.8),
    "Pencue": (5.2, 1.0),
    "JP": (4.5, -0.8)
}

colores_mapa = {
    "Centro": "#2ecc71",
    "Familia": "#9b59b6",
    "Companeros": "#e67e22",
    "Amigos": "#e74c3c"
}
colores_nodos = [colores_mapa[G.nodes[n]["grupo"]] for n in G.nodes()]

plt.figure(figsize=(15, 11))

nx.draw_networkx_nodes(G, pos, node_color=colores_nodos, node_size=3600, edgecolors="black", linewidths=1.5)
nx.draw_networkx_edges(G, pos, width=1.2, alpha=0.35, edge_color="gray", arrows=False)
nx.draw_networkx_labels(G, pos, font_size=8, font_family="sans-serif", font_weight="bold")

plt.axis("off")
plt.tight_layout()
plt.show()