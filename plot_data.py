def plot_data (x_batch,y_batch,y_pred_batch,x_true,y_true):
    
    plt.style.use('dark_background')
    
    fig     = plt.figure(figsize=(13, 10))
    grid    = plt.GridSpec(5, 5, hspace=0.5, wspace=0.5)
    main_ax = fig.add_subplot(grid[:-1, 1:])
    y_hist  = fig.add_subplot(grid[:-1, 0], sharey=main_ax)
    x_hist  = fig.add_subplot(grid[-1, 1:], sharex=main_ax)
    
    data_set = main_ax.scatter(x_batch, y_batch,
                               color="b", label="DATA SET",
                               s=50, alpha=0.6  )
    truth    = main_ax.scatter(x_true , y_true,
                               color='r', label='TRUTH LINEAR',
                               s=200)

    
    if len(y_pred_batch)==0:
        optimized_model, = main_ax.plot   (x_true, y_true, color='y', 
                                           label="LINEAR MODEL",
                                           linewidth=4)
    else:
        optimized_model, = main_ax.plot   (x_batch, y_pred_batch, 
                                           color='cyan',
                                           label="OPTIMIZED MODEL",
                                           linewidth=4)
    handles=[data_set,truth,optimized_model]
        
    main_ax.legend(handles=handles,fancybox=True,
                   framealpha=0.8,facecolor="gray",frameon=True)
    main_ax.set_xlim([min(x_batch),max(x_batch)])
    main_ax.set_ylim([min(y_batch),max(y_batch)])
    main_ax.set_xlabel('X Coordinate')
    main_ax.set_ylabel('Y Coordinate')

    x_hist.hist(y_batch, 40, histtype='stepfilled',
                orientation='vertical',
                color='b',alpha=0.6)
    x_hist.invert_yaxis()

    y_hist.hist(y_batch, 40, histtype='stepfilled',
                orientation='horizontal',
                color='b',alpha=0.6)
    y_hist.invert_xaxis()

    plt.show()
    
    return
