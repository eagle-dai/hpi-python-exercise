
def fitrac_generator():
    return "r5c97m", 58.6, [3.042, 1.541, 1.503, 8.303, 1.681, 1.531]
    
def hexID_generator(seed=0):
    import random
    if seed != 0:
        random.seed(seed)
    return ''.join([random.choice('0123456789abcdef') for n in range(6)])

orig = {
'hexID': "k8z61d",
'screentime': 119.4,
'acc':[2.025, 2.161, 1.872, 1.870, 4.569, 1.823],
'tz': "UTC",
'device':"smart_watch_14",
'group':'treatment_D',
'dose': 17
}

new = {
'hexID': "k8z61d",
'screentime': 132.7,
'age':25,
'group':'treatment_D',
'country':"DE"
}
