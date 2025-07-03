def solution(balances, requests):
    cashback_times = {}
    last_time = 0

    for a, req in enumerate(requests):
        parts = req.split()
        type_op = parts[0]
        timestamp = int(parts[1])
        acc_id = int(parts[2]) - 1
        amount = int(parts[3])

        cashback_due = [time for time in cashback_times if time <= timestamp]
        for time in sorted(cashback_due):
            for acc_idx, cash_amount in cashback_times[time]:
                balances[acc_idx] += cash_amount
            del cashback_times[time]

        if acc_id < 0 or acc_id >= len(balances):
            return [-(a + 1)]

        if type_op == "deposit":
            balances[acc_id] += amount
        elif type_op == "withdraw":
            if balances[acc_id] < amount:
                return [-(a + 1)]
            balances[acc_id] -= amount
            cashback = int(amount * 0.02)
            cashback_time = timestamp + 86400
            if cashback_time not in cashback_times:
                cashback_times[cashback_time] = []
            cashback_times[cashback_time].append((acc_id, cashback))

    final_time = int(requests[-1].split()[1])
    cashback_due = [time for time in cashback_times if time <= final_time]
    for time in sorted(cashback_due):
        for acc_idx, cash_amount in cashback_times[time]:
            balances[acc_idx] += cash_amount

    return balances
