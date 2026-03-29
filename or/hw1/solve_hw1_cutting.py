import gurobipy as gp
from gurobipy import GRB

try:
    m = gp.Model("cutting_stock_user_model")
    
    # 定义 9 个决策变量
    x = m.addVars(9, vtype=GRB.CONTINUOUS, lb=0.0, name="x")
    
    # 目标函数：最小化总原料数
    m.setObjective(gp.quicksum(x[i] for i in range(9)), GRB.MINIMIZE)
    
    # 约束条件
    # 2.9m 需求
    m.addConstr(2*x[0] + 1*x[3] + 1*x[4] + 2*x[5] + 1*x[8] >= 100, "demand_2_9")
    
    # 2.1m 需求
    m.addConstr(3*x[1] + 2*x[3] + 1*x[6] + 2*x[7] + 1*x[8] >= 100, "demand_2_1")
    
    # 1.5m 需求
    m.addConstr(4*x[2] + 3*x[4] + 1*x[5] + 3*x[6] + 2*x[7] + 1*x[8] >= 100, "demand_1_5")
    
    # 求解
    m.optimize()
    
    if m.status == GRB.OPTIMAL:
        print("最优解状态: 成功!")
        print("最小使用钢材数量 (目标值):", m.objVal)
        print("最佳下料方案：")
        for i in range(9):
            if x[i].x > 1e-6:
                print(f"  x{i+1} = {x[i].x}")
    else:
        print("非最优状态，状态码:", m.status)
        
except gp.GurobiError as e:
    print("Gurobi 错误", e)
