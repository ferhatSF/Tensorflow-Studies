import matplotlib.pyplot as plt

def plot_convergence (loss_history,
                      W_history, b_history, 
                      W_actual, b_actual):
    
    plt.style.use('dark_background')
    
    fig  = plt.figure(figsize=(12, 8))
    grid = plt.GridSpec(2, 1, hspace=0.2, wspace=0.2)
    ax1  = fig.add_subplot(grid[0, 0])
    ax2  = ax1.twinx()
    ax3  = fig.add_subplot(grid[1, 0], sharex=ax1)


    color = 'red'
    W_plot,=ax1.plot(W_history,
                  color=color,
                  label="W history -> "+str(W_history[-1]))
    ax1.set_ylabel('W History', color=color)
    ax1.tick_params(axis='W history (W*x+b)', labelcolor=color)
    
    W_True_plot, = ax1.plot([W_actual]*len(W_history),
                            color=color,linestyle="--",
                            label="W ACTUAL: "+str(W_actual))

    color = 'yellow'
    b_plot,=ax2.plot(b_history,
                  color=color,
                  label="\nb history -> "+str(b_history[-1]))
    ax2.set_ylabel('b history', color=color)
    ax2.tick_params(axis='b', labelcolor=color)
    
    b_True_plot, = ax2.plot([b_actual]*len(b_history),
                            color=color,linestyle="--",
                            label="b ACTUAL: "+str(b_actual))

    legend = ax2.legend(
        handles=[W_plot, W_True_plot, b_plot, b_True_plot],
        title=" Model: W * x + b",
        fancybox=True, framealpha=0.8,facecolor="gray",frameon=True) 
        
    color = 'yellow'
    loss,=plt.plot(loss_history,
                   color=color,
                   label="LOSS history-> "+str(loss_history[-1]))
    ax3.set_xlabel('time (iterations)') 
    ax3.set_ylabel('LOSS History', color=color)
    ax3.tick_params(axis='LOSS history', labelcolor=color)
    legend = plt.legend(handles=[loss], 
                        title=" Model: W * x + b \n", 
                        fancybox=True,
                        framealpha=0.8,
                        facecolor="gray",frameon=True) 
    fig.suptitle('GRADIENT DESCENT OPTIMIZER AT WORK', fontsize=16)
        
    plt.show()
    
    return
