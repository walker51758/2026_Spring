import gurobipy as gp
from gurobipy import GRB

# 9 food items in the problem
prices = [2.89, 2.89, 1.50, 1.89, 2.09, 1.99, 2.49, 0.89, 1.59]

# Constraints coefficients by nutrient
calories = [410, 420, 560, 380, 320, 320, 320, 100, 330]
protein = [24, 32, 20, 4, 12, 15, 31, 8, 8]
fat = [26, 10, 32, 19, 10, 12, 12, 2.5, 10]
sodium = [730, 1190, 1800, 270, 930, 820, 1230, 125, 180]

try:
    m = gp.Model("diet_problem")
    x = m.addVars(9, lb=0.0, name="x")

    # Objective
    m.setObjective(gp.quicksum(prices[i] * x[i] for i in range(9)), GRB.MINIMIZE)

    # Constraints
    m.addConstr(gp.quicksum(calories[i] * x[i] for i in range(9)) >= 1800, "cal_min")
    m.addConstr(gp.quicksum(calories[i] * x[i] for i in range(9)) <= 2200, "cal_max")
    m.addConstr(gp.quicksum(protein[i] * x[i] for i in range(9)) >= 91, "prot_min")
    m.addConstr(gp.quicksum(fat[i] * x[i] for i in range(9)) <= 65, "fat_max")
    m.addConstr(gp.quicksum(sodium[i] * x[i] for i in range(9)) <= 1779, "sod_max")
    # m.addConstr(x[7]+x[8] <= 6, "milk_max")

    m.optimize()

    if m.status == GRB.OPTIMAL:
        print("最优目标值(最小花费):", m.objVal)
        print("最优组合(x):")
        for i in range(9):
            if x[i].x > 1e-9:
                print(f"  x{i+1} = {x[i].x:.6f}")
        print("各约束值:")
        print("  calories=", sum(calories[i] * x[i].x for i in range(9)))
        print("  protein=", sum(protein[i] * x[i].x for i in range(9)))
        print("  fat=", sum(fat[i] * x[i].x for i in range(9)))
        print("  sodium=", sum(sodium[i] * x[i].x for i in range(9)))
    else:
        print("模型没有找到最优解，状态码", m.status)

except gp.GurobiError as e:
    print("Gurobi 错误:", e)
except Exception as e:
    print("其他错误:", e)