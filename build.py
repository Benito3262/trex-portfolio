X="https://x.com/Trextxxy/status/"
reel=[
("videos","GMGN #GGC: gabbens calls a pump live","2112944849209188587","6.6K views",1),
("videos","GMGN #GGC: dev sold mid-stream","2113661778097762599","5.6K views",1),
("videos","GMGN #GGC: the random wallet that saved him","2114385119217885411","4.2K views",1),
("videos","grvt: app, docs and GitHub in one video","2114114721041318217","1.7K views",1),
("videos","Quip: same physics, no luck excuse","2113903322381897931","1.9K views",1),
("threads","How to use Grok to find the exact Web3 gig","2106987759005052941","23.6K views",0),
("threads","How to create motion graphics using only Grok","2113510732142952921","10.5K views",0),
("threads","How to position yourself for jobs & gigs","2114597895337058699","9.4K views",0),
("threads","How to grow on CT 101","2114235508243202480","7.3K views",0),
("threads","Connection 101","2115323612861272427","4.9K views",0),
("threads","Your KOL reach is limited, how to fix it","2107350138914271497","2.7K views",0),
("campaigns","Quip World (X Article)","2092146158273503684","5.4K views",0),
("campaigns","Xora Finance: the payday mistake (X Article)","2079482413256704005","8.2K views",0),
("campaigns","AgentOS: I have been rude","2096267736296915286","5.1K views",0),
]
cards=""
for i,(c,t,id,v,vid) in enumerate(reel,1):
  th=f'<div class="still"><img loading="lazy" src="v/{id}.jpg" alt=""><span class="playdot">▶</span></div>' if vid else f'<div class="still txt"><span>{c[:-1]}</span></div>'
  cards+=f'<button class="fcard" data-cat="{c}" data-id="{id}" data-vid="{vid}" data-title="{t}" data-v="{v}"><span class="num">{i:02d}</span>{th}<div class="fb"><span class="tag">{c}</span><h4>{t}</h4><small>{v}</small></div></button>'
ledger=[("AgentOS","Content","Writing for @AgentOS_Tech. Studio, Apps, Primeflows, Vault, Chronos, explained like a system you can run.","https://x.com/AgentOS_Tech","ongoing"),
("Quip","Growth","Skill based physics games on Solana. 600+ signups from X into the game.","https://quip.gg/","2+ months"),
("GMGN","Clipper","Clipping the @gmgnai #GGC streams into posts CT actually watches.",X+"2112944849209188587","clips"),
("Bitget & OKX","Campaigns","Exchange campaign content on CT. Posts that travel in the replies.","https://x.com/Trextxxy","campaigns"),
("CardRadar","Content","Giftcard rating project. Check the card before you buy it.","https://x.com/Trextxxy","content"),
("Xora Finance","Long form","X Article: yield on XRP without locking the money away.",X+"2079482413256704005","8.2K views"),
("Aeterna","Brief","Infra for the agent era. Pulled people into the AMA.",X+"2090486499074547906","brief"),
("MOSS AI","Ambassador","Launch story for the Moss Agent Marketplace.",X+"2095407280434917570","ambassador")]
led="".join(f'<a class="lrow" href="{u}" target="_blank" rel="noopener"><span class="li">{i:02d}</span><b>{n}</b><span class="role">{r}</span><span class="ld">{d}</span><em>{m} ↗</em></a>' for i,(n,r,d,u,m) in enumerate(ledger,1))
collabs=[("AgentOS","Content"),("Quip","Growth"),("GMGN","Clipper"),("Bitget","Campaigns"),("OKX","Campaigns"),("Xora Finance","Long form"),("CardRadar","Content"),("MOSS AI","Ambassador"),("Aeterna","Content"),("ZoneX","Video")]
col="".join(f'<div class="collab"><span class="mono">{n[0]}</span><div><b>{n}</b><small>{r}</small></div></div>' for n,r in collabs)
top=[("How to use Grok to find the exact Web3 gig","2106987759005052941","23.6K"),("bro with $5 portfolio is panicking about Binance and bybit hacks","2115915034891260360","19.1K"),
("How to create motion graphics using only Grok","2113510732142952921","10.5K"),("crossed 10k and my fren sent this to my dm","2114039219018486262","10.3K")]
tp="".join(f'<a class="pst" href="{X}{i}" target="_blank" rel="noopener"><strong>{v}</strong><span>impressions</span><p>{t}</p></a>' for t,i,v in top)
tpl=open('tpl.html').read()
open('index.html','w').write(tpl.replace('__COL__',col).replace('__CARDS__',cards).replace('__LED__',led).replace('__TOP__',tp))
