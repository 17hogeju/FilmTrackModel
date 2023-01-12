
## To get media data, run the following:

1. scrape_media.py
    - Gets most popular titles on each streaming platform from Rotten Tomatoes
2. merge_media.py
    - Puts all the gathered media into one json
3. get_imdb_tconsts.py
    - Gets the IMDB tconst for each title (with a matching name)
4. get_imdb_ratings.py
    - Sorts the IMDB tconst dictionary by most popular title name
5. replace_media_ids.py (May need to manually edit some titles to match what is in IMDB)
    - Replaces the ids in the media.json with IMDB tconsts

- To add more data from IMDB, run aggregate_imdb_data.py

