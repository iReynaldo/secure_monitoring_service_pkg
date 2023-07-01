class CDN:
    akamai = {20940, 16625}
    cloudflare = {13335}
    verisign = {26415, 30060, 7342, 16838}
    incapsula = {19551}
    neustar = {7786, 12008, 19905}
    conglomerate = akamai | cloudflare | verisign | incapsula | neustar
