def generate_dataset(W_actual=1.5, b_actual=0.5, 
                     npoints=100,
                     x_random=False,x_start=0, x_range=1,
                     noise_amplitude=0.2):
    
    if x_random:
        x_data = np.random.randn(npoints)*x_range + x_start
    else:
        x_data = np.linspace(x_start, x_start+x_range, npoints)
        
    noise  = np.random.randn(*x_data.shape) * noise_amplitude
    y_data = x_data * W_actual + b_actual + noise
    
    x_true = np.linspace(min(x_data), max(x_data), 10)
    y_true = x_true * W_actual + b_actual
    
    return(x_data,y_data,x_true,y_true)
