#!/usr/bin/env python3

# pip deps: beautifulsoup4 colorama 

from check_lol_version import check_league_of_legend_version
from check_discord_version import check_discord_version

if __name__ == "__main__":
	check_league_of_legend_version("https://ddragon.leagueoflegends.com/api/versions.json")
	check_discord_version("https://discord.en.uptodown.com/windows")
