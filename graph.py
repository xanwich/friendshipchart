import matplotlib.pyplot as plt
import networkx as nx
import io
import base64

import matplotlib

matplotlib.use("agg")

# (0.53, 0.91, 0.99, 0.5)


class Grapher:
    def __init__(self, edges, color=(1, 1, 1, 0.8)):
        self.G = nx.Graph()
        self.G.add_edges_from([(e.l, e.r) for e in edges])
        self.color = color

    def make_image(self, edge_colors=None, node_colors=None):
        plt.clf()
        plt.figure(figsize=(12, 12))
        pos = nx.spring_layout(
            self.G, scale=20, k=2 / (self.G.order() ** 0.9), iterations=100
        )
        nx.draw_networkx(
            self.G,
            pos=pos,
            node_size=150,
            node_color=node_colors if node_colors else self.color,
            edge_color=edge_colors if edge_colors else self.color,
            font_family="serif",
        )
        plt.axis("off")
        img = io.BytesIO()
        plt.savefig(img, format="svg", bbox_inches="tight", transparent=True)
        img.seek(0)
        return base64.b64encode(img.getvalue()).decode("utf-8")

    def shortest_path(self, l, r):
        path = nx.shortest_path(self.G, l, r)
        return path

    def shortest_path_text(self, path):
        if len(path) > 1:
            return (
                path[0]
                + " knows "
                + " who knows ".join(path[1:])
                + f" ({len(path) - 1}°)"
            )
        elif len(path) == 1:
            return path[0] + " knows themself!"
        else:
            return "sorry"

    def make_shortest_path_image(self, path, color=(1, 0.5, 0.1, 0.8)):
        l = path[0]
        r = path[-1]
        path_edges = list(zip(path, path[1:]))
        # Create a list of all edges, and assign colors based on whether they are in the shortest path or not
        edge_colors = [
            (
                color
                if edge in path_edges or tuple(reversed(edge)) in path_edges
                else self.color
            )
            for edge in self.G.edges()
        ]
        node_colors = [
            ("yellow" if n == l or n == r else color if n in path else self.color)
            for n in self.G.nodes
        ]
        return self.make_image(edge_colors=edge_colors, node_colors=node_colors)
