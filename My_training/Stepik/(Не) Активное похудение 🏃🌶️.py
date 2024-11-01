def norma_rate_weight(dey:int = 1, current_weight:float = 1, beginning_weight:float = 100, desired_weight:float = 88,deadline:int = 60):


    dey_norma = (beginning_weight-desired_weight) / deadline
    goal_weight = beginning_weight - (dey_norma * dey)
    status = "Все идет по плану" if current_weight <= goal_weight else "Что-то пошло не так"

    return f"{status}\n#{dey} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight} кг,  ЦЕЛЬ по ВЕСУ = {goal_weight}"


print(norma_rate_weight(10,99))
