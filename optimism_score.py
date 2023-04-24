def PmB(score):
    if score <= 1:
        return "Very optimistic"
    elif score <= 3:
        return "Moderate optimistic"
    elif score == 4:
        return "Average"
    elif score <= 6:
        return "Quite pessimistic"
    else:
        return "Very pessimistic"

def PmG(score):
    if score >= 7:
        return "Very optimistic"
    elif score == 6:
        return "Moderate optimistic"
    elif score >= 4:
        return "Average"
    elif score == 3:
        return "Quite pessimistic"
    else:
        return "Very pessimistic"

def PvB(score):
    if score <= 1:
        return "Very optimistic"
    elif score <= 3:
        return "Moderate optimistic"
    elif score == 4:
        return "Average"
    elif score <= 6:
        return "Quite pessimistic"
    else:
        return "Very pessimistic"

def PvG(score):
    if score >= 7:
        return "Very optimistic"
    elif score == 6:
        return "Moderate optimistic"
    elif score >= 4:
        return "Average"
    elif score == 3:
        return "Quite pessimistic"
    else:
        return "Very pessimistic"

def PsB(score):
    if score <= 1:
        return "High self-esteem"
    elif score <= 3:
        return "Moderate self-esteem"
    elif score == 4:
        return "Average"
    elif score <= 6:
        return "Low self-esteem"
    else:
        return "Very low self-esteem"

def PsG(score):
    if score >= 7:
        return "Very optimistic"
    elif score == 6:
        return "Moderately optimistic"
    elif score >= 4:
        return "Average"
    elif score == 3:
        return "Quite pessimistic"
    else:
        return "Very pessimistic"

def TotalB(total):
    if total >= 14:
        return "Very pessimistic"
    elif total >= 12:
        return "Quite pessimistic"
    elif total >= 10:
        return "About average"
    elif total >= 6:
        return "Moderately optimistic"
    else:
        return "Very optimistic"

def TotalG(total):
    if total >= 19:
        return "Very optimistic"
    elif total >= 17:
        return "Moderately optimistic"
    elif total >= 14:
        return "Average"
    elif total >= 11:
        return "Quite pessimistic"
    else:
        return "Very pessimistic"

def GB(G, B):
    total = G - B
    if total >= 8:
        return "Very optimistic"
    elif total >= 6:
        return "Moderately optimistic"
    elif total >= 3:
        return "Average"
    elif total >= 1:
        return "Quite pessimistic"
    else:
        return "Very pessimistic"
