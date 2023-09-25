class CDN:
    akamai = frozenset({20940, 16625})
    cloudflare = frozenset({13335})
    verisign = frozenset({26415, 30060, 7342, 16838})
    incapsula = frozenset({19551})
    neustar = frozenset({7786, 12008, 19905})
    conglomerate = frozenset(akamai | cloudflare | verisign | incapsula | neustar)

    reverse_mapping = {
        akamai: 'akamai',
        cloudflare: 'cloudflare',
        verisign: 'verisign',
        incapsula: 'incapsula',
        neustar: 'neustar',
        conglomerate: 'conglomerate'
    }
