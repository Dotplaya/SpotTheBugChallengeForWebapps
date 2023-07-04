# Challenge:
# You are performing a code review for an online voting system. Your task is to identify and address any potential 
#  vulnerabilities in the codebase.

@app.route("/vote", methods=["POST"])
def vote():
    candidate_id = request.form.get("candidate_id")
    vote_count = get_vote_count(candidate_id)
    if vote_count is None:
        return "Candidate not found."

    vote_count += 1
    update_vote_count(candidate_id, vote_count)

    return "Vote successfully cast."
