#!/bin/bash
if [ ! -f name.basics.tsv.gz ]; then
    curl https://datasets.imdbws.com/name.basics.tsv.gz > name.basics.tsv.gz
fi
if [ ! -f title.akas.tsv.gz ]; then
    curl https://datasets.imdbws.com/title.akas.tsv.gz > title.akas.tsv.gz
fi
if [ ! -f title.basics.tsv.gz ]; then
    curl https://datasets.imdbws.com/title.basics.tsv.gz > title.basics.tsv.gz
fi
if [ ! -f title.crew.tsv.gz ]; then
    curl https://datasets.imdbws.com/title.crew.tsv.gz > title.crew.tsv.gz
fi
if [ ! -f title.episode.tsv.gz ]; then
    curl https://datasets.imdbws.com/title.episode.tsv.gz > title.episode.tsv.gz
fi
if [ ! -f title.principals.tsv.gz ]; then
    curl https://datasets.imdbws.com/title.principals.tsv.gz > title.principals.tsv.gz
fi
if [ ! -f title.ratings.tsv.gz ]; then
    curl https://datasets.imdbws.com/title.ratings.tsv.gz > title.ratings.tsv.gz
fi
