def bootstrap_mean(array, n):
    #mean bootstrapping for 95% confidence interval
    #n is the number of bootstrapping samples
    averages=np.zeros(n)
    for i in range(n):
        averages[i]=(np.mean(random.choices(array, k=len(array))))
    averages=np.sort(averages)
    return (averages[math.floor(0.05*(n-1))], averages[math.ceil(0.95*(n-1))])
