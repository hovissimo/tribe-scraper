tribe-scraper
=============

This is a personal project to help my tribe and I while we play Ark: Survival Evolved.
It leverages a public API provided by arkservers.net and Firebase

The Plan
--------

It's easy to start dreaming up features and start hacking them together, but I feel a phased approach will benefit me the most here.  I'll start by making the arkservers.net data available in realtime via Firebase, and then adding features should be simple and painless (not to mention portable across devices and platforms).

I'm going to start with a Python script that gets data from arkservers.net and pushes it into Firebase.  (The script's role will be to maintain and curate the Firbase state). The data from arkservers isn't as complete as I'd like it to be (specifically, I want to know what Tribe a player belongs to), so this script will add more data (mechanism TBD).

The Future
----------

Nope, there's no future.  This is just a mini hackathon-type project, please don't expect maintenance or support.
