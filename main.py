import random
import matplotlib.pyplot as plt
from src.final_project.city import City

random.seed(123)

def run_simulation(use_modified_rule, label):
    city = City(size=10, area_rates={
        0: (100, 200),
        1: (50, 250),
        2: (250, 350),
        3: (150, 450)
    })
    city.use_modified_rule = use_modified_rule
    city.initialize()

    for _ in range(180):
        city.iterate()

    return city.history_rates

history_v0 = run_simulation(False, "v0")
history_v1 = run_simulation(True, "v1")

plt.figure(figsize=(14, 7))
for area in [0, 1, 2, 3]:
    plt.plot(history_v0[area], label=f"Area {area} - v0")
plt.xlabel("Month")
plt.ylabel("Average Rate")
plt.title("Average Rate per Area Over Time (Original Rule v0)")
plt.legend()
plt.tight_layout()
plt.savefig("reports/graph2_v0.png")
plt.close()

plt.figure(figsize=(14, 7))
for area in [0, 1, 2, 3]:
    plt.plot(history_v1[area], label=f"Area {area} - v1")
plt.xlabel("Month")
plt.ylabel("Average Rate")
plt.title("Average Rate per Area Over Time (Modified Rule v1)")
plt.legend()
plt.tight_layout()
plt.savefig("reports/graph2_v1.png")
plt.close()

wealth_city = City(size=10, area_rates={
    0: (100, 200),
    1: (50, 250),
    2: (250, 350),
    3: (150, 450)
})
wealth_city.use_modified_rule = False
wealth_city.initialize()

for _ in range(180):
    wealth_city.iterate()

wealth = []
areas = []

for h in wealth_city.hosts:
    value_assets = sum(list(wealth_city.places[pid].price.values())[-1] for pid in h.assets)
    wealth.append(h.profits + value_assets)
    areas.append(h.area)

plt.figure(figsize=(12, 6))
order = sorted(range(len(wealth)), key=lambda i: wealth[i])
plt.bar(range(len(wealth)), [wealth[i] for i in order], color=["C" + str(areas[i]) for i in order])
plt.xlabel("Host")
plt.ylabel("Total Wealth")
plt.title("Wealth per Host")
plt.tight_layout()
plt.savefig("reports/graph1.png")
plt.close()

print("Simulation finished. Graphs generated in reports/ file")