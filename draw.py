import json
from pyecharts import options as opts
from pyecharts.charts import Graph
'''
nodes_data = [
    opts.GraphNode(name="结点1", symbol_size=10),
    opts.GraphNode(name="结点2", symbol_size=20),
    opts.GraphNode(name="结点3", symbol_size=30),
    opts.GraphNode(name="结点4", symbol_size=40),
    opts.GraphNode(name="结点5", symbol_size=50),
    opts.GraphNode(name="结点6", symbol_size=60),
]
links_data = [
    opts.GraphLink(source="结点1", target="结点2", value=2),
    opts.GraphLink(source="结点2", target="结点3", value=3),
    opts.GraphLink(source="结点3", target="结点4", value=4),
    opts.GraphLink(source="结点4", target="结点5", value=5),
    opts.GraphLink(source="结点5", target="结点6", value=6),
    opts.GraphLink(source="结点6", target="结点1", value=7),
]
'''
nodes_data = []
links_data = []
with open('res_dict_old.json','r',encoding='utf-8') as f:
    res = json.load(f)
for k in res:
    src = k.split('#')[0]
    tar = k.split('#')[1]
    if res[k]==1 and res[tar+'#'+src]==2:
        links_data.append((src,tar))
        nodes_data.append(src)
        nodes_data.append(tar)
nodes_data = list(set(nodes_data))
links_data = list(set(links_data))
nodes_data = [opts.GraphNode(name=x) for x in nodes_data]
links_data = [opts.GraphLink(source=x[0], target=x[1]) for x in links_data]
print(len(links_data))
c = (
    Graph()
    .add(
        "",
        nodes_data,
        links_data,
        repulsion=500,
        edge_symbol=[ None,'arrow']
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="prerequisite relations")
    )
    .render("relations_old.html")
)