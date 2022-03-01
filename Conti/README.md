# Conti Ransomware Leaks

This repository contains relevant files and information pertaining to the Conti Ransomware Leaks and my research. I do endorse the use of Ransomware in any way, shape, or form. This is strictly for academic purposes.

*@ziggoon : zack musgrave*

# Jabber Chat Leaks / Analysis (~60694 messages)
Download: https://share.vx-underground.org/Conti/

Source for Russian to English translation: [Russian to English](https://medium.com/@arnozobec/analyzing-conti-leaks-without-speaking-russian-only-methodology-f5aecc594d1b)

How I Converted Russian Chats to English: 

-Concatenate all the JSON files + Prettify using jq:
    
    cat \*.json | jq -cr > big.json

-Convert Russian to English using RUtoEN.py
-Repeat Step 1 on the English translation:

    cat output.json | jq -cr > out2.json
    
-Now JSON is pretty and translated *(some errors may occur and translations aren't perfect)*

# URLs

Grab URLs from JSON:

    egrep '(http|https):\/\/\[a-zA-Z0-9.\/?=_%&:-]*' -o big.json > full_url_output.txt
    
    cat url_output.txt | grep .onion > onion_urls.txt

CONTI Admin Login Page - http://czb6edlp7gsar4u5crxccldjkjn36p35fro7c7gck7wjumcrzq4efgid.onion/zeh7dkwfdxw99tdk/

CONTI.Recovery Chat - http://contirec7nchr45rx6ympez5rjldibnqzh7lsa56lvjvaeywhvoj3wad.onion/

!!Active 2/28!! Chat - http://contirec7nchr45rx6ympez5rjldibnqzh7lsa56lvjvaeywhvoj3wad.onion/chat/56e2f25572050b4699a847ec90a94675c27c73f2f68aae0a82a5c2a8d25dd7fd

Internal Conti RocketChat Server - https://6yp2jljwgdxmwy4uxfaxbkjgm2txlxxb5akxn43cyaz3cjo2gqd65yid.onion/home

RocketChat Server 2 - https://xflemdsxjrjilw34dsxpvrxp5whnaut7hc5xejwuqs6eqrkt77bxkwid.onion

CONTI.News - http://continewsnv5otx5kaoje7krkto2qbu3gtqef22mnr7eaxw3y6ncz3ad.onion/

## Conti Dashboard Images
[Conti Customer Chat](https://i.imgur.com/PeUqIrh.png)

[Conti Internal RocketChat  Server](https://i.imgur.com/Gbo5IMk.png)

