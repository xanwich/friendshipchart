import matplotlib.pyplot as plt
import networkx as nx
import io
import base64

import matplotlib

matplotlib.use("agg")

# (0.53, 0.91, 0.99, 0.5)


class Grapher:
    def __init__(self, edges):
        self.G = nx.Graph()
        self.G.add_edges_from([(e.l, e.r) for e in edges])

    def make_image(self):
        plt.clf()
        plt.figure(figsize=(12, 12))
        pos = nx.spring_layout(self.G, scale=20, k=2 / (self.G.order() ** 0.5))
        nx.draw_networkx(
            self.G,
            pos=pos,
            node_color=(1, 1, 1, 0.8),
            node_size=150,
            edge_color=(1, 1, 1, 0.8),
            font_family="serif",
        )
        plt.axis("off")
        img = io.BytesIO()
        plt.savefig(img, format="svg", bbox_inches="tight", transparent=True)
        img.seek(0)
        return base64.b64encode(img.getvalue()).decode("utf-8")
