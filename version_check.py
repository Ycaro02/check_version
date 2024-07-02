# pip deps: beautifulsoup4 colorama requests

from check_lol_version import check_league_of_legend_version
from check_discord_version import check_discord_version
from final_fantasy_version import get_ff_last
if __name__ == "__main__":
	check_league_of_legend_version("https://ddragon.leagueoflegends.com/api/versions.json")
	check_discord_version()
	# get_ff_last()
