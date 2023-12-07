def weatherprediction(T, H, W):
    W = (0.5*T**2 - 0.2*H + 0.1*W - 15)
    
    if W > 300:
        return "sunny",W
    elif 200 < W <= 300:
        return "cloudy",W
    elif 100 < W <= 200:
        return "rainy",W
    else:
        return "stormy",W

print(weatherprediction(20, 70, 15))