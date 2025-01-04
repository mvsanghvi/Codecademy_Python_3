weight = 41.5

#Ground Shipping:
if weight <= 2:
  cost_ground= 20 + 1.5*weight
elif weight >2 and weight <=6:
  cost_ground= 20 + 3*weight
elif weight >6 and weight <=10:
  cost_ground= 20 + 4*weight
else:
  cost_ground= 20 + 4.75*weight
print("Ground Shipping: $", cost_ground)

#Ground Premium:
ground_premium = 125 + 0*weight
print("Ground Shipping Premium: $", ground_premium)

#Drone Shipping
if weight <= 2:
  cost_drone= 4.5*weight
elif weight >2 and weight <=6:
  cost_drone= 9*weight
elif weight >6 and weight <=10:
  cost_drone= 12*weight
else:
  cost_drone= 14.25*weight
print("Drone Shipping: $", cost_drone)