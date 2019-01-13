from graphviz import Digraph

g = Digraph('method_a', node_attr={'shape':'box'})

# -- NODES --

g.node('load', label="""Load Information\\nfrom Bulk Data File""")
g.node('lhs', label= """Use LHS to generate\\n1000 load cases""")
g.node('select',     """Select only systems with\\nforce magnitude > 190514.\\n(Number selected ~= 25)""")

# -- Subgraphs --
with g.subgraph(name='cluster_forloop',node_attr={'shape':'box'}) as c:
    c.attr(label="For Each Load Case")
    c.node('foo')

# -- Edges --
g.edge('load', 'lhs')
g.edge('lhs', 'select')
g.edge('select', 'cluster_forloop')

print(g.source)
g.render()
