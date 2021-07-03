import csv

path = "python_challenge/PyPoll/Resources/election_data.csv"
with open(path) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    data = [row for row in csvreader]

    print("--------------------------------------------------")
    print("Election Results")
    print("--------------------------------------------------")




    votes =0
    for row in data:
        votes += 1
    print(f"Total Votes: {votes}")
    print("--------------------------------------------------")

    candidates = {}

    candidate_votes = []
    for row in data:
        candidate_votes.append(row[2])
    unique_candidates = set(candidate_votes)


    for candidate in unique_candidates:
        candidates[candidate] = 0


    for vote in candidate_votes:
        candidates[vote] += 1
    

    candidate_pct = {}
    for candidate in unique_candidates:
        vote_count = candidates[candidate]
        candidate_pct[candidate] = int(round(vote_count/votes * 100, 0))
   

    winner_name =""
    winner_votes = 0
    winner_pct = 0
    for key, value in candidates.items():
        if value > winner_votes:
            winner_votes = value
            winner_name = key
            winner_pct = candidate_pct[key]
    

    for w in sorted(candidates, key = candidates.get):
        
        print(f"{w}: {candidate_pct[w]} % ({candidates[w]})")


    
    print("--------------------------------------------------")
    print((f"WINNER: {winner_name} VOTES: {winner_votes} PERCENTAGE {winner_pct}%"))

    

