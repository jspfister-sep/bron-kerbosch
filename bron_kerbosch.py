import sys

def bron_kerbosch(r, p, x, maximal_cliques=[], level=0):
    print(f'{"  " * level}R={r}, P={p}, X={x}{" <--" if not p and not x else ""}')
    if not p and not x:
        maximal_cliques.append(r)
    else:
        for v in p.copy():
            bron_kerbosch(r | {v}, p & neighbors[v], x & neighbors[v], maximal_cliques, level + 1)
            p.remove(v)
            x.add(v)

def bron_kerbosch_with_pivot(r, p, x, maximal_cliques=[], level=0):
    print(f'{"  " * level}R={r}, P={p}, X={x}{" <--" if not p and not x else ""}', end='')
    if not p and not x:
        maximal_cliques.append(r)
        print('')
    else:
        u = max(p | x, key=lambda s: len(neighbors[s]))
        print(f' Pivot={u}')
        for v in p - neighbors[u]:
            bron_kerbosch_with_pivot(r | {v}, p & neighbors[v], x & neighbors[v], maximal_cliques, level + 1)
            p.remove(v)
            x.add(v)

if __name__ == '__main__':
    neighbors = {
        1 : {2, 5},
        2 : {1, 3, 5},
        3 : {2, 4},
        4 : {3, 5, 6},
        5 : {1, 2, 4},
        6 : {4}}

    if len(sys.argv) > 1 and sys.argv[1] == '-p':
        bron_kerbosch_with_pivot(set(), {1, 2, 3, 4, 5, 6}, set())
    else:
        bron_kerbosch(set(), {1, 2, 3, 4, 5, 6}, set())
