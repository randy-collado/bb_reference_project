# Basketball era analysis via fantasy points
A project currently under the works...which era was best for fantasy?

This project is very simple, to analyse the effectiveness of eras in terms of how well they do in fantasy. To start, all I currently have is a url-scrubber for basketball-reference.com (courtesy of Oscar Sanchez from towardsdatascience.com), but the plan is to start with the top 10 effective players from 5 eras and compare them against each other using heuristics from the top 3 fantasy platforms, YahooSports, ESPN Fantasy, and DraftKings Fantasy. Any collaboration would be greatly appreciated

Current Progress:
- Working URL scrubber

Goals:
- Extract data of top 10 players from each era and place them into their own DataFrames (pandas)
- Either average them out or assemble mock fantasy teams for each and assess them over a season (this would require extracting per-game statistics for each player, large data set)
- Compare total fantasy points drawn from each team and use plotlib to show which era trumps others in certain categories
    -Possible method would be to simulate a year using the most effective player from each position during each era 
    -Would it be better to use the same team for all fantasy formats or change teams based on what each fantasy platform deems more valuable?
