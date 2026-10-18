def solution(bandage, health, attacks):
    max_health = health
    cast_time, heal_per_sec, bonus_heal = bandage

    attack_dict = {time: damage for time, damage in attacks}

    current_health = health
    success_time = 0

    last_attack_time = attacks[-1][0]

    for time in range(1, last_attack_time + 1):
        if time in attack_dict:
            current_health -= attack_dict[time]
            success_time = 0

            if current_health <= 0:
                return -1

        else:
            success_time += 1
            current_health += heal_per_sec

            if success_time == cast_time:
                current_health += bonus_heal
                success_time = 0

            current_health = min(current_health, max_health)

    return current_health