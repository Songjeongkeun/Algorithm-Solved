from itertools import product


def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]

    best_subscribers = 0
    best_sales = 0

    for discounts in product(discount_rates, repeat=len(emoticons)):
        subscribers = 0
        sales = 0

        for user_discount, user_limit in users:
            total = 0

            for discount, price in zip(discounts, emoticons):
                if discount >= user_discount:
                    total += price * (100 - discount) // 100

            if total >= user_limit:
                subscribers += 1
            else:
                sales += total

        if subscribers > best_subscribers:
            best_subscribers = subscribers
            best_sales = sales
        elif subscribers == best_subscribers and sales > best_sales:
            best_sales = sales

    return [best_subscribers, best_sales]