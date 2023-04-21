# Speedrun.com V2 API for Python

I am trying to reverse engineer the unreleased v2 speedrun.com API. I hope this isn't illegal!

## API V2 Endpoints

`https://www.speedrun.com/api/v2/GetGameRecordHistory`:
 * __Purpose__: Getting the world record history for a game.
 * __Contents__: List of players that have a world record, and a list of world record runs.

`https://www.speedrun.com/api/v2/GetGameList`:
 * __Purpose__: Listing all games on speedrun.com.
 * __Contents__: Lits of games with some metadata

`https://www.speedrun.com/api/v2/GetGameData`:
 * __Purpose__: A summary of the game leaderboard filtering data.
 * __Contents__: Categories, levels, variables, values, number of runs per category/variable combinations.

`https://www.speedrun.com/api/v2/GetGameSummary`:
 * __Purpose__: A summary of a game mostly containing metadata and statistics.
 * __Contents__: Game metadata, game booster information, moderators, game statistics, series information, a collection of users.

`https://www.speedrun.com/api/v2/GetGameLeaderboard`:
 * __Purpose__: Get leaderboard of a game/category/level/variable/value combination.
 * __Contents__: Category info, game info, platform info, all players of the chosen combination, all runs in the leaderboard, all variable/value information.

`https://www.speedrun.com/api/v2/GetLatestLeaderboard`:
 * __Purpose__: I have literally _no_ idea why this is here.

`https://www.speedrun.com/api/v2/GetUserLeaderboard`:
 * __Purpose__: A summary of all data related to a user.
 * __Contents__: The games, categories, and levels a user has played, other users a user has played with, the user profile, the individual runs by a user, leaderboard position of runs by a user, what variables are active in users' runs.

__THESE ARE NOT IMPLEMENTED YET:__

`https://www.speedrun.com/api/v2/GetSearch`:
 * __Purpose__: Filtering search between games, series, and users?
 * __Contents__: 

`https://www.speedrun.com/api/v2/GetRun`: 
 * __Purpose__: A summary of all the information for a single run.
 * __Contents__: 


## Quirks

Endpoints have request bodies that are encoded base64 JSON with removed padding. Base64 uses `=` to pad an encoded string to a multiple of 4. These are removed upon requests.

## Example Requests

`GET https://www.speedrun.com/api/v2/GetGameLeaderboard?_r=eyJwYXJhbXMiOnsiZ2FtZUlkIjoiNzZyNTV2ZDgiLCJjYXRlZ29yeUlkIjoidzIwdzFsemQiLCJ2YWx1ZXMiOltdLCJ0aW1lciI6MCwicmVnaW9uSWRzIjpbXSwicGxhdGZvcm1JZHMiOltdLCJ2aWRlbyI6MCwib2Jzb2xldGUiOjB9LCJwYWdlIjoxLCJ2YXJ5IjoxNjgyMDgzMjIxfQ`

This request gets the leaderboards for the Any% category of Super Mario Odyssey. The \_r header is encoded base 64. This is what this request is:
```json
{
    "params": {
        "gameId": "76r55vd8",
        "categoryId":"w20w1lzd",
        "values": [
            {
            "variableId":"68km3w4l",
            "valueIds":[
                "zqoyz021"
            ]
            }
        ],
        "timer":0,
        "regionIds":[],
        "platformIds":[],
        "video":0,
        "obsolete":0
    },
    "page":1,
    "vary":1682083221
}
```
