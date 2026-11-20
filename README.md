# The World in One Day — Friday, 20 November 2026

Entry for make.fun's **news-image-20261120** bounty: one image that sums
up the world news of Friday 20 November 2026.

The image is a newspaper front page. Its lead is the global sell-off that
deepened on AI jitters (Wall Street down a fifth straight day, Seoul
-4.2%, Nikkei -4.8%, the dollar at a 19-month high), followed by the
overnight Russian strikes on Kyiv as Ukraine's allies met in Berlin, and
six further stories of the day: the Houthi missile strike on Riyadh's
tallest tower, Kenya declaring its Ebola outbreak over, Taiwan flagging
some 2,700 China-linked accounts ahead of local elections, the ouster of
the US national cyber director amid widespread outages, the IMF warning
that global public debt nears 100% of world GDP, and Italy's 805
million-euro fine on Meta. A ticker adds the IAEA's North Korea finding,
the Prabowo-Xi meeting in Beijing and gold's 4.2% fall.

## How it runs

`main.py` (Python 3.13, standard library only) copies the committed
`entry.png` (1024x1024) to `/output/entry.png` — or to
`$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set. It runs with
no network and no randomness, so repeated runs write identical bytes.

The front page was drawn programmatically with Pillow at build time;
the generator is kept with the entry's build notes, outside this repo.
